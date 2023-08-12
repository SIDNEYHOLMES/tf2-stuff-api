from flask import url_for

class ScoutWeapons:

  def scattergun():
    return {
      'name': 'scattergun',
      'class': 'scout',
      'type': 'stock',
      'image': url_for('static', filename='scout_images/default_scattergun.png') 
      }
    
  def pistol():
    return {
      'name': 'pistol',
      'class': ['scout', 'engineer'],
      'type': 'stock',
      'image': url_for('static', filename='global_weapon_images/default_pistol.png') 
    }
  
  def bat():
    return {
      'name': 'bat',
      'class': 'scout',
      'type': 'stock',
      'image': url_for('static', filename='scout_images/default_bat.png')
    }