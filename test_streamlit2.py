import os
import openai
import streamlit as st
import time
 
openai.api_key = os.getenv("OPENAI_API_KEY")


with st.form("my_form", clear_on_submit=False):
    question = st.text_input('質問を入力してください')
    submitted = st.form_submit_button('質問を実行')
     
     
if submitted:
    with st.spinner('実行中です...'):
        time.sleep(3)
    st.subheader('GPTによる回答')

    question += "。日本語で回答してください"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    st.text(response['choices'][0]['text'])
