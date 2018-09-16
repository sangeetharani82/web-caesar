from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

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
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form method="post">
            <label for="rot">
                Rotate by
            </label>
                <input type="text" name="rot" value="0" id="rot"/>
                <br>
                <textarea type="text" name="text">{0}</textarea>
                <br>
                <input type="submit" value="Submit Query"/>

        </form>

    </body>
</html>
"""



@app.route("/", methods=['POST'])
def encrypt():
    rotate_by = request.form['rot']
    rotate_by = int(rotate_by)
    te_xt = request.form['text']
    #te_xt =  str(te_xt)
    resp = ""
    encrypted = rotate_string(te_xt, rotate_by)
    return .format(encrypted)
    


@app.route("/")
def index():
    return form



app.run()