import csv
import math

def main():
    print("Welcome to the DMB Song Probability Calculator!")
    inquire()

def inquire():
    song = input("Enter your favorite song: ").strip()
    venue = input("(Optional) Enter a venue: ").strip()
    if not song:
        print("You must enter a song name.")
        return
    analysis(song, venue)

def analysis(song, venue):
    csv_file = "fake_shows.csv"

    # Read all shows into a list
    with open(csv_file, newline="") as f:
        reader = csv.DictReader(f)
        shows = list(reader)

    # Filter by venue if provided
    if venue:
        potential_shows = [row for row in shows if row['venue'].lower() == venue.lower()]
    else:
        potential_shows = shows

    total = len(potential_shows)
    if total == 0:
        print(f"No shows found for {venue}." if venue else "No shows found in the dataset.")
        return

    # Count how many times the song was played
    count = sum(1 for row in potential_shows if row['song'].lower() == song.lower())

    if count == 0:
        print(f"{song} has never been played at {venue}." if venue else f"{song} has never been played at any venue.")
        return

    # Probability calculations
    probability = count / total
    to_hear = 1 / probability
    want50 = math.log(0.5) / math.log(1 - probability)

    print(f"\nResults for '{song}':")
    print(f"At {venue if venue else 'all venues'}, this song will appear approximately once every {to_hear:.2f} shows.")
    print(f"For a 50% chance of hearing it at a show, attend about {want50:.2f} shows at this venue.\n")

    # Ask if the user wants to try another query
    another = input("Would you like to check another song? (y/n): ").strip().lower()
    if another == 'y':
        inquire()
    else:
        print("Thanks for using the DMB Song Probability Calculator!")

if __name__ == "__main__":
    main()