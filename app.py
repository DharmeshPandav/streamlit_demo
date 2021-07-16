import streamlit as st

from apps import demo_session_state
from apps import demo_query_param

params = st.experimental_get_query_params()
first_params = {key: values[0] for key, values in params.items()}
app = first_params.get("app")
apps = ["Session State", "Query Param"]
if app and app in apps:
    app_index = apps.index(app)
else:
    app_index = 0

app_selected = st.sidebar.selectbox("Select app", apps, index=app_index)
if app_selected == "Query Param":
    demo_query_param.app()
elif app_selected == "Session State":
    demo_session_state.app()
