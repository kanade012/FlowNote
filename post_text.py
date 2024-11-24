import requests
import json

# 노션 API 키 및 페이지 ID 설정
NOTION_API_KEY = ""
PARENT_PAGE_ID = ""  # 노션 페이지의 ID

# 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# 전송할 텍스트 정의
text_to_add = "이것은 페이지에 추가될 내용입니다."

# 페이지에 블록 추가
def create_page_in_parent(parent_id, title, content):
    url = "https://api.notion.com/v1/pages"

    data = {
        "parent": {
            "page_id": parent_id  # 부모 페이지 ID
        },
        "properties": {
            "title": {  # 새 페이지의 제목
                "title": [
                    {
                        "text": {"content": title}
                    }
                ]
            }
        },
        "children": [
            {  # 페이지 안에 내용 추가 (단락 블록)
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": content
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("새 페이지가 성공적으로 생성되었습니다!")
        print("응답 데이터:", response.json())
    else:
        print("오류 발생:", response.status_code, response.text)

# 새 페이지 생성
create_page_in_parent(
    PARENT_PAGE_ID,
    "새로운 페이지 제목",  # 페이지 제목
    "이것은 새로운 페이지에 추가될 내용입니다."  # 페이지 내용
)