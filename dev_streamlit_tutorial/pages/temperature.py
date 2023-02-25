import streamlit as st
import pandas as pd

# データ操作
st.markdown('### データ操作 のサンプル')
link_chart_widjets = '[chart widjets](https://docs.streamlit.io/library/api-reference/charts#chart-elements)'
st.markdown(f'これは {link_chart_widjets} を使ったサンプルです. ')
st.markdown(f'チャートウィジェットについては {link_chart_widjets} を参照してください.')

# csv データを読み込んでオブジェクトを格納します
# あとは Streamlit の API 経由でこのオブジェクトを扱うだけで色々なチャートでデータを見ることができます
data_file = pd.read_csv("./dev_streamlit_tutorial/data/temperature.csv",
                        index_col='月')

# レイアウト調整, ページレイアウトを 4分割 します
# ここでは温度データをテーブル、折れ線グラフ、棒グラフ(2021年), 棒グラフ(2022年) で表示させてみます
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.caption('温度データをテーブルで表示')
    st.table(data_file)

with col2:
    st.caption('温度データを折れ線グラフで表示')
    st.line_chart(data_file)

with col3:
    st.caption('温度データを棒グラフで表示(2021年)')
    st.bar_chart(data_file['2021年'])

with col4:
    st.caption('温度データを棒グラフで表示(2022年)')
    st.bar_chart(data_file['2022年'])