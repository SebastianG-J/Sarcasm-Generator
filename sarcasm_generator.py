import random

# List of emojis to make it extra spicy
EMOJIS = ["💅", "😎", "🤡", "🙃", "🔥", "👀", "😂", "🧠"]

def to_sarcastic(text: str) -> str:
    """Convert text to a sarcastic version with random upper/lower casing."""
    sarcastic_text = "".join(
        random.choice([ch.upper(), ch.lower()]) if ch.isalpha() else ch
        for ch in text
    )
    emoji = random.choice(EMOJIS)
    return sarcastic_text + " " + emoji

def main():
    print("🤖 Welcome to the Sarcasm Generator 3000")
    user_input = input("Enter your text: ")
    result = to_sarcastic(user_input)
    print("\nYour sarcastic masterpiece:")
    print(result)

if __name__ == "__main__":
    main()
