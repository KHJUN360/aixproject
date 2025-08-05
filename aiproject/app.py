import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()
df = pd.read_csv('./data/mydata.csv')

#global veriable
url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'


st.title('This is my first webapp!!')
col1, col2 = st.columns((4, 1))
with col1 :
    with st.expander('Subcontent1...') :
        st.subheader('SubContent1...')
        st.video(url)

    with st.expander('Subcontent2...') :
        st.subheader('Image Content...')
        st.image('./images/catdog.jpg')

    with st.expander('Subcontent3...') :
        st.subheader('html Content...')
        import streamlit.components.v1 as htmlviewer
        with open('./htmls/index.html', 'r', encoding='utf-8') as f:
            html1 = f.read()
            f.close()
        htmlviewer.html(html1, height = 800)

    with st.expander('Subcontent4...') :
        st.subheader('data app Content...')
        st.table(df)
        st.write(df.describe())
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

with col2 :
    with st.expander('Tips...'):
        st.info('Tips........')