from flask import Flask, request, jsonify
import json
from processImage import identifyMark, setStandardValues

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def identifyStandard():
    data = request.json
    d = {}
    d['found'], d['img'], d['height'] = identifyMark(data['image'])
    return jsonify(d)
    
@app.route('/setting', methods=['POST'])
def settingStandard():
	data = request.json
	d = {}
	d['img'], d['img_dil'] = setStandardValues(data['image'], data['values'])
	return jsonify(d)
    
if __name__ == '__main__':
    app.run()

