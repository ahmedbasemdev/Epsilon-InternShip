from flask import Flask , render_template
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load(open('model.h5','rb'))


@app.route('/')
def home():
    return render_template('home.html')


if __name__ ==  "__main__":
    app.run(debug=True , port = 9000)