"""A basic Flask application to show the general framework."""
from flask import Flask, render_template, jsonify
import csv
import random

app = Flask(__name__)
@app.route('/', methods=['GET'])
def generate_predictions():
    # Load data from CSV file
    with open('.\example.csv', 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Flatten data into a single list of words
    words = [word.lower() for row in data for word in row]

    # Generate random starting word
    current_word = random.choice(words)

    # Initialize list to store predicted words
    predicted_words = []

    # Set maximum number of words to predict
    max_predictions = 6

    # Loop until we have generated the desired number of predicted words
    while len(predicted_words) < max_predictions:

        # Find all occurrences of the current word in the data
        matches = [i for i, word in enumerate(words) if word == current_word]

        # If no matches were found, start over with a new random word
        if not matches:
            current_word = random.choice(words)
            continue

        # Select a random occurrence of the current word
        index = random.choice(matches)

        # Add the next word to the predicted words list
        next_word = words[index + 1]
        predicted_words.append(next_word)

        # Set the current word to the predicted next word
        current_word = next_word

    # Return the predicted words as a JSON response
    return jsonify(predicted_words)

if __name__ == '__main__':
    app.run()

