import streamlit as st
import pandas as pd
from predict import get_prob, get_global_mean_play_rate

st.header("WHAT WOULD THEY PLAY?")
st.subheader("Type in your favorite Dave Matthews Band song, get the probability of it playing at the next show!")
st.markdown("Data routinely sourced from DMBAlmanac.")
st.divider()

@st.cache_data
def load_and_prep_data():
    df = pd.read_csv("allshows.csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%m.%d.%Y").dt.date
    df["Song"] = df["Song"].str.lower()
    mean_rate = get_global_mean_play_rate(df)
    return df, mean_rate, df['Song'].unique()

data, global_mean_rate, valid_songs = load_and_prep_data()

song = st.text_input("Your favorite DMB song: ")

button_clicked = st.button("Give me the numbers!")

if button_clicked:
    clean_song = song.strip().lower()
    
    if clean_song not in valid_songs:
        st.error("Sorry, that song is not in the database. Try another song!")
    else:
        prob = get_prob(data, clean_song, global_mean_rate)
        
        prob_percent = f"{prob * 100:.2f}"
        
        st.success(f"The probability of hearing **{song}** at the next DMB show is **{prob_percent}%**!")
        st.markdown("Type in another song to get another probability!")