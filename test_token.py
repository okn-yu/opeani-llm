import os
import openai 
import streamlit as st
import tiktoken


openai.api_key = os.getenv("OPENAI_API_KEY")

enc = tiktoken.get_encoding("cl100k_base")
tokens = enc.encode("こんにちは、世界")
print(len(tokens))
print(tokens)
