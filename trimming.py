def refine_text_with_openai(api_key, input_text):
    import openai

    openai.api_key = api_key

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that improves text readability."},
                {"role": "user", "content": f"Please refine the following text:\n{input_text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
