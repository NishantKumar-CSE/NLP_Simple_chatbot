from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

QA = [
    [r"my name is (.+)", ["Hello %1, good to see you! Do you have any questions for me?"]],
    [r"(what is your name|who are you|who's there)\s*\??", ["My name is GYANI Get Your Answers New Insights, and I'm your friend. Let's chat!"]],
    [r"how are you\??", ["I'm doing well, thank you! What about you?"]],
    [r"(friends?|am I lonely)\s*\??", ["I have many friends and just made a new one! Hi there! :)"]],
    [r"i'm sorry|i am sorry", ["It's alright", "It's OK, never mind, friend."]],
    [r"doing good|fine", ["Nice to hear that!", "Alright! :)"]],
    [r"hi|hey|hello|greetings", ["Hello!", "Hey there!"]],
    [r"your age|old are you", ["I'm a computer program. Still want to know my age?"]],
    [r"(want|need) (.*)", ["I want to help you find answers!"]],
    [r"(who|what) (created|made) you", ["I am a result of Nakul's exploration of the NLTK Library."]],
    [r"(where|location|city)", ['I reside in Gangtok, Sikkim.']],
    [r"how is the weather in (.+)\??", [
        "Weather in %1 is awesome as always!",
        "It's perfect here in %1!",
        "Too cold here in %1!",
        "I have heard about %1. You are lucky to stay in the beautiful city of %1!"
    ]],
    [r"work in (.+)\??", ["%1 sounds like an amazing company to work for! Hope you love it."]],
    [r"(is it|it's|do you think) raining in (.+)", [
        "You never know when it can rain here in %2.",
        "Damn, it's raining too much here in %2!"
    ]],
    [r"how (is|are) health\??", ["I'm a computer program, so I'm always healthy!"]],
    [r"(like|favorite) (sports|games)", ["I'm a big fan of Cricket!"]],
    [r"quit|exit|goodbye", ["Bye, take care! Hope to see you soon, friend! :)"]],
    [r"(have|can you have|you have) all the answers\??", [
        "I can help you with most of your questions! :)",
        "Maybe you can help: https://www.google.com/"
    ]],
    [r"(.*) siri(.*)", ["Hey! Do you know her too? What a small world!", "She is my best friend!"]],
    [r"(help|lost|direction|maps)", [
        "I think this is best for you: https://www.google.com/maps",
        "Are you lost? Keep calm and click here: https://www.google.com/maps"
    ]],
    [r"(weather|forecast)", [
        "You can check here: https://www.accuweather.com/en/in/india-weather. Have a great day!"
    ]],
    [r"what do you like\??", ["There's only one thing I like: chatting!"]]
]


# Create a chatbot
chatbot = Chat(QA, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = request.args.get('msg')
    return str(chatbot.respond(user_input))

if __name__ == "__main__":
    app.run()