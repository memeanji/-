import streamlit as st
import folium
from streamlit_folium import st_folium

# 앱 제목
st.title("Re:Team | LOCALREADY")

# 탭 나누기
tabs = st.tabs([
    "1단계 - 일거리 매칭 및 후기 시스템",
    "2단계 - 포인트 마켓 & 체험 탐색",
    "3단계 - AI 매칭 & 정책 알림",
    "4단계 - 커뮤니티 & 데이터 분석"
])

# --- 1단계: 일거리 매칭 ---
with tabs[0]:
    st.header("📌 1단계: 일거리 매칭 및 후기 시스템")

    st.subheader("일거리 등록 (클라이언트)")
    with st.form("register_job"):
        job_title = st.text_input("업무 제목")
        job_type = st.radio("업무 기간", ["단기", "장기"])
        provide_meals = st.checkbox("식사 제공")
        provide_stay = st.checkbox("숙소 제공")
        submit_job = st.form_submit_button("등록하기")
        if submit_job:
            st.success("✅ 일거리가 등록되었습니다!")

    st.divider()

    st.subheader("사용자 일거리 검색")
    selected_type = st.selectbox("기간", ["전체", "단기", "장기"])
    keyword = st.text_input("키워드 검색 (예: 사과 수확, SNS 마케팅 등)")
    st.button("🔍 검색")

    st.divider()

    st.subheader("후기 등록")
    job_id = st.text_input("참여한 일거리 ID")
    feedback = st.text_area("후기 작성", key="job_feedback")
    st.button("후기 제출")

# --- 2단계: 포인트 마켓 + 체험 탐색 ---
with tabs[1]:
    st.header("💰 2단계: 포인트 마켓 & 체험형 프로젝트")

    st.subheader("체험형 프로젝트 검색")
    region = st.selectbox("지역 선택", ["전라남도", "경상북도", "충청남도"])
    provide_accommodation = st.checkbox("숙소 제공")
    provide_meal = st.checkbox("식사 제공")
    st.button("🔍 체험 프로그램 찾기")

    st.divider()

    st.subheader("포인트 잔액 보기 / 사용처 확인")
    st.metric("내 포인트", "3,200P")
    st.selectbox("사용처 검색", ["전통시장 식당", "게스트하우스", "지역 카페"])
    st.button("QR 결제하기")

# --- 3단계: AI 매칭 및 정책 알림 ---
with tabs[2]:
    st.header("🤖 3단계: AI 매칭 & 정책 추천")

    st.subheader("추천 일거리")
    st.info("협업 필터링 기반 추천 시스템 적용 예정")
    st.button("AI 추천 받기")

    st.subheader("정책 추천")
    age = st.number_input("나이", 18, 40)
    region = st.selectbox("거주 지역", ["서울", "광주", "강원", "제주"])
    interest = st.multiselect("관심 분야", ["귀촌", "창업", "문화", "주거"])
    st.button("정책 추천 받기")

# --- 4단계: 커뮤니티 & 데이터 분석 ---
with tabs[3]:
    st.header("🗣 4단계: 커뮤니티 & 데이터 시각화")

    st.subheader("자유 후기 게시판")
    post = st.text_area("후기 작성", key="community_post")
    st.button("게시하기")

    st.divider()

    st.subheader("인기 지역 키워드 시각화 (지도)")

    # 지도 생성 (중심: 대한민국)
    m = folium.Map(location=[36.5, 127.8], zoom_start=7)

    # 예시 데이터: (위도, 경도, 키워드, 아이콘)
    locations = [
        (36.3525, 128.6978, "경북 의성", "사과", "🍎"),
        (34.5741, 126.5986, "전남 해남", "SNS", "📱"),
        (36.1871, 127.098, "충남 논산", "기타", "⭐"),
    ]

    for lat, lon, region, keyword, icon in locations:
        folium.Marker(
            location=[lat, lon],
            popup=f"{region} - {keyword}",
            icon=folium.DivIcon(html=f"""<div style="font-size:24px;">{icon}</div>""")
        ).add_to(m)

    st_folium(m, width=700, height=500)

