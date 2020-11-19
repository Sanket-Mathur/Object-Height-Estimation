from flask import Flask, request, jsonify
import json
from processImage import identifyMark

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def identifyStandard():
    data = request.json
    d = {}
    d['found'], d['img'] = identifyMark(data['image'])
    return jsonify(d)
    
if __name__ == '__main__':
    app.run()

