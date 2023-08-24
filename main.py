import random
import json

def load_data():
    with open('master.json', 'r') as f:
        return json.load(f)

def game(data):
    correct = 0
    incorrect = 0
    random.shuffle(data)

    for item in data:
        answer = input(f"What is the origin of {item['WineName']}? ")
        
        if answer == str(item['CountryState']):
            correct += 1
            print("Correct!")
            print(f"You have {correct} correct and {incorrect} incorrect answers.")
        else:
            incorrect += 1
            print("Incorrect!")
            print(f"Correct: {correct} Incorrect: {incorrect}")

    print(f"Game over! You got {correct} correct and {incorrect} incorrect answers.")

data = load_data()

while True: 
    print("Greetings! How well do you know your wine?")
    print("Guess the country origin of each wine")
    game(data)
    
    replay = input("Would you like to play again? (yes/no): ")
    if replay.lower() != 'yes':
        break
