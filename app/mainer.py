import streamlit as st
from daliegenerator import sending_picture ,sending_picture_small ,sending_picture_azure



st.header("Hello WIX !!!")
title = 'wix'

texts = ['WIX icon beautiful realistic with snowflake super cool and shine ','WIX icon carton realistic with snowflake super cool and shine ','WIX icon fantasy realistic with snowflake super cool and shine ','WIX i]
for _text in text:
    st.image(sending_picture_azure(_text),caption=title,use_column_width="always")