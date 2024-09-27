import streamlit as st
import pandas as pd
import os


#getting data
data_path  = "Design_Unit1_database_CSV.csv"
excel_data = pd.read_csv(data_path)

#testing functions
def testing():
    st.write("Testing")



#opening of the website
st.title(" Having trouble starting a conversation? ")
st.title(" Well, you've come to the right place!")

st.subheader(" How we can help you:")

st.markdown(" - A great way to start a conversation, especially one about difficult or uncomfortable topics, is through movies!")
st.markdown(" - So, just type in the topic you want to talk about into the input box, and we'll give you a list of movies you can watch to start the discussion.")
st.markdown(" - Just pick whichever movie you think will be best, and ask the person/people you want to talk to about the topic to watch it with you!")

st.subheader("Your Topic")


# getting input and using it to generate output

def clickedFunc():
    #clearing screen to print output at bottom of the page
    st.empty()

    #generating output
    #st.write(excel_data.loc[excel_data.Topic==option])
    # name = excel_data.loc[excel_data.Topic == option]["Name"] 
    # names_list = name.tolist()

    # year = excel_data.loc[excel_data.Topic == option]["Year"]
    # dates_list = year.tolist()

    # description = excel_data.loc[excel_data.Topic == option]["Description"]
    # desc_list = description.tolist()

    # i = 0
    # while i < len(names_list):
    #     st.write(f"- {names_list[i]} ({dates_list[i]}): {desc_list[i]}")
    #     i+=1

#getting input
option = st.selectbox(
    " ",
    ("Bullying", "Racism", "Exam Stress"),
    placeholder="Your movie topic"
)

st.button("Generate Suggestions", on_click = clickedFunc)

# """
# # My first app
# Here's our first attempt at using data to create a table:
# """

#in design doc, add final step as launching the app
