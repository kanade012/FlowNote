import os
from dotenv import load_dotenv
import openai

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def refine_text(input_text):
    try:
        # GPT 요청
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that refines text. You correct typos, improve grammar, split paragraphs, and make sentences more natural."},
                {"role": "system", "content": "If the input text is in Korean, please write it in a way that is appropriate for the Korean language."},
                {"role": "user", "content": f"Please refine the following text:\n\n{input_text}"}
            ]
        )

        # 응답 반환
        return response['choices'][0]['message']['content']

    except openai.AuthenticationError:
        return "Invalid API key. Please check your .env file."
    except openai.RateLimitError:
        return "Rate limit exceeded. Please wait and try again."
    except openai.OpenAIError as e:
        return f"An OpenAI error occurred: {e}"

# 사용자 입력
if __name__ == "__main__":
    input_text = input("Enter the text you want to refine:\n")
    refined_text = refine_text(input_text)
    print("\nRefined Text:\n")
    print(refined_text)
