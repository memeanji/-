# 파일명: localink_app.py

import streamlit as st
import pandas as pd

# 샘플 데이터프레임
df = pd.DataFrame({
    "지역": ["강릉", "군산", "대전", "부산", "제주", "전주"],
    "직무": ["데이터분석", "프론트엔드", "백엔드", "데이터엔지니어", "UX디자인", "데이터분석"],
    "월세(만원)": [35, 28, 40, 45, 38, 30],
    "병원수": [12, 10, 30, 50, 25, 20],
    "교통편수": [8, 6, 12, 18, 10, 9],
    "위도": [37.75, 35.97, 36.35, 35.18, 33.5, 35.82],
    "경도": [128.88, 126.71, 127.38, 129.07, 126.53, 127.15]
})

st.title("🧭 나에게 맞는 디지털 정착지 추천 서비스")
# 1. 입력 받기
job = st.selectbox("희망 직무를 선택하세요", df["직무"].unique())
max_rent = st.slider("최대 월세 예산 (만원)", 20, 70, 35, step=1)
# 2. 필터링

filtered = df[(df["직무"] == job) & (df["월세(만원)"] <= max_rent)].copy()


# 3. 점수 계산 및 결과 출력
filtered["정착점수"] = (
    (50 - filtered["월세(만원)"]) * 1.5 +
    filtered["병원수"] * 1.0 +
    filtered["교통편수"] * 1.2
)

filtered = filtered.sort_values("정착점수", ascending=False)

st.subheader("📊 정착지 추천 순위")
st.dataframe(filtered[["지역", "직무", "월세(만원)", "병원수", "교통편수", "정착점수"]])

# 4. 지도 시각화
st.map(filtered.rename(columns={"위도": "lat", "경도": "lon"}))

# 5. 지역 선택
selected_region = st.selectbox("정착지 상세 보기", filtered["지역"].unique())

# 6. 선택 지역의 채용공고 표시
st.subheader(f"📌 {selected_region} 지역의 '{job}' 채용공고")
st.markdown("- 예시 공고 1")
st.markdown("- 예시 공고 2")

# 7. 살아보기 신청 버튼
if st.button("이 지역 살아보기 신청하기"):
    st.success(f"{selected_region} 신청이 완료되었습니다! 담당자가 곧 연락드릴 예정입니다.")
