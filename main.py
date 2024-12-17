import streamlit as st
import langchain_helper

custom_css = """
<style>
/* Style for the header */
h1 {
    font-family: 'Arial', sans-serif;
    color: #1e81b0;
    text-align: center;
    border-bottom: 2px solid #1e81b0;
    padding-bottom: 10px;
}

/* Style for the subtitle */
h2 {
    font-family: 'Arial', sans-serif;
    color: #023e8a;
    margin-top: 30px;
    font-size: 1rem;
}

/* Style for the list of universities */
ul {
    list-style-type: circle;
    padding-left: 20px;
}

li {
    font-family: 'Verdana', sans-serif;
    color: #495057;
    font-size: 16px;
    margin: 5px 0;
}

/* Add padding and background color */
body {
    background-color: #f7f9fb;
    padding: 20px;
}
</style>
"""

st.title("Recommended Universities for Pursuing a PhD")

country = st.sidebar.selectbox("Pick a Country", ("Germany","Italy","Spain","France","Netherland","Switzerland","Belguim"))

st.markdown(custom_css, unsafe_allow_html=True)

if 'langchain_helper' in globals() and 'country' in globals():
    response = langchain_helper.get_country_and_university_name(country)
    st.header(response['country_name'].strip())

    university_names = response['university_names'].strip().split(",")
    st.subheader("List of Universities")
    
    university_list_html = "<ul>"
    for item in university_names:
        university_list_html = f"{item.strip()}" 
    university_list_html += "</ul>"
    st.markdown(university_list_html, unsafe_allow_html=True)