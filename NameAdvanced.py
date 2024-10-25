from tkinter.font import names  # Assuming you need this import for something
from typing import List
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud  # Import the wordcloud module
import statistics  # Import the statistics module for calculating median


class NameAdvanced:
    i = 0

    def letter_histogram(self, text: str):
        # Count occurrences of each letter
        letter_counts = Counter(text.lower())  # Convert to lowercase to ignore case
        # Filter out non-letter characters
        letter_counts = {k: v for k, v in letter_counts.items() if k.isalpha()}

        # Plot histogram
        plt.bar(letter_counts.keys(), letter_counts.values())
        plt.title("Letter Frequency Histogram")
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.show()

    def letter_wordcloud(self, text: str):
        # Count occurrences of each letter
        letter_counts = Counter(text.lower())
        letter_counts = {k: v for k, v in letter_counts.items() if k.isalpha()}

        # Create a new string where each letter is repeated according to its frequency
        wordcloud_input = ' '.join([k * v for k, v in letter_counts.items()])

        # Generate a word cloud based on the letter frequencies
        wordcloud = WordCloud(width=800, height=400, background_color='white',
                              collocations=False).generate(wordcloud_input)

        # Plot the letter word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")  # No axes for the word cloud
        plt.title("Letter Frequency Word Cloud")
        plt.show()

    def word_histogram(self, text: str):
        # Count occurrences of each word
        word_counts = Counter(word.lower() for word in text.split())  # Convert to lowercase and split

        # Filter out non-word characters (optional)
        word_counts = {k: v for k, v in word_counts.items() if k.isalpha()}

        # Plot histogram for words
        plt.bar(word_counts.keys(), word_counts.values())
        plt.title("Word Frequency Histogram")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
        plt.show()

    def wordcloud(self, text: str):
        # Generate a word cloud based on the word frequencies
        wordcloud = WordCloud(width=800, height=400, background_color='white',
                              collocations=False).generate(text)

        # Plot the word cloud
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")  # No axes for the word cloud
        plt.title("Word Frequency Word Cloud")
        plt.show()

    def name_length_distribution(self, text: str):
        # Extract unique names (capitalized words) using a set
        unique_names = set(word for word in text.split() if word[0].isupper() and word.isalpha())

        # Calculate the lengths of the unique names
        name_lengths = [len(name) for name in unique_names]

        # Plot the distribution of unique name lengths
        plt.hist(name_lengths, bins=range(1, max(name_lengths) + 2), alpha=0.7, color='blue', edgecolor='black')
        plt.title("Distribution of Unique Name Lengths")
        plt.xlabel("Length of Names")
        plt.ylabel("Frequency")
        plt.xticks(range(1, max(name_lengths) + 1))  # Set x-ticks to the length of names
        plt.show()

        # Calculate and print the mean and median name lengths
        mean_length = sum(name_lengths) / len(name_lengths) if name_lengths else 0
        median_length = statistics.median(name_lengths) if name_lengths else 0
        print(f"Mean Unique Name Length: {mean_length:.2f}")
        print(f"Median Unique Name Length: {median_length:.2f}")


if __name__ == "__main__":
    text = (
        "Alice Bob Charlie David Emily Frank George Hannah Ian Jack Karen Leo Mia "
        "Nina Oliver Paul Quinn Rachel Steve Tina Ulysses Victor Wendy Xander Yara "
        "Zane Anna Brian Clara Derek Eva Fiona Greg Helen Isaac Julia Kevin Laura "
        "Mark Nancy Oscar Peter Quinn Rachel Sam Tina Uma Victor Walter Xavier Yvonne "
        "Zara"
    )

    name_adv = NameAdvanced()

    # Show letter histogram
    name_adv.letter_histogram(text)

    # Show letter word cloud
    name_adv.letter_wordcloud(text)

    # Show word histogram
    name_adv.word_histogram(text)

    # Show word cloud
    name_adv.wordcloud(text)

    # Show distribution of unique name lengths
    name_adv.name_length_distribution(text)
