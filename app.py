from flask import Flask, jsonify, send_file, make_response
import os

## object containing all weapon classes with the keys being the class name
from tf2_data.weapons import ALL_WEAPON_CLASSES 

app = Flask(__name__)

absolute_path = os.path.dirname(__file__)
test_img_path = 'testimg1.PNG'
weapon_img_path = os.path.join(absolute_path, 'imgs/weapons/', test_img_path)


## ||||||||||| WEAPONS ||||||||||||||
@app.route('/weapon/<class_name>/<weapon_name>', methods=['GET']) ## ROUTE FOR INPUTTED CLASS WEAPONS (DYNAMIC)
def get_weapon(weapon_name, class_name): ## takes weapon name and class name from route and checks corrisponding module for a match
    weapon_method = getattr(ALL_WEAPON_CLASSES[class_name], weapon_name, None) ## retrieves weapon module
    
    if weapon_method and callable(weapon_method): ## if inputted name is same as class method, return weapon data
        weapon_data = weapon_method()
        return make_response(jsonify({'weapon': weapon_data}), 200)
    else: ## failed, weapon dosent exsist (or mispelled)
        return make_response(jsonify({'error': 'Weapon or class not found (check route spelling)'}), 404)
    
## ||||||||||| LORE ||||||||||||||


## ||||||||||| CHARACTER STUFF ||||||||||||||||||
@app.route('/character/mercs/<class_name>', method=['GET'])
def get_class_info(class_name):
    data = {
        'name': 'jermey',
        'class_name': 'scout',
        'fav_food': 'bucket of fried chiken',
        'class_data': {'boring class data like speed and stuff'},
        'lore': '/lore/mercs/scout'       
    }
    return data


##  ||||||||||||||  IMAGES ||||||||||||||||

@app.route('/get_weapon_image', methods=['GET'])
def serve_weapon_image():
    return send_file(weapon_img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
