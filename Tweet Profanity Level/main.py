import nltk
import pandas as pd
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer


def calculate_profanity(tweet: str, profanity_list: list) -> int:
    """
    Calculate the degree of profanity in a tweet by counting the number of
    profanity words.

    Args:
        tweet (str): A string representing the tweet.
        profanity_list (list): A list of words considered as profanity.

    Returns:
        int: Degree of profanity.
    """
    profanity_count = 0
    tweet = tweet.replace('#', '')
    words = tweet.split()
    lemmatizer = WordNetLemmatizer()
    for word in words:
        lemma = lemmatizer.lemmatize(word)
        if lemma in profanity_list:
            profanity_count += 1
    return profanity_count


def main():
    profanity_list = list(pd.read_csv("Tweet Profanity Level\profanity.csv")['Profanity'])
    tweets = list(pd.read_csv("Tweet Profanity Level\\tweets.csv")['tweet'])
    for tweet in tweets:
        profanity_degree = calculate_profanity(tweet, profanity_list)
        print(f"Tweet: '{tweet}'\nProfanity degree: {profanity_degree}")


if __name__ == "__main__":
    main()
