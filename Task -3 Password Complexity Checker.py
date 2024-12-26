import re
import math
from getpass import getpass
from random import randint, choice
def calculate_entropy(password):
    charset_size = 0
    if any(char.islower() for char in password):
        charset_size += 26
    if any(char.isupper() for char in password):
        charset_size += 26
    if any(char.isdigit() for char in password):
        charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    return round(entropy, 2)
def check_criteria(password):
    feedback = []
    stars = 0

    if len(password) >= 12:
        stars += 1
    else:
        feedback.append("Extend your password to at least 12 characters!")
    if any(char.isupper() for char in password):
        stars += 1
    else:
        feedback.append("Include an uppercase letter for extra strength.")

    if any(char.islower() for char in password):
        stars += 1
    else:
        feedback.append("Include a lowercase letter to balance things.")

    if any(char.isdigit() for char in password):
        stars += 1
    else:
        feedback.append("Add some numbers to make your password unpredictable.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        stars += 1
    else:
        feedback.append("Throw in some special characters for flair!")

    return stars, feedback
def generate_progress_bar(stars):
    filled = "🟩" * stars
    empty = "⬜" * (5 - stars)
    return filled + empty
def password_to_emojis(password):
    emoji_map = {
        "a": "🍎", "b": "🍌", "c": "🌵", "d": "🐶", "e": "🥚", 
        "f": "🐟", "g": "🍇", "h": "🏠", "i": "🍦", "j": "😂",
        "k": "🔑", "l": "🍋", "m": "🐒", "n": "🎵", "o": "🐙",
        "p": "🍍", "q": "👑", "r": "🌹", "s": "🌞", "t": "🌴",
        "u": "☂️", "v": "🎻", "w": "🐋", "x": "❌", "y": "🍸", "z": "⚡"
    }
    return "".join(emoji_map.get(char.lower(), char) for char in password)
def leaderboard(password_strength):
    competitors = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    scores = [randint(30, 80) for _ in competitors]
    user_score = randint(85, 100) if password_strength == "Very Strong" else randint(50, 84)
    competitors.append("You")
    scores.append(user_score)
    sorted_leaderboard = sorted(zip(competitors, scores), key=lambda x: x[1], reverse=True)
    return sorted_leaderboard
def main():
    print("\n---------------- 🎮 Crazy Password Strength Tool 🎮 ----------------")
    print("Welcome to the password arena! Let's see if your password can top the leaderboard.")
    password_input = getpass("\nEnter your password (input is hidden): ")
    entropy = calculate_entropy(password_input)
    stars, feedback = check_criteria(password_input)
    strength_levels = ["Weak", "Moderate", "Strong", "Very Strong"]
    strength = strength_levels[stars - 1] if stars > 0 else "Very Weak"
    progress_bar = generate_progress_bar(stars)
    emoji_password = password_to_emojis(password_input)
    print(f"\nPassword Strength: {progress_bar} ({strength})")
    print(f"Entropy Score: {entropy} bits")
    print(f"Emoji Transformation: {emoji_password}")
    if feedback:
        print("\nSuggestions for Improvement:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("\nYou're a password pro! No improvement needed. 🌟")
    print("\n🔝 Leaderboard (Random Challenge):")
    ranking = leaderboard(strength)
    for idx, (name, score) in enumerate(ranking, start=1):
        print(f"{idx}. {name} - {score} points")
    print("\n💡 Did You Know? The world's longest password ever created was 63,000 characters long!")
if __name__ == "__main__":
    main()
