import random

WORDS = [
    "aback", "abate", "abhor", "abode", "abort",
    "about", "above", "abuse", "abyss", "actor",
    "adapt", "admix", "adobe", "adult", "affix",
    "after", "again", "alamo", "alarm", "alert",
    "alien", "apple", "aptly", "arise", "aroma",
    "array", "audio", "badge", "baker",
    "beard", "blame", "blend",
    "brave", "brick", "broad", "cabin", "candy",
    "carry", "chair", "chart", "chase", "check",
    "charm", "chirp", "clock", "chock", "clean",
    "clear", "cliff", "cloud", "crane", "crash",
    "creek", "cried", "crown", "cubic", "debts",
    "debit", "demon", "diver", "doubt", "eager",
    "early", "earth", "elbow", "empty", "enter",
    "every", "feast", "fiber", "flame",
    "flock", "frame", "fuzzy", "gamer", "gleam",
    "globe", "grape", "grief", "grind", "grove",
    "growl", "guine", "habit", "heart",
    "hiker", "horns", "house", "index", "irony",
    "juice", "joint", "jolly", "laser",
    "latch", "liver", "loose", "manor", "metal",
    "minor", "molar", "needy", "novel", "north",
    "obese", "ocean", "olive", "often", "party",
    "pearl", "peace", "place", "plane", "plant",
    "proud", "raise", "rains", "racer", "react",
    "scale", "screw", "serve", "shape", "sheep",
    "shine", "slate", "snoop", "speak",
    "start", "sugar", "sweet", "table", "theta",
    "tiger", "train", "treat", "trust", "uncle",
    "upset", "vague", "water", "whale", "write",
    "yacht", "yearn", "zebra"
]

def pick_word():
    return random.choice(WORDS)

def check_guess(secret, guess):
    result = []
    secret_copy = list(secret)
    guess = guess.lower()
    for i in range(5):
        if guess[i] == secret[i]:
            result.append('🟩')
            secret_copy[i] = None
        else:
            result.append(None)
    for i in range(5):
        if result[i] is None:
            if guess[i] in secret_copy:
                result[i] = '🟨'
                secret_copy[secret_copy.index(guess[i])] = None
            else:
                result[i] = '⬛'
    return ''.join(result)

def main():
    print("wordle! guess the 5-letter word.")
    secret_word = pick_word()
    tries = 6
    for attempt in range(1, tries + 1):
        while True:
            guess = input(f"attempt {attempt}/{tries}: ").strip().lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print("please enter a 5-letter word.")
        if guess == secret_word:
            print("🟩🟩🟩🟩🟩  You win! 🎉")
            print(f"the word was: {secret_word}")
            return
        else:
            feedback = check_guess(secret_word, guess)
            print(feedback)
    print(f"outta tries, the word was: {secret_word}")

main()
