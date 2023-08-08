from flask import Flask, jsonify, send_file, make_response
import os

app = Flask(__name__)

absolute_path = os.path.dirname(__file__)
test_img_path = 'testimg1.PNG'
weapon_img_path = os.path.join(absolute_path, 'imgs/weapons/', test_img_path)

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {
        'name': 'scattergun',
        'class': 'scout',
        'type': 'default',
        'image_url': f"/get_weapon_image",  # Provide the image URL
    }
    return make_response(jsonify(data), 200)

@app.route('/get_weapon_image', methods=['GET'])
def serve_weapon_image():
    return send_file(weapon_img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
