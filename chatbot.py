import datetime
import random

def dora():
    print("👋 Hi! I'm Dora.")
    print("You can talk to me freely. Type 'bye' anytime to exit.\n")

    name = ""

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("🤖 Dora: Bye! Take care and have a great day 😊")
            break

        elif user_input in ["hi", "hello", "hey"]:
            print("🤖 Dora: Hello! Nice to meet you 😊")

        elif "how are you" in user_input:
            print("🤖 Dora: I'm doing good, thanks for asking! How about you?")

        elif "your name" in user_input:
            print("🤖 Dora: I'm Dora. Nice to meet you 🤍")

        elif "what can you do" in user_input:
            print("🤖 Dora: I can chat with you, remember your name, and answer simple questions.")

        elif "help" in user_input:
            print("🤖 Dora: You can greet me, tell your name, ask time, or just chat 😄")

        # 👉 Memory feature
        elif "my name is" in user_input:
            name = user_input.replace("my name is", "").strip()
            print(f"🤖 Dora: Nice to meet you {name.title()} 😊")

        elif "who am i" in user_input:
            if name:
                print(f"🤖 Dora: You are {name.title()} 😄")
            else:
                print("🤖 Dora: I don’t know your name yet! Tell me 😊")

        # 👉 Time feature
        elif "time" in user_input:
            now = datetime.datetime.now().strftime("%H:%M")
            print(f"🤖 Dora: Current time is {now} ⏰")

        elif "date" in user_input:
            today = datetime.datetime.now().strftime("%d %B %Y")
            print(f"🤖 Dora: Today is {today} 📅")

        # 👉 Smart fallback responses
        else:
            responses = [
                "Interesting… tell me more 🤔",
                "I’m still learning, but that sounds cool!",
                "Hmm, can you explain that differently?",
                "Got it… I’ll try to learn that soon 😄",
                "That’s something new for me!"
            ]
            print(f"🤖 Dora: {random.choice(responses)}")


if __name__ == "__main__":
    dora()