# FlowNote
## 🤷‍♂️ FlowNote란? 
1️⃣ _"수업시간, 노트에 필기한 걸 디지털로 옮길 수 없을까?"_ 라는 고민에서 출발한 프로젝트!    
2️⃣ 손글씨를 디지털 텍스트로 변환시켜 노션에 작성해 주는 프로그램   
3️⃣ `Flow` + `Note` 두 단어를 합친 글자로 자연스러운 연결과 흐름으로 노트 필기를 돕는다는 의미를 지님   

### 📌 실행 방법
`main.py`를 실행   
### 📌 실행 데모
<img src="https://github.com/user-attachments/assets/63eeb16c-5111-4404-9bcb-e1d42ba43e57" width="300" height="600"/> 
<img src="https://github.com/user-attachments/assets/bd6902aa-a16e-4ba5-8fc6-7e0373c8ad50" width="300" height="600"/>     

손글씨 이미지를 인식한 모습   

<img src="https://github.com/user-attachments/assets/786a7ec5-1140-4cbe-83bc-8ee15e753f72" width="500" height="200"/>     

텍스트로 변환한 내용을 노션에 적용한 모습

## 🔍 Flow chart 
다음 흐름에 따라 프로그램을 진행
```mermaid
graph LR
A[손글씨 촬영] -- OCR --> B(텍스트로 변환)
B -- OpenAI API --> C(문법 검사)
C -- Notion API --> D(노션에 저장)
```

## ✅ Preparation
프로그램을 실행하기 전 필요한 요소    
- 폰트 파일
- OpenAI API key
- Notion API key

## 👥 Member
- __ImageProcessing 팀__ ([김채연](https://github.com/chaechae10),[박승규](https://github.com/ParkSeungGyu1))  
  `feature/imageProcessing` 브랜치에서 개발
- __Trimming_gpt 팀__ ([황고은](https://github.com/HwangGoeun),[황유림](https://github.com/yulimmm))   
  `feature/Trimming_gpt` 브랜치에서 개발
- __Export 팀__ ([장영하](https://github.com/kanade012))   
  `export` 브랜치에서 개발
