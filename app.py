from flask import Flask, jsonify, send_file, make_response
import os

from tf2_data.weapons.scout_weapons import ScoutWeapons
app = Flask(__name__)

absolute_path = os.path.dirname(__file__)
test_img_path = 'testimg1.PNG'
weapon_img_path = os.path.join(absolute_path, 'imgs/weapons/', test_img_path)


## ||||||||||| WEAPONS ||||||||||||||
@app.route('/weapon/scout/<weapon_name>', methods=['GET']) ## ROUTE FOR SCOUT WEAPONS (DYNAMIC)
def Scout_Weapon(weapon_name): ## takes weapon name from route and checks the scout weapons module for a match
   weapon_method = getattr(ScoutWeapons, weapon_name, None) ## retrieves scout weapon from module
    
   if weapon_method and callable(weapon_method): ## if wep name is same as class method, return weapon data
        weapon_data = weapon_method()
        return make_response(jsonify({'weapon': weapon_data}), 200)
   else: ## failed, weapon dosent exsist (or mispelled)
        return make_response(jsonify({'error': 'Weapon not found'}), 404)
    
## ||||||||||| LORE ||||||||||||||


## ||||||||||| CHARACTER STUFF ||||||||||||||||||


##  ||||||||||||||  IMAGES ||||||||||||||||

@app.route('/get_weapon_image', methods=['GET'])
def serve_weapon_image():
    return send_file(weapon_img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
