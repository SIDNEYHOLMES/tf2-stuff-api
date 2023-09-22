from flask import url_for

## CONTAINES ALL SCOUT WEAPONS 

# TODO
# All weapon classes need to be added
# Weapon images need to be in the folder and corrisponding url (instead of default from wiki)

# EXAMPLE  |||||||||||||||||||
 
  # def bat():
  #   return {
  #     'name': 'bat',
  #     'class': 'scout',
  #     'type': 'stock',
  #     'image': url_for('static', filename='scout_images/default_bat.png')
  #   }

class ScoutWeapons:
    def scattergun():
        return {"name": "scattergun", 'class': 'scout', 'type': 'Stock', 'image': 'localhost:5000/image/class_weapon/scout/scattergun'}

    def force_a_nature():
        return {"name": "force-A-Nature", 'class': 'scout', 'type': 'Unlock', 'image': 'localhost:5000/image/class_weapon/scout/force_a_nature'}

    def shortstop():
        return {"name": "shortstop", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/shortstop'}

    def soda_popper():
        return {"name": "soda popper", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/soda_popper'}

    def baby_faces_blaster():
        return {"name": "baby face's blaster", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/baby_faces_blaster'}

    def back_scatter():
        return {"name": "back scatter", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/back_scatter'}

    def pistol():
        return {"name": "pistol", 'class': ['scout', 'engineer'], 'type': 'Stock', 'image': 'localhost:5000/image/class_weapon/scout/pistol'}

    def lugermorph():
        return {"name": "lugermorph", 'class': ['scout', 'engineer'], 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/lugermorph'}

    def capper():
        return {"name": "c.a.p.p.e.r", 'class': ['scout', 'engineer'], 'type': 'Uncrate', 'image': 'localhost:5000/image/class_weapon/scout/c.a.p.p.e.r'}

    def winger():
        return {"name": "winger", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/winger'}

    def pretty_boys_pocket_pistol():
        return {"name": "pretty boy's pocket pistol", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/pretty_boys_pocket_pistol'}

    def flying_guillotine():
        return {"name": "flying guillotine", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/flying_guillotine'}

    def bonk_atomic_punch():
        return {"name": "bonk! atomic punch", 'class': 'scout', 'type': 'Unlock', 'image': 'localhost:5000/image/class_weapon/scout/bonk_atomic_punch'}

    def crit_a_cola():
        return {"name": "crit-a-cola", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/crit_a_cola'}

    def mad_milk():
        return {"name": "mad milk", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/mad_milk'}

    def mutated_milk():
        return {"name": "mutated milk", 'class': 'scout', 'type': 'Uncrate', 'image': 'localhost:5000/image/class_weapon/scout/mutated_milk'}

    def bat():
        return {"name": "bat", 'class': 'scout', 'type': 'Stock', 'image': 'localhost:5000/image/class_weapon/scout/bat'}

    def holy_mackerel():
        return {"name": "holy mackerel", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/holy_mackerel'}

    def unarmed_combat():
        return {"name": "unarmed combat", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/unarmed_combat'}

    def batsaber():
        return {"name": "batsaber", 'class': 'scout', 'type': 'Uncrate', 'image': 'localhost:5000/image/class_weapon/scout/batsaber'}

    def sandman():
        return {"name": "sandman", 'class': 'scout', 'type': 'Unlock', 'image': 'localhost:5000/image/class_weapon/scout/sandman'}

    def candy_cane():
        return {"name": "candy cane", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/candy_cane'}

    def boston_basher():
        return {"name": "boston basher", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/boston_basher'}

    def three_rune_blade():
        return {"name": "three-rune blade", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/three_rune_blade'}

    def sun_on_a_stick():
        return {"name": "sun-on-a-stick", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/sun_on_a_stick'}

    def fan_owar():
        return {"name": "fan o'war", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/fan_owar'}

    def atomizer():
        return {"name": "atomizer", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/atomizer'}

    def wrap_assassin():
        return {"name": "wrap assassin", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/wrap_assassin'}
