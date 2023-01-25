import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトル
st.title("Streamlit introduction")

st.write("DataFrame")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text("Iterarion {}".format(i+1))
    bar.progress(i+1)
    time.sleep(0.1)

df = pd.DataFrame(
    np.random.rand(20,2)/50 + [35.69, 139.70],
    columns = ["lat", "lon"]
)

st.map(df)

# 折れ線グラフ
st.line_chart(df)

# 折れ線グラフ(塗りつぶし)
st.area_chart(df)

#マークダウン
"""
# hello
## hello
### hello
"""

#動的なテーブルを描写
st.write(df)

#動的なテーブルを描写　オプションが多い
st.dataframe(df, width = 100, height = 100)

#静的なテーブルを表示
st.table(df)


st.write("Display Image")

img = Image.open("dog.jpg")

#チェックボックスはboole型を返す
if st.checkbox("show image"):
    st.image(img, caption = "dog", use_column_width = True)

option = st.selectbox("好きな数字は何ですか？", list(range(1,11)))

st.write("あなたの好きな数字は"+str(option)+"です。")

#サイドバーに表示される
text = st.sidebar.text_input("あなたの名前を教えてください")
age = st.sidebar.slider("年齢は？", 0, 100, 50)

st.write("あなたの好きな名前は"+text+"です。")

st.write(str(365 * age)+"日間生きました")

left_columns , right_columns = st.columns(2)

if left_columns.button("押すなよ"):
    right_columns.write("押したらあかんって")

expander = st.expander("おなかすいた")

expander.write("セブン→ナナチキ→満足")

