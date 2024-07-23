# Probabilities of Winning the Game

This Python program calculates the probabilities that Bob wins a game where he and Alice take turns rolling a k-sided die.
Whichever player rolls a k first wins the game.

## Setup

1. Make sure you have Python installed. 
   You can check by running `python --version` in your terminal. If Python is not installed, you need to install it first.

2. Install the required Python packages by running `pip install -r requirements.txt` in the terminal.

## Running the Program

To calculate the probabilities and print them to the console, run `python main.py`.

To run the unit tests, run `python test_main.py`.

## Bonus: Running the Program with Flask

1. Start the Flask application by running `waitress-serve --port=5000 app:app`.

2. The server will start running locally on your machine at `http://localhost:5000`. You can access the API by making a GET request to `http://localhost:5000/probability`.

3. If you want to provide a value for `k`, you can add it as a header in your GET request. If the `k` header is provided, the server will return the probability for that value of `k`. If not, it will return the probabilities for `k` from 6 to 99.