import streamlit as st


def app():

    st.text_input("A", key="demo_a")
    st.write(f"Value of A: {st.session_state.demo_a}")
