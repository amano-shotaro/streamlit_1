import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Stream lit 超入門')

st.write('プレグレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

"Done!"

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')

text = st.text_input(
    'What is your hobby?'
)
slider = st.slider(
    'How are you feeling?', 0, 100, 50
)
option = st.selectbox(
    'What is your favorite number?',
    list(range(1, 11))
)
f'Your hobby: {text}.'
f'Your condition: {slider}'
f'Your favorite number: {option}.' 

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('bird.jpg')
    st.image(img, caption='Bird', use_container_width=True)


st.write('Data Frame')

# df = pd.DataFrame({
#     '1st col': [1,2,3,4],
#     '2nd col': [10,20,30,40],
# })

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

st.write("折れ線ブラフ line_chart")
st.line_chart(df) 

st.write("エリアグラフ area_chart")
st.area_chart(df)

st.write("棒グラフ bar_chart")
st.bar_chart(df)

df = pd.DataFrame(
    np.random.randn(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.write("地図 map")
st.map(df, size=30)

# """
# # 章
# ## 節
# ### 項
# ```python 
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
