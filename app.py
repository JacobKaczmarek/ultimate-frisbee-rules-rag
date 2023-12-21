import sys
import streamlit as st
sys.path.insert(0, 'src')

from ultimate_frisbee_rules_rag.pipelines.query_rag_model import QueryRagModelPipeline


st.title("Ultimate Frisbee Rules Chat 🥏")

pipeline = QueryRagModelPipeline()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    response = pipeline.main(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})