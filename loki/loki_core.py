from datetime import datetime
import subprocess


class Loki:
    def __init__(self):
        self.name = "Loki"
        self.time = datetime.now()
        self.user = None

    # Input layer
    def hear(self, text):
        # Append the current message

        intent, data = self.parse_intent(text)
        return self.decide(intent, data)

    # Intent parsing
    def parse_intent(self, text):
        t = text.lower()

        if "open" in t and "browser" in t:
            return ("open_app", "browser")
        if "open" in t and "terminal" in t:
            return ("open_app", "terminal")
        if "open" in t and "spotify" in t:
            return ("open_app", "spotify")

        if "what time is it" in t:
            return ("get_time", None)

        if "who are you" in t:
            return ("identity", None)

        if "hello" in t:
            return ("greeting", None)
        if "remember" in t:
            return ("remember", text)

        return ("unknown", None)

    # Decision layer
    def decide(self, intent, data):
        if intent == "open_app":
            return self.open_app(data)
        if intent == "get_time":
            self.time = datetime.now()
            return self.tell_time()
        if intent == "identity":
            return f"I am {self.name}."
        if intent == "greeting":
            return "Hey, let's work on this, shall we?"

        return "I didn't understand your request."

    # Memory layer
    # def remember(self, data):
    # TODO: Add filtering on what to remember

    # Action layer
    def open_app(self, app):
        match app:
            case "browser":
                subprocess.Popen(["zen-browser"])
                return "Opening browser"
            case "terminal":
                subprocess.Popen(["kitty"])
                return "Opening terminal"
            case "spotify":
                subprocess.Popen(["spotify"])
                return "Opening Spotify"

    def tell_time(self):
        return f"The time is: {self.time.hour}:{self.time.minute:02d}"
