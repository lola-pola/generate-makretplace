import streamlit as st
from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure


st.write("https://github.com/lola-pola/generate-makretplace")

st.image('code.png',caption='qrcode',use_column_width="always", width=200)


st.header("Hello WIX !!!")
title = 'wix'

texts = ['WIX icon beautiful realistic with snowflake super cool and shine ',
         'WIX icon carton realistic with snowflake super cool and shine ',
         'WIX icon fantasy realistic with snowflake super cool and shine ']
for _text in texts:
    st.image(sending_picture_azure(_text),caption=title,use_column_width="always", width=200)