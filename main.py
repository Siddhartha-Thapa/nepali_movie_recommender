import pyrebase
import streamlit as st
from datetime import datetime
import datetime
import time
from google.cloud import firestore
from firebase_admin import auth

firebaseConfig = {
  'apiKey': "AIzaSyDFk5VfMxtlPlQ0aU3jR33Q5kLYw-bvfTE",
  'authDomain': "nepali-movie-recommender.firebaseapp.com",
  'projectId': "nepali-movie-recommender",
  'databaseURL': "https://nepali-movie-recommender-default-rtdb.europe-west1.firebasedatabase.app",
  'storageBucket': "nepali-movie-recommender.firebasestorage.app",
  'messagingSenderId': "299098239036",
  'appId': "1:299098239036:web:23fd8663f33cc558cfd339",
  'measurementId': "G-3DLFJCM23M"
}

def init_firestore():
    # Path to your service account key
    
    return firestore.Client.from_service_account_json(service_account_key)

#firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#database
db = init_firestore()

if "username" not in st.session_state:
    st.session_state.username = ""


def get_user_handle(email):
    # Reference the collection where user data is stored
    user_docs = db.collection('users').where('email', '==', email).get()
    
    
    for doc in user_docs:
        # Extract and return the handle
        return doc.to_dict().get('handle', 'No handle found')
def get_user_dob(email):
    # Reference the collection where user data is stored
    user_docs = db.collection('users').where('email', '==', email).get()
    
    
    for doc in user_docs:
        # Extract and return the handle
        return doc.to_dict().get('dob', 'No dob found')

page_bg_img = """
<style>
[data-testid ="stMain"]{
background-image: url("https://images.pexels.com/photos/7130555/pexels-photo-7130555.jpeg?cs=srgb&dl=pexels-codioful-7130555.jpg&fm=jpg");
background-size: cover;
}
[data-testid ="stSidebar"]{
background-image: url("https://pictureframenepal.com/wp-content/uploads/2024/08/NPL.jpg");
background-size: cover;
}
[data-testid ="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown(
    """
    <h1 style="color:black; text-align:left; font-weight:bold; background: linear-gradient(45deg, #ff9a9e, #fad0c4); display: inline-block; padding: 2px 4px; border-radius: 3px">
        Trending
    </h1>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style="font-weight:bold">
        Watch Trailer
    </div>
    """,
    unsafe_allow_html=True
)

st.video("https://www.youtube.com/watch?v=5zbtEmxEyGk")
st.video("https://www.youtube.com/watch?v=Tc0ZtDdNkX8&t=124s")
st.video("https://www.youtube.com/watch?v=2h9qtZq-hHU")
st.video("https://www.youtube.com/watch?v=lnhvA1PBtA0")
st.video("https://www.youtube.com/watch?v=5JMcucWbNxs")
st.video("https://www.youtube.com/watch?v=xwjbSOo6Wsg")
st.video("https://www.youtube.com/watch?v=6oEghnv7hpk")
st.video("https://www.youtube.com/watch?v=osXBtY2SwyQ")
st.video("https://www.youtube.com/watch?v=HPGOQhguvJo")
more = st.button("Recommend More")
if more:
    st.video("https://www.youtube.com/watch?v=0tx6eeW0NiQ")
    st.video("https://www.youtube.com/watch?v=rzUboQGZU-o")
    st.video("https://www.youtube.com/watch?v=e29qr_lr_eI")
    st.video("https://www.youtube.com/watch?v=q42GwbiUol8")
    st.video("https://www.youtube.com/watch?v=jcO53FtHCI0")
    st.video("https://www.youtube.com/watch?v=SXMcWzNErfk")
    st.video("https://www.youtube.com/watch?v=CRbG8XBkZkE")
    st.video("https://www.youtube.com/watch?v=-eweJ6K-8RI")
st.markdown(
    """
    <h3 style="color:black; text-align:left; font-weight:bold; background: linear-gradient(45deg, #ff9a9e, #fad0c4); display: inline-block; padding: 2px 4px; border-radius: 15px">
        Sign in 
    </h3>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <h3 style="color:black; font-weight:bold; background-color:#8ef;display: inline-block; padding: 2px 4px; border-radius: 3px">
         for more recommendations
    </h3>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <style>
    .sidebar-title1 {
        font-size: 25px;
        color: black;
        font-weight: bold;
        text-align: left;
        background-color:#8ef;
        display: inline-block; padding: 2px 4px; border-radius: 6px;    
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .sidebar-title2 {
        font-size: 25px;
        color: #8ef;
        font-weight: bold;
        text-align: left;
        background-color:black;
        display: inline-block; padding: 2px 4px; border-radius: 6px;    
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .sidebar-success {
        font-size: 20px;
        color: black;
        text-align: left;
        background: linear-gradient(45deg, #ff9a9e, #fad0c4);
        display: inline-block; padding: 2px 4px; border-radius: 6px;    
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .sidebar-exist {
        font-size: 20px;
        color: black;
        text-align: left;
        background: linear-gradient(45deg, #ff9a9e, #fad0c4);
        display: inline-block; padding: 2px 4px; border-radius: 6px;    
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .sidebar-welcome {
        font-size: 40px;
        color: black;
        font-weight: bold;
        text-align: left;
        background-color: white; 
        display: inline-block; padding: 2px 4px; border-radius: 6px;    
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .sidebar-info {
        font-size: 15px;
        color: yellow;
        text-align: left;
        background-color:black;
        display: inline-block; padding: 2px 4px; border-radius: 6px;    
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.sidebar.markdown('<div class="sidebar-title1">Nepali</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-title2">Movie Recommeneder</div>', unsafe_allow_html=True)


#authentication
choice = st.sidebar.selectbox('Login/Signup',['Login','Sign up'])
email = st.sidebar.text_input('Please enter your email address',placeholder="enter your email here")
if email:
    st.session_state.user_email = email

password = st.sidebar.text_input('please enter your password',type='password',placeholder='your password')
if password:
    st.session_state.user_password = password

if choice == 'Sign up':
  
    if "user_handle" not in st.session_state:
        st.session_state.user_handle = ""
    
    dob = st.sidebar.date_input(
        "please enter your date of birth",  # Default date
        min_value=datetime.date(1950, 1, 1),  # Minimum selectable date
        max_value=datetime.date(2030,1,1),
        ) 
    if dob:
        st.session_state.user_dob = dob
    handle = st.sidebar.text_input('Please input your app handle name',st.session_state.user_handle,placeholder="Enter your Handle name")
    if handle:
        st.session_state.user_handle = handle
        
    submit = st.sidebar.button('Create My Account')
    if submit:
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age >= 18:
            user = auth.create_user_with_email_and_password(email,password)
            st.sidebar.markdown('<div class="sidebar-success">your account is created successfully!</div>', unsafe_allow_html=True)
            st.balloons()
            username = user
            st.session_state.username = user
            user = auth.sign_in_with_email_and_password(email,password)
            st.sidebar.page_link("pages\Home.py")
        else:
           st.sidebar.markdown('<div class="sidebar-success">You must be atleast 18 years to sign up!!!</div>', unsafe_allow_html=True)
    #sign in 
        
     
if choice == 'Login':
  login = st.sidebar.button('Login')
  if login:
    user = auth.sign_in_with_email_and_password(email,password)
    username = user
    st.session_state.username = user
    handle = get_user_handle(email)
    st.write(handle)
    st.session_state.user_handle = handle
    dob = get_user_dob(email)
    st.write(dob)
    st.session_state.user_dob = dob
    st.sidebar.markdown('<div class="sidebar-info">Logged in successfully!</div>', unsafe_allow_html=True)
    st.sidebar.page_link("pages\Home.py")
   
    

