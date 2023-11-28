import streamlit as st
import pandas as pd
import hashlib
tokenn=None	
ACCOUNT_CSV_PATH = 'account/account.csv'
def check_credentials(email, password):
    account_data = pd.read_csv(ACCOUNT_CSV_PATH)
    if email in account_data['email'].values:
        stored_hash = account_data.loc[account_data['email'] == email, 'hash_code'].values[0]
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == stored_hash:
            return True
    return False

def register_user(email, password, token):
    account_data = pd.read_csv(ACCOUNT_CSV_PATH)
    if email in account_data['email'].values:
        st.error('This email is already registered. Please use a different email.')
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        new_data = pd.DataFrame({'email': [email], 'hash_code': [hashed_password], 'token': [token]})
        with open(ACCOUNT_CSV_PATH, 'a') as file:
            new_data.to_csv(file, header=False, index=False)
        st.success('Registration successful! Please login.')

def mainn():
        st.title('Gmail Login')

        email = st.text_input('Enter your email:')
        password = st.text_input('Enter your password:', type='password')
        token = st.text_input('Enter your token:')

        register = st.button('Register')
        login = st.button('Login')
        if register:
            if email and password and token:
                register_user(email, password, token)
            else:
                st.error('All fields are required for registration.')

        if login:
            if email and password:
                if check_credentials(email, password):
                    st.success('Login successful!')
                    account_data = pd.read_csv(ACCOUNT_CSV_PATH)
                    f=open('gmail_current.txt','w')
                    f.write(email)
                    f.close()
                    token = account_data.loc[account_data['email'] == email, 'token'].values[0]
                    return token

                else:
                    st.error('Invalid credentials. Please try again.')
if __name__ == '__main__':
    mainn()
