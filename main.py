from ocr import process_image
from post import post_to_notion
from trimming import refine_text_with_openai

def main():
    print("1. 이미지 처리 시작")
    extracted_text = process_image()
    if not extracted_text:
        print("이미지 처리 중 오류가 발생했습니다. 프로그램을 종료합니다.")
        return

    print("\n추출된 텍스트:")
    print(extracted_text)

    print("\n2. OpenAI API를 사용하여 텍스트 수정하시겠습니까? y/n")
    answer = input()
    if answer == "y":
        openai_api_key = input("OpenAI API 키를 입력하세요: ")
        refined_text = refine_text_with_openai(openai_api_key, extracted_text)
        if not refined_text:
            print("텍스트 수정 중 오류가 발생했습니다. 프로그램을 종료합니다.")
            return

        print("\n수정된 텍스트:")
        print(refined_text)

        print("\n3. 노션에 텍스트 업로드")
        notion_api_key = input("Notion API 키를 입력하세요: ")
        page_id = input("Notion 페이지 ID를 입력하세요: ")
        title = input("노션에 생성할 페이지 제목을 입력하세요: ")
        post_to_notion(notion_api_key, page_id, title, refined_text)
    elif answer == "n":
        print("\n2. 노션에 텍스트 업로드")
        notion_api_key = input("Notion API 키를 입력하세요: ")
        page_id = input("Notion 페이지 ID를 입력하세요: ")
        title = input("노션에 생성할 페이지 제목을 입력하세요: ")
        post_to_notion(notion_api_key, page_id, title, extracted_text)
    else:
        print("입력하신 값이 정확하지 않습니다. 수정을 생략합니다.")
        print("\n2. 노션에 텍스트 업로드")
        notion_api_key = input("Notion API 키를 입력하세요: ")
        page_id = input("Notion 페이지 ID를 입력하세요: ")
        title = input("노션에 생성할 페이지 제목을 입력하세요: ")
        post_to_notion(notion_api_key, page_id, title, extracted_text)

if __name__ == "__main__":
    main()
