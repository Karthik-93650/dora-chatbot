def dora():
    print("👋 Hi! I'm Dora.")
    print("You can talk to me freely. Type 'bye' anytime to exit.\n")

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
            print("🤖 Dora: I can chat with you and answer simple questions.")

        elif "help" in user_input:
            print("🤖 Dora: You can say hello, ask my name, or just talk to me 😄")

        else:
            print("🤖 Dora: Hmm… I didn’t fully get that, but I’m listening 😊")


if __name__ == "__main__":
    dora()