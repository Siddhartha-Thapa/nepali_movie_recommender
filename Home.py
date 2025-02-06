from google.cloud import firestore
import streamlit as st
import time
import pickle
import random
import datetime
import pandas as pd
import firebase_admin
from firebase_admin import auth
import pyrebase
from firebase_admin import credentials, firestore
from firebase_admin import auth, credentials
import firebase_admin
from datetime import datetime


# Initialize Firestore (using the same function from main.py)
def init_firestore():
   
    return firestore.Client.from_service_account_json(service_account_key)
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

db = init_firestore()  # Initialize Firestore client


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db1 = firebase.database()
def is_authenticated():
    return st.session_state.get("authenticated", False)

def update_user_password(uid, new_password):
    try:
        # Update the password
        auth.update_user(uid, password=new_password)
        st.sidebar.success("Password updated successfully!")
    except Exception as e:
        st.sidebar.error(f"Error updating password: {str(e)}")
if "username" not in st.session_state or not st.session_state.username:
    st.warning("You must log in first.")
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
    st.sidebar.markdown('<div class="sidebar-title1">Nepali</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="sidebar-title2">Movie Recommeneder</div>', unsafe_allow_html=True)
    st.sidebar.video("https://www.youtube.com/watch?v=5zbtEmxEyGk")
    st.sidebar.video("https://www.youtube.com/watch?v=Tc0ZtDdNkX8&t=124s")
    st.sidebar.video("https://www.youtube.com/watch?v=2h9qtZq-hHU")
    st.sidebar.video("https://www.youtube.com/watch?v=lnhvA1PBtA0")
    st.sidebar.video("https://www.youtube.com/watch?v=5JMcucWbNxs")
    st.sidebar.video("https://www.youtube.com/watch?v=xwjbSOo6Wsg")
    st.sidebar.video("https://www.youtube.com/watch?v=6oEghnv7hpk")
    st.sidebar.video("https://www.youtube.com/watch?v=osXBtY2SwyQ")
    st.sidebar.video("https://www.youtube.com/watch?v=HPGOQhguvJo")
    more = st.sidebar.button("Recommend More")
    if more:
        st.sidebar.video("https://www.youtube.com/watch?v=0tx6eeW0NiQ")
        st.sidebar.video("https://www.youtube.com/watch?v=rzUboQGZU-o")
        st.sidebar.video("https://www.youtube.com/watch?v=e29qr_lr_eI")
        st.sidebar.video("https://www.youtube.com/watch?v=q42GwbiUol8")
        st.sidebar.video("https://www.youtube.com/watch?v=jcO53FtHCI0")
        st.sidebar.video("https://www.youtube.com/watch?v=SXMcWzNErfk")
        st.sidebar.video("https://www.youtube.com/watch?v=CRbG8XBkZkE")
else:
    
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
    .Pass {
        font-size: 15px;
        color: black;
        font-weight: bold;
        text-align: left;
        background-color:white;
        display: inline-block; padding: 2px 4px; border-radius: 6px;margin-top:50px;margin-bottom:0px;    
    }
    </style>
    """,
        unsafe_allow_html=True,
        )
        st.markdown(
    """
    <style>
    .sidebar-profile-container {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-top: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .sidebar-profile-info {
        font-size: 15px;
        color: black;
        font-weight: bold;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
        st.markdown("""
    <style>
    .stRadio > div {
        display: flex;
        flex-direction: row;
    }
    </style>
    """, unsafe_allow_html=True)

        st.sidebar.markdown('<div class="sidebar-title1">Nepali</div>', unsafe_allow_html=True)
        st.sidebar.markdown('<div class="sidebar-title2">Movie Recommeneder</div>', unsafe_allow_html=True)
        
        
    
        
        def get_all_posts(email):
    # Reference the collection where user data is stored
            user_docs = db.collection('users').where('email', '==', email).get()
    
    
            for doc in user_docs:
        # Extract and return the posts
                return doc.to_dict().get('posts')
    # Ensure Firestore user reference exists
        user = st.session_state.username
        user_id = user['localId']  # Extract the unique user ID from Firebase
        user_doc_ref = db.collection("users").document(user_id)

    # Fetch user info for personalized messages
        handle = st.session_state.get("user_handle", None)
        dob = st.session_state.get("user_dob")
        email = st.session_state.get("user_email")
        password = st.session_state.get("user_password")
        if "init_message_shown" not in st.session_state:
                st.session_state.init_message_shown = True
                placeholder = st.empty()
                placeholder.success(f"Welcome, {handle}! Enjoy surfing")
                time.sleep(5)
                placeholder.empty()
       
        if st.sidebar.button("Profile"):
           
            st.sidebar.markdown('<div class="sidebar-title1">My Profile</div>', unsafe_allow_html=True)
            st.sidebar.image("default-profile-account-unknown-icon-black-silhouette-free-vector.jpg", width=100)
            st.sidebar.markdown(f'<div class="sidebar-title2">{handle}</div>', unsafe_allow_html=True)   
            st.sidebar.markdown(
            f"""
            <div class="sidebar-profile-container">
            <div class="sidebar-profile-info">Date of Birth: {dob}</div>
            <div class="sidebar-profile-info">Email: {email}</div>
            
            </div>
            """,
            unsafe_allow_html=True,
            )

            st.sidebar.markdown('<div class="Pass">Password:</div>', unsafe_allow_html=True)
            st.sidebar.text_input(label="", type='password', value = password)
                    






    # Load movie data and similarity model
        movies = pickle.load(open("movies_list2.pkl", 'rb'))
        similarity = pickle.load(open("similarity2.pkl", 'rb'))
        movies_list = movies['title'].values
        st.header("Nepali Movie Recommender")
    # Movie selection dropdown
        selectvalue = st.selectbox("Select movie from dropdown", movies_list)
        default_poster = "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie.jpg"
    # Recommendation function
        def recommend(movie):
                index = movies[movies['title']==movie].index[0]
                distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
                recommend_movie=[]
                recommend_poster=[]
                for i in distance[1:6]:
                        recommend_movie.append(movies.iloc[i[0]].title) 
                        poster_link= movies.iloc[i[0]].poster
                        if pd.isna(poster_link) or poster_link is None or not isinstance(poster_link, str):
                                recommend_poster.append(default_poster)  # Use placeholder image if missing or invalid
                        else:
            # Ensure the link points to a valid image URL (optional check)
                                if not poster_link.lower().startswith(('http://', 'https://')): 
                                        recommend_poster.append(default_poster)  # Use placeholder image if not a valid URL
                                else:
                                        recommend_poster.append(poster_link)

                return recommend_movie, recommend_poster


        if st.button("Show recommend"):
                movie_name , movie_poster = recommend(selectvalue)
                col1,col2,col3,col4,col5 = st.columns(5)
                with col1:

                        st.text(movie_name[0])
                        st.image(movie_poster[0], use_container_width=True)
                with col2:
                        st.text(movie_name[1])
                        st.image(movie_poster[1], use_container_width=True)
                with col3:
                         st.text(movie_name[2])
                         st.image(movie_poster[2], use_container_width=True)
                with col4:
                        st.text(movie_name[3])
                        st.image(movie_poster[3], use_container_width=True)
                with col5:
                        st.text(movie_name[4])
                        st.image(movie_poster[4], use_container_width=True)

       
        # Save recommendations to Firestore
                user_data = user_doc_ref.get().to_dict()

                if user_data:
            # Update recommendations if user data exists
                        user_doc_ref.update({
                        "recommendations": firestore.ArrayUnion([{
                        "selected_movie": selectvalue,
                        "recommendations": movie_name,
                        "posters": movie_poster,
                    
                        }])
                                })
                else:
            # Create new document if user data doesn't exist
                        user_doc_ref.set({
                        "email": user['email'],
                        "handle": handle,
                        "dob":str(dob),
                        "recommendations": [{
                        "selected_movie": selectvalue,
                        "recommendations": movie_name,
                        "posters": movie_poster,
                    
                        }]
                 })

                st.success("Recommendations saved successfully!")
        with st.expander("Your History-Based Recommendations"):
            user_data = user_doc_ref.get().to_dict()

            if user_data and "recommendations" in user_data:
    # Collect all past recommendations and posters
                recommendations = []
                posters = []
                for record in user_data["recommendations"]:
                        recommendations.extend(record["recommendations"])
                        posters.extend(record["posters"])
    # Ensure unique recommendations and posters
                unique_recommendations = list(set(zip(recommendations, posters)))
    # Select 5-10 random unique recommendations
                if len(unique_recommendations) > 20:
                        history_recommendations = random.sample(unique_recommendations, 20)
                else:
                        history_recommendations = unique_recommendations

                st.write("Based on your past recommendations, we suggest these movies:")
                cols = st.columns(5)  # Create 5 columns

                for i, (movie, poster) in enumerate(history_recommendations):
                        col = cols[i % 5]  # Distribute movies across columns
                        with col:
                                st.text(movie)
                                st.image(poster if poster else default_poster, use_container_width=True)
     
            else:
                st.info("No history found. Start exploring movies to build your recommendation history!")
        with st.expander("Get recommendations according to the genre"):
        # Load the dataset
            movies_df = pd.read_pickle("movies_list2.pkl")  # Update the file path if needed

            movies_df['poster'] = movies_df['poster'].fillna(default_poster)
            movies_df['genre'] = movies_df['genre'].str.lower().fillna("unknown")
# Get unique genres for the radio options
            genres = movies_df['genre'].unique()
            genres = [genre.capitalize() for genre in genres] 
            selected_genre = st.radio("select genre:", options=['comedy','drama','romance','action','documentary','family'],key = None,)

        # Filter movies by selected genre
            filtered_movies = movies_df[movies_df['genre'].str.contains(selected_genre.lower(), na=False)]

            st.write(f"Movies under genre: **{selected_genre}**")

# Display the movie titles and posters
            for i in range(0, len(filtered_movies), 5):
                row = filtered_movies.iloc[i:i+5]
                cols = st.columns(5)
    
                for col, (_, movie) in zip(cols, row.iterrows()):
                    with col:
                        st.image(movie['poster'], caption=movie['title'], use_container_width=True)


        with st.expander(" My Posts"):
                  
            col1,col2 = st.columns(2)
            with col1:
                    st.markdown(f'<div class="sidebar-title2">{handle}</div>', unsafe_allow_html=True) 
                    post = st.text_input("Share my recommendations as a post!!",max_chars=200)
                    add_post = st.button("Share post")
                    if add_post:
                          now = datetime.now()
                          dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
                          st.session_state.dt_string = dt_string
                          post = {
                                    post }
                          dt = {dt_string}
                          # Save posts to Firestore
                          user_data = user_doc_ref.get().to_dict()

                          if user_data:
            # Update recommendations if user data exists
                            user_doc_ref.update({
                        "posts": firestore.ArrayUnion([{
                        
                        "posts": post,
                    
                                        }])
                                })
                            user_doc_ref.update({
                        "dt": firestore.ArrayUnion([{
                        
                        "dt": dt,
                    
                                        }])
                                })
                          else:
            # Create new document if user data doesn't exist
                            user_doc_ref.set({
                                    "posts": post
                    
                       
                                    })
                            user_doc_ref.set({
                                    "dt": dt
                    
                       
                                    })
                            st.balloons()
            with col2:
                  all_posts = get_all_posts(email)
                  if all_posts is not None:
                     for post in reversed(all_posts):
                           st.code(post ,language='') 
                   
        with st.expander("Feed"):
            
            
            def get_all_user_posts():
                users_ref = db.collection("users")
                docs = users_ref.stream()
    
                posts_list = []

                for doc in docs:
                    user_data = doc.to_dict()
                    user_handle = user_data.get("handle", "Unknown Handle")
                    posts_data = user_data.get("posts", [])
                    posts_dt = user_data.get("dt",[])

        # Extract posts for each user
                    for post_group in posts_data:
                        if isinstance(post_group, dict) and "posts" in post_group:
                            post_entries = post_group["posts"]
                        for post_group1 in posts_dt:
                            if isinstance(post_group1, dict) and "dt" in post_group1:
                                post_entries1 = post_group1["dt"]
                # Ensure we have a valid list for each post
                        if isinstance(post_entries, list) and len(post_entries) == 1 and isinstance(post_entries1,list) and len(post_entries1) == 1:
                                
                               
                                    post_time = post_entries1[0]
                                    post_content = post_entries[0]
                                    posts_list.append(f"{post_content}")
                                    posts_list.append(f"{user_handle}_____________________________{post_time}")
                                    posts_list.append("")

                return posts_list

            
            posts = get_all_user_posts()
            if posts:
                for post in reversed(posts):
                    st.write(post)
            else:
                st.write("No posts found.")
        logout_url = "/"  # Redirect to the main entry point
        st.markdown(f'<a href="{logout_url}" target="_self"><button>Logout</button></a>', unsafe_allow_html=True)

        movies_df1 = pd.read_pickle("movies_list2.pkl")  # Update the file path if needed
        default_poster = "https://motivatevalmorgan.com/wp-content/uploads/2016/06/default-movie.jpg"
        movies_df1['poster'] = movies_df1['poster'].fillna(default_poster)
        movies_df1['genre'] = movies_df1['genre'].str.lower().fillna("unknown")
# Get unique genres for the radio options
        genres = movies_df1['genre'].unique()
        genres = [genre.capitalize() for genre in genres]     
        search_query = st.text_input("Search for a movie:")
        
# Filter movies based on the search query
        if search_query:
            filtered_movies = movies_df1[movies_df1['tags'].str.contains(search_query, case=False, na=False)]
            st.write(f"Search results for: **{search_query}**")
        else:
              st.write("explore movies:")
              filtered_movies = movies_df1
              

        

# Display movies in rows with 5 columns per row
        for i in range(0, len(filtered_movies), 5):
                row = filtered_movies.iloc[i:i+5]
                cols = st.columns(5)
    
                for col, (_, movie) in zip(cols, row.iterrows()):
                    with col:
                        st.image(movie['poster'], caption=movie['title'], use_container_width=True)  
