from flask import Flask, jsonify, send_file, make_response
from flask_caching import Cache
import os

## object containing all weapon classes with the keys being the class name
from tf2_data.weapons import ALL_WEAPON_CLASSES 

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

absolute_path = os.path.dirname(__file__)
test_img_path = 'testimg1.PNG'
weapon_img_path = os.path.join(absolute_path, 'imgs/weapons/', test_img_path)

## clear cache (for debugging)

@app.route('/clearcache', methods=['POST'])
def clear_cache():
    cache.clear()
    return 'CLEARD'

## ||||||||||| WEAPONS ||||||||||||||
@app.route('/weapon/<class_name>/<weapon_name>', methods=['GET']) ## ROUTE FOR INPUTTED CLASS WEAPONS
## takes weapon name and class name from route and checks corrisponding module for a match
def get_weapon(weapon_name, class_name): 
    if (weapon_name == 'all'): # if input is all
        if class_name in ALL_WEAPON_CLASSES: ## if the class exsists in the module 
            result_dict = {} # result dictionary to be returned
            weapon_class = ALL_WEAPON_CLASSES[class_name] # retrieves the model of the inputted class
            #retrieves public classes from moduel. (all of the weapon functions from the class)
            public_method_names = [method for method in dir(weapon_class) if callable(getattr(weapon_class, method)) if not method.startswith('_')]
            for weapon_method in public_method_names: # each weapon method returns its data to the result dictionary
                result_dict[weapon_method] = getattr(weapon_class, weapon_method)()  
            
            return make_response(jsonify({'data': result_dict}), 200)
        else:
            return make_response(jsonify({'error': 'Class not found (check route spelling)'}), 404)
        
        
    # otherwise the weapon name is specified
    weapon_method = getattr(ALL_WEAPON_CLASSES[class_name], weapon_name, None) ## retrieves weapon module
    if weapon_method and callable(weapon_method): ## if inputted name is same as class method, return weapon data
        weapon_data = weapon_method()
        return make_response(jsonify({'data': weapon_data}), 200)
    else: ## failed, weapon dosent exsist (or mispelled)
        return make_response(jsonify({'error': 'Weapon or lass not found (check route spelling)'}), 404)
    
    
## ||||||||||| LORE ||||||||||||||


## ||||||||||| CHARACTER STUFF ||||||||||||||||||
# @app.route('/character/mercs/<class_name>', method=['GET'])
# def get_class_info(class_name):
#     data = {
#         'name': 'jermey',
#         'class_name': 'scout',
#         'fav_food': 'bucket of fried chiken', // this goes in lore prob
#         'class_data': {'boring class data like speed and stuff'},
#         'lore': '/lore/mercs/scout'       
#     }
#     return data


##  ||||||||||||||  IMAGES ||||||||||||||||
## get weapon image by class and weapon name
@app.route('/image/class_weapon/<class_name>/<weapon_name>', methods=['GET'])
def serve_weapon_image(class_name, weapon_name):
    weapon_img_path = os.path.join(absolute_path, 'static/weapons', class_name + '_images' , weapon_name +'.png') ## path of weapon image
    if os.path.exists(weapon_img_path): ## if a image is located at path
        return make_response(send_file(weapon_img_path, mimetype='image/png'), 200)
    else:
        return make_response(jsonify({'error': 'weapon or class image not found (check route spelling)'}), 404)
    
    

if __name__ == '__main__':
    app.run(debug=True)
