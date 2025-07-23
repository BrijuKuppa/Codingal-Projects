import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

# Initialize colorama
init(autoreset=True)

# Load and preprocess the dataset
def load_data(file_path='imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()

# Vectorize the combined features and compute cosine similarity
tfidf = TfidfVectorizer(stop_words = "english")
tfidf_meterics = tfidf.fit_transform(movies_df["combined_features"])
cosin_sim = cosine_similarity(tfidf_meterics, tfidf_meterics)

# List all unique genres
def list_genre(df):
    return sorted(set(genre.strip() for sub_list in df["Genre"].dropna().str.split(",") for genre in sub_list))

genres = list_genre(movies_df)

# Recommend movies based on filters (genre, mood, rating)
def recommend_movies(genre=None, mood=None, rating=None, top_n=None):
    filtered_df = movies_df

    if genre:
        filtered_df = filtered_df[filtered_df["Genre"].str.contains(genre, case=False, na=False)]
        
    if rating:
        filtered_df = filtered_df[filtered_df["IMDB_Rating"] >= rating]

    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)

    recommendations = []
    
    for idx, row in filtered_df.iterrows():
        overview = row["Overview"]
        if pd.isna(overview):
            continue
        polarity = TextBlob(overview).sentiment.polarity
    
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row["Series_Title"], polarity))

        if len(recommendations) == top_n:
            break

    return recommendations if recommendations else "No suitable recommendations found."

# Display recommendations🍿 😊  😞  🎥
def display_recommednations(recs, name):
    print(Fore.YELLOW + f"\n🍿 Here are some recommedations for you, {name}:")

    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive 😀" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
        print(f"{Fore.CYAN}{idx}. 🎥 {title} (Polarity: {polarity:.2f}, {sentiment})")

# Small processing animation
def processing_animation():
    
    for _ in range(10):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Handle AI recommendation flow 🔍
def handle_ai(name):
    print(Fore.BLUE + f"\n🔍 Lets start finding the perfect movie just for you, {name}!\n")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")

    while True:
        genre_input = input(Fore.GREEN + "Choose a genre: ")
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input)-1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(f"{Fore.RED}Please enter a valid input without spaces and underscores. You can enter the genre number or name.")

    mood = input(Fore.CYAN + "Great! Now, type something that reprents the general mood you would like your movie to be in. ").strip()

    # Processing animation while analyzing mood 😊  😞  😐
    print(Fore.YELLOW + "\nThinking", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive 😊" if polarity > 0 else "negative 😞" if polarity < 0 else "neutral 😐"
    print(f"{Fore.BLUE}\nAfter looking at your response, it looks like you would want a {mood_desc} feeling movie.")
    print(f"{Fore.YELLOW}Advanced info: Polarity is {polarity:.2f}.\n")

    while True:
        rating_input = input(Fore.GREEN + "Now, you have to decide your IMBd-rating (7.6 - 9.3). Or, you can skip this by typing 'skip': ")

        if rating_input == "skip":
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Your input is not in the range.")
        except ValueError:
            print(Fore.RED + "Your input is not valid.")

    # Processing animation while finding movies
    print(f"Finding movies just for you, {name}", end="")
    processing_animation() # Small processing animation while finding movies 🎬🍿
    
    recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        display_recommednations(recs, name)
    
    while True:
        action = input(Fore.LIGHTYELLOW_EX + "\nDo you want more movies to watch?").strip().lower()

        if action == "no":
            print(f"Okay, enjoy your movie, {name}!")
            break
        elif action == "yes":
            recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
            if isinstance(recs, str):
                print(Fore.RED + recs + "/n")
            display_recommednations(recs, name)
        else:
            print(Fore.RED + "I do not understand, please try again.\n")
        
# Main program 🎥
def main():
    print(f"{Fore.GREEN}\nWelcome, User! I am here to recommend movies for you! 🎥")
    name = input(f"{Fore.CYAN}\nFirst, lets introduce ourselves. I am Movie Recommender! How about you? ").strip()
    print(f"{Fore.LIGHTYELLOW_EX}Okay, {name}. I am going to need you to answer a few questions before I recommend movies for you.")

    handle_ai(name)

if __name__ == "__main__":
    main()