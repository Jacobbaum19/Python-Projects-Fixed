import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv

load_dotenv("env.txt")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URL = os.getenv("REDIRECT_URL")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    redirect_uri=REDIRECT_URL,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    scope="playlist-modify-private",
    cache_path="tokens.txt",
    )
)

user_id = sp.current_user()["id"]

# ISSUE WITH SCRIPT: COULDN'T SOLVE 401 TOKEN ERROR...

#------------------------ Get Billboard Data ------------------------#


def get_billboard_data(date_str):
    """
    Retrieves the Billboard Hot 100 chart data for the given date.

    Args:
        date_str (str): The date in the format "YYYY-MM-DD".

    Returns:
        list: A list of song titles from the Billboard Hot 100 chart for the given date.
    """
    try:
        billboard_request = requests.get(f"https://www.billboard.com/charts/hot-100/{date_str}")
        if billboard_request.status_code == 200:
            soup = BeautifulSoup(billboard_request.content, "html.parser")

            # Making a list of song titles and artist_names using list compensation
            song_titles = [title.get_text(strip=True) for title in soup.select("li ul li h3")]
            return song_titles
        else:
            print(f"Error: Billboard API request failed with status code {billboard_request.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

#------------------------ Load Cached Data ------------------------#


def load_cached_token():
    """Was trying to check if my token was working... It still isn't. Unfortunately I give up on this app.
    I'll possibly come back to this project, I have to move on for now."""
    try:
        with open("tokens.txt", "r") as f:
            cached_data = json.load(f)
            access_token = cached_data["access_token"]
            return access_token
    except (FileNotFoundError, json.JSONDecodeError):
        return None


#------------------------ Main Script ------------------------#
def main():
    user_input_date = input("What year do you want to travel to in music?\nPlease type in this format, 'YYYY-MM-DD'\n")
    # Checks to see if the day consist of 10 characters.
    if len(user_input_date) == 10:
        song_titles = get_billboard_data(user_input_date)
        year = user_input_date.split("-")[0]

        # Check to see if you have access token loaded.
        access_token = load_cached_token()
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            # Searches for the song by song and year.
            for song in song_titles:
                result = sp.search(q=f"track:{song} year:{year}", type="track")
                print(result)
        else:
            print("No cached token found. Please run the authentication flow first.")
    else:
        print("Invalid date format. Please try again.")


if __name__ == "__main__":
    main()
