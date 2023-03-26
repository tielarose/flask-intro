"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
      <html>
      Hi! This is the home page.
      <a href="/hello"> go to hello page </a>
      </html>
            """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <label for="compliment">Choose Your Compliment:</label>
          <select name="compliment">
            <option value="awesome"> Awesome </option>
            <option value="terrific"> Terrific </option>
            <option value="fantastic"> Fantastic </option>
          </select> 
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <label for="diss">Choose Your Diss:</label>
          <select name="diss">
            <option value="mean"> Mean </option>
            <option value="terrible"> Terrible </option>
            <option value="horrible"> Horrible </option>
          </select> 
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")
   # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
