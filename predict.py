import csv
import pandas as pd
from datetime import datetime
from collections import defaultdict

def get_show_count(data):
    return data['date'].nunique()

def get_counts(data):
    shows = data['song'].tolist()
    song_show_count = {}
    for show in shows:
        check = show.strip().lower()
        if check not in song_show_count:
            song_show_count[check] = 1
        else:
            song_show_count[check] += 1
    return song_show_count

def get_prob(show_num, freq):
    return float(freq / show_num)
    
def main():
    data = pd.read_csv("sample_shows.csv")

    show_num = get_show_count(data)
    song_counts = get_counts(data)

    while True:
        request = input("What song do you want to hear at the next show? ")
        cont = False
        if request.strip().lower() not in song_counts:
            want_to_cont = ""
            while want_to_cont != "Y" and want_to_cont != "N":
                want_to_cont = input("Sorry, that song is not in the database. Try another song! (Y/N) ")
            if want_to_cont == "Y":
                cont = True
        else:
            prob = get_prob(show_num, song_counts[request.strip().lower()])
            want_to_cont = ""
            while want_to_cont != "Y" and want_to_cont != "N":
                want_to_cont = input(f"You have a {prob*100}% chance of hearing {request} at the next show! Try another song? (Y/N) ")
            if want_to_cont == "Y":
                cont = True
        if (not cont):
            break


if __name__ == "__main__":
    main()