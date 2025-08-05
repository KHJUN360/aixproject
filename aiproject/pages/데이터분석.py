import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit 페이지 설정
st.set_page_config(page_title="학생 성적 시각화", layout="wide")

# 페이지 제목
st.title("학생 성적 시각화 대시보드")

# 데이터 준비
data = {
    "name": ["lee", "part", "kim"],
    "grade": [2, 2, 2],
    "number": [1, 2, 3],
    "kor": [90, 88, 99],
    "eng": [91, 89, 99],
    "math": [81, 77, 99],
    "info": [100, 100, 100]
}
df = pd.DataFrame(data)

# 데이터프레임 표시
st.subheader("학생 성적 데이터")
st.dataframe(df, use_container_width=True)

# 레이아웃을 위한 컬럼 생성
col1, col2 = st.columns(2)

# 막대 그래프
with col1:
    st.subheader("과목별 학생 성적 (막대 그래프)")
    fig_bar = px.bar(
        df,
        x="name",
        y=["kor", "eng", "math", "info"],
        barmode="group",
        title="학생별 과목 점수 비교",
        labels={"name": "학생 이름", "value": "점수", "variable": "과목"}
    )
    fig_bar.update_layout(
        xaxis_title="학생 이름",
        yaxis_title="점수",
        legend_title="과목",
        template="plotly_white",
        height=400
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# 선 그래프
with col2:
    st.subheader("과목별 학생 성적 (선 그래프)")
    fig_line = px.line(
        df,
        x="name",
        y=["kor", "eng", "math", "info"],
        title="학생별 과목 점수 추이",
        labels={"name": "학생 이름", "value": "점수", "variable": "과목"},
        markers=True
    )
    fig_line.update_layout(
        xaxis_title="학생 이름",
        yaxis_title="점수",
        legend_title="과목",
        template="plotly_white",
        height=400
    )
    st.plotly_chart(fig_line, use_container_width=True)

# 평균 점수 히스토그램
st.subheader("과목별 평균 점수 (히스토그램)")
df_mean = df[["kor", "eng", "math", "info"]].mean().reset_index()
df_mean.columns = ["subject", "average_score"]
fig_hist = px.bar(
    df_mean,
    x="subject",
    y="average_score",
    title="과목별 평균 점수",
    labels={"subject": "과목", "average_score": "평균 점수"},
    color="average_score",
    color_continuous_scale="Blues"
)
fig_hist.update_layout(
    xaxis_title="과목",
    yaxis_title="평균 점수",
    template="plotly_white",
    height=400
)
st.plotly_chart(fig_hist, use_container_width=True)

# 데이터 설명
st.markdown("""
### 데이터 설명
- **데이터**: 2학년 학생(lee, part, kim)의 국어(kor), 영어(eng), 수학(math), 정보(info) 과목 점수.
- **시각화**:
  - **막대 그래프**: 학생별 각 과목 점수를 비교.
  - **선 그래프**: 학생별 과목 점수 추이를 확인.
  - **히스토그램**: 과목별 평균 점수를 시각화.
""")