def refine_text_with_openai(api_key, input_text):
    import openai

    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that refines text. You correct typos, improve grammar, split paragraphs, and make sentences more natural."},
                {"role": "system", "content": "If the input text is in Korean, please write it in a way that is appropriate for the Korean language."},
                {"role": "user", "content": f"Please refine the following text:\n\n{input_text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
