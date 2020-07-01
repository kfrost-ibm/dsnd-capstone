from flask import Flask
from flask import render_template, request, jsonify
import joblib
import json
import pandas as pd

app = Flask(__name__)

# load model
model = joblib.load("../models/classifier.pkl")

# open parameters JSON file
with open('../models/parameters.json') as json_file:
    parameters = json.load(json_file)

# open column json
with open('../models/columns.json') as json_file:
    columns = json.load(json_file)

# setup webapp routes
@app.route('/')
@app.route('/index')

# home page route
def index():
    return render_template('index.html', parameters=parameters)

# view results route
@app.route('/run')
def run():
    # create a dict object from request parameters
    house = request.args.to_dict(flat=True)

    # convert any number parameters to int
    for key in house.keys():
        type = parameters[key]['type']

        if type == 'number':
            house[key] = int(house[key])

    # create a dataframe from the parameter dict
    df = pd.DataFrame(house, index=[0])
    # create dummy variables for categorical features
    df = pd.get_dummies(df)
    # add missing columns and fill with 0
    df = df.reindex(columns=columns, fill_value=0)

    # use model to predict house price for query
    value = model.predict(df)[0]

    # render results
    return render_template(
        'run.html',
        value=value
    )

def main():
    app.run(host='0.0.0.0', port=3001, debug=True)

if __name__ == '__main__':
    main()
