from loki_core import Loki

loki = Loki()

while True:
    user_input = input("You: ")
    if user_input.lower() in ["shutdown", "quit", "exit"]:
        print("Goodbye user!")
        break
    response = loki.hear(user_input)
    print("Loki:", response)
