from flask import url_for

class ScoutWeapons:

  def scattergun():
    return {
      'name': 'scattergun',
      'class': 'scout',
      'type': 'default',
      'image': url_for("static", filename="scout_images/default_scattergun.png") ## 
      }
  