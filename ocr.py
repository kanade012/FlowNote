def process_image():
    import cv2
    import numpy as np
    import easyocr
    from PIL import Image, ImageDraw
    import matplotlib.pyplot as plt

    print("이미지를 처리 중입니다. 업로드할 이미지를 선택하세요.")
    file_path = input("이미지 파일 경로를 입력하세요: ")

    # 이미지 로드
    image = cv2.imread(file_path)
    if image is None:
        print("이미지를 불러올 수 없습니다. 경로를 확인하세요.")
        return None

    print("이미지 처리 중...")
    reader = easyocr.Reader(['en', 'ko'])
    result = reader.readtext(image)

    # 텍스트만 추출
    extracted_text = [detection[1] for detection in result]

    # 경계 상자 표시
    image_pil = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image_pil)
    for detection in result:
        coords = detection[0]
        x_min, y_min = map(int, coords[0])
        x_max, y_max = map(int, coords[2])
        draw.rectangle(((x_min, y_min), (x_max, y_max)), outline="red", width=2)

    plt.figure(figsize=(20, 20))
    plt.imshow(np.asarray(image_pil))
    plt.axis("off")
    plt.show()

    print("텍스트 추출 완료.")
    return " ".join(extracted_text)
