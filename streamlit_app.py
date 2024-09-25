import streamlit as st
import pandas as pd
import os


#getting data
data_path  = "Design_Unit1_database_CSV.csv"
excel_data = pd.read_csv(data_path)

st.write(excel_data.head())

st.title(" Having trouble starting a conversation? ")
st.title(" Well, you've come to the right place!")

st.subheader(" How we can help you:")

st.markdown(" - A great way to start a conversation, especially one about difficult or uncomfortable topics, is through movies!")
st.markdown(" - So, just type in the topic you want to talk about into the input box, and we'll give you a list of movies you can watch to start the discussion.")
st.markdown(" - Just pick whichever movie you think will be best, and ask the person/people you want to talk to about the topic to watch it with you!")

st.subheader("Your Topic")


def clickedFunc():
    #the everything
    print("just for now, delete later")

option = st.selectbox(
    " ",
    ("Email", "Home phone", "Mobile phone"),
    placeholder="Your movie topic"
)


st.button("Generate Suggestions", on_click = clickedFunc)

# """
# # My first app
# Here's our first attempt at using data to create a table:
# """
