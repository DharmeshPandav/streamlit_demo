import streamlit as st


def app():

    radio_list = ["Eat", "Sleep", "Both"]

    params = st.experimental_get_query_params()
    if not params:
        params = {}
    first_params = {key: values[0] for key, values in params.items()}
    activity_from_param = int(first_params.get("activity", 0))
    # Query parameters are returned as a list to support multiselect.
    # Get the first item in the list if the query parameter exists.
    activity = st.radio(
        "What are you doing at home during quarantine?", radio_list, index=activity_from_param, key="abc"
    )
    if activity:
        st.experimental_set_query_params(activity=radio_list.index(activity))

    st.write(st.session_state.abc)
    params = st.experimental_get_query_params()
    if not params:
        params = {}
    first_params = {key: values[0] for key, values in params.items()}
    activity_from_param = int(first_params.get("activity", 0))
    st.write(activity_from_param)
    st.balloons()
    st.write("end")
