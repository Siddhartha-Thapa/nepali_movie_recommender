# Nepali Movie Recommender

A web application for recommending Nepali movies, built with [Streamlit](https://streamlit.io/) for the backend and custom frontend components. The app supports user authentication, personalized recommendations, history tracking, genre-based suggestions, and a social feed for sharing posts.

---

## Features

- **User Authentication:** Sign up and login using email, password, and handle. Age verification is enforced.
- **Movie Recommendation:** Get personalized movie recommendations based on similarity models.
- **Genre-Based Suggestions:** Browse movies by genre and view posters.
- **Recommendation History:** See your past recommendations and posters.
- **Social Feed:** Share your recommendations as posts and view posts from other users.
- **Custom UI:** Styled with Bootstrap and custom CSS for a modern look.
- **Streamlit Components:** Includes a Svelte-based image carousel component for enhanced UI.

---


## Backend (Streamlit)

- **Main Files:**  
  - [`main.py`](main.py): Main entry point, handles authentication, UI, and recommendations.
  - [`pages/Home.py`](pages/Home.py): Main dashboard after login, handles recommendations, history, posts, and feed.

- **Data Files:**  
  - `movies_list2.pkl`: Movie datasets.
  - `similarity2.pkl`: Precomputed similarity matrices.
  - `Nepali_Movies_Dataset.xlsx`: Source dataset.

## Frontend (Streamlit components)
- **Styling:**  
  - [`style.css`](style.css): Custom CSS for Streamlit UI.

---
## Database
-Used Firebase for more efficient and easy haldling.

## Setup & Installation

### 1. Python Environment

- Install required Python packages:
  ```sh
  pip install streamlit pyrebase firebase-admin pandas google-cloud-firestore
  ```

- Place your Firebase service account JSON (`nepali-movie-recommender-firebase-adminsdk-pl76i-f9b872abb7.json`) in the project root.

### 2. Running the App

- Start the Streamlit app:
  ```sh
  streamlit run main.py
  ```
 
- The app will be available at [localhost:8501](http://localhost:8501).

---

## Usage

1. **Sign Up:**  
   - Enter your email, password, handle, and date of birth (must be 18+).
2. **Login:**  
   - Enter your credentials to access recommendations.
3. **Get Recommendations:**  
   - Select a movie to get similar recommendations.
   - Browse by genre or search for movies.
4. **History & Feed:**  
   - View your recommendation history.
   - Share posts and see posts from other users.

---

## Customization

- **Styling:**  
  Modify [`style.css`](style.css) for custom UI changes.
- **Frontend Components:**  
  Add or edit Svelte components in [`frontend/src`](frontend/src).
- **Data:**  
  Update or replace movie datasets (`.pkl`, `.xlsx`) as needed.

---

## License

- Bootstrap is MIT licensed.
- Other code is provided for educational purposes.

---

## Credits

- Nepali movie dataset and recommendations logic by me and my project team.


## Screenshots
/demo1.png
/demo2.png


## Troubleshooting

- Ensure all `.pkl` and `.json` files are present.
- If you encounter authentication issues, check your Firebase credentials and service account file.
- For frontend issues, rebuild with `npm run build`.

---

## Contributing

Pull requests and suggestions are welcome!
