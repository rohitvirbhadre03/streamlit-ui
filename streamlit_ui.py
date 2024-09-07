import streamlit as st
import pandas as pd
import random


# Function to generate mock user profile data
def generate_mock_user_data():
    columns = ['UserID', 'FirstName', 'LastName', 'Email', 'Age', 'Country', 'SignupDate', 'LastLogin', 'IsActive', 'SubscriptionType']
    data = []
    for i in range(20):
        row = [
            i + 1,  # UserID
            ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=5)),  # FirstName
            ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=7)),  # LastName
            f'user{i}@example.com',  # Email
            random.randint(18, 60),  # Age
            random.choice(['USA', 'Canada', 'UK', 'Germany', 'France']),  # Country
            pd.Timestamp('2021-01-01') + pd.to_timedelta(random.randint(0, 1000), unit='D'),  # SignupDate
            pd.Timestamp('2023-01-01') + pd.to_timedelta(random.randint(0, 100), unit='D'),  # LastLogin
            random.choice([True, False]),  # IsActive
            random.choice(['Free', 'Basic', 'Premium'])  # SubscriptionType
        ]
        data.append(row)

    df = pd.DataFrame(data, columns=columns)
    metadata = "This is metadata for the mock user profile data."
    return 'ind', df, metadata

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a question"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Wait for it.."):
        out_type, data, metadata = generate_mock_user_data()
        st.success("Done!")

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        if out_type == 'ind':
             st.write(data)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": data})
