import streamlit as st
import pymongo

# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"

myclient = pymongo.MongoClient("mongodb+srv://mayurdabade1103:HvZ2QBn2XuQYool8@brainwave.bndu2pa.mongodb.net/")
mydb = myclient["Brainwave"]
mycol = mydb["Login_Credentials"]

def save_cred(name,mail,pwd):
    info ={"Name": name, "Mail": mail, "Password" : pwd}
    mycol.insert_one(info)


# # Insert a form in the container
# with placeholder.form("login"):
#     st.markdown("#### Enter Login credentials")
#     name = st.text_input("Enter Name")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")
#     submit = st.form_submit_button("Login")

# if submit:
#     save_cred(name,email,password)
#     placeholder.empty()
#     st.success("Login successful")
# elif submit and email != actual_email and password != actual_password:
#     st.error("Login failed")
# else:
#     pass



if __name__ == '__main__':

    
    t1,t2 = st.tabs(['Login','Register'])

    with t1:
        # Insert a form in the container
        with placeholder.form("login"):
            st.markdown("#### Enter Login credentials")
            name = st.text_input("Enter Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")

        if submit:
            save_cred(name,email,password)
            placeholder.empty()
            st.success("✔️ Login successful")
        
            # st.success("✔️ Saved successfully")

    with t2:
        print(mydb.list_collection_names())

        selected_folder = st.selectbox("Select a folder:", mydb.list_collection_names())
        selected_title = st.selectbox("Select a title:", mydb[selected_folder].distinct("Title"))
        st.write("Hello")

        if selected_title:
            # Query MongoDB collection to retrieve document based on selected title
            document = mydb[selected_folder].find_one({"Title": selected_title})

            # Display content and time_data of selected title
            if document:
                st.write("Content:", document["Content"])
                st.write("Time Date:", document["time_date"])
            else:
                st.write("No information found for selected title.")



        if submit and email == actual_email and password == actual_password:
            # If the form is submitted and the email and password are correct,
            # clear the form/container and display a success message
            placeholder.empty()
            st.success("Login successful")
        elif submit and email != actual_email and password != actual_password:
            st.error("Login failed")
        else:
            pass


