def post_to_notion(api_key, page_id, title, content):
    import requests
    import json

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": {"page_id": page_id},
        "properties": {
            "title": {
                "title": [{"text": {"content": title}}]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": content}}]
                }
            }
        ]
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("노션에 페이지가 성공적으로 생성되었습니다.")
    else:
        print(f"오류 발생: {response.status_code} - {response.text}")
