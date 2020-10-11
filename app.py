import numpy as np
import xgboost as xgb
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


model = xgb.XGBClassifier({'nthread': 4})  # init model
model .load_model('0001.model')  # load data


samples = []


def predict_bot(points):
    try:
        points = np.array(points).reshape(1, 80)
    except BaseException:
        return 1, -1
    res = model.predict_proba(points)[0][1]
    # res=0.5
    res_bin = res > 0.7
    return res_bin, res


@app.route('/points', methods=['POST'])
@cross_origin()
def save_points():
    try:
        points = request.get_json()['points']
    except KeyError:
        return jsonify({'response': 'FAIL',
                        'msg': 'INCORRECT INPUT'})

    if len(points) == 40:
        samples.append(points)
    else:
        return jsonify({'response': 'FAIL',
                        'msg': 'INCORRECT INPUT'})

    bot, score = predict_bot(points)

    if bot == False:
        return jsonify({'response': "SUCCESS",
                        'msg': f"{score}"})
    else:
        if score == -1:
            return jsonify({'response': 'FAIL',
                     'msg': 'INCORRECT INPUT'})
        return jsonify({'response': "FAIL",
                        'msg': f"{score}"})

@app.route('/points', methods=['GET'])
def manage_points():
    global samples
    data = samples.copy()
    samples = []
    return {'points': data}


if __name__ == '__main__':
    app.run(debug=True)

