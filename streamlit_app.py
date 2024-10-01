import streamlit as st
import pandas as pd


#getting data
data_path  = "Design_Unit1_database_CSV.csv"
excel_data = pd.read_csv(data_path)
    # a CSV file was used to avoid bugs
    #an excel file needs pip to install openpyxl, which resulted in an error

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
    
    st.write("Here are some suggestions for you:")

    #generating output
       
    name = excel_data.loc[excel_data.Topic == option]["Name"] 
    names_list = name.tolist()

    year = excel_data.loc[excel_data.Topic == option]["Year"]
    dates_list = year.tolist()

    description = excel_data.loc[excel_data.Topic == option]["Description"]
    desc_list = description.tolist()

    #printing output

    i = 0
    while i < len(names_list):
        st.write(f"- {names_list[i]} ({dates_list[i]}): {desc_list[i]}")
        i+=1


#getting input
option = st.selectbox(
    " ",
    ("Bullying", "Racism", "Exam Stress"),
    placeholder="Your movie topic"
)

#st.button("Gen", on_click = clickedFunc)
    #using the above code results in the output being printed at the top of the page 
    #thus, the below piece of code is used
if st.button("Generate Suggestions"):
    clickedFunc()


# """
# # My first app
# Here's our first attempt at using data to create a table:
# """

#in design doc, add final step as launching the app
