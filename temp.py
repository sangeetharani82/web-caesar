from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      #<!-- create your form here -->
        <form action="/form" method="post">
            <label for="rot">
                Rotate by
                <input type="text" id="rot" name="rot"/>
            </label>
            #<input type="textarea" name="text"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

app.run()