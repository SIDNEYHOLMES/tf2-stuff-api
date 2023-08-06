from flask import Flask, jsonify, send_file
from console_logging import console
import base64
import os
app = Flask(__name__)


absolute_path = os.path.dirname(__file__)
test_img_path = 'testimg1.PNG'
weapon_img_path = os.path.join(absolute_path, 'imgs/weapons/', test_img_path)

console.log(weapon_img_path)


@app.route('/get_data', methods=['GET'])
def get_data():
    #object 
    data = {
        'name': 'scattergun',
        'class': 'scout',
        'type': 'default',
        'image': get_base64_image(weapon_img_path)
    }

    return jsonify(data)

def get_base64_image(image_path):
    # need to properly take the image file 
    # path and convert it into something useable
   

    return image_path

if __name__ == '__main__':
    app.run(debug=True)
