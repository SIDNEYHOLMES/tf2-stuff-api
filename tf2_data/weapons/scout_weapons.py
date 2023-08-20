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
        return {"name": "Scattergun", 'class': 'scout', 'type': 'Stock', 'image': '/w/images/thumb/1/1b/Item_icon_Scattergun.png/100px-Item_icon_Scattergun.png'}

    def force_a_nature():
        return {"name": "Force-A-Nature", 'class': 'scout', 'type': 'Unlock', 'image': '/w/images/thumb/e/ed/Item_icon_Force-A-Nature.png/100px-Item_icon_Force-A-Nature.png'}

    def shortstop():
        return {"name": "Shortstop", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/8/84/Item_icon_Shortstop.png/100px-Item_icon_Shortstop.png'}

    def soda_popper():
        return {"name": "Soda Popper", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/f/f1/Item_icon_Soda_Popper.png/100px-Item_icon_Soda_Popper.png'}

    def baby_faces_blaster():
        return {"name": "Baby Face's Blaster", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/e/e6/Item_icon_Baby_Face%27s_Blaster.png/100px-Item_icon_Baby_Face%27s_Blaster.png'}

    def back_scatter():
        return {"name": "Back Scatter", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/1/11/Item_icon_Back_Scatter.png/100px-Item_icon_Back_Scatter.png'}

    def pistol():
        return {"name": "Pistol", 'class': ['scout', 'engineer'], 'type': 'Stock', 'image': '/w/images/thumb/5/52/Item_icon_Pistol.png/100px-Item_icon_Pistol.png'}

    def lugermorph():
        return {"name": "Lugermorph", 'class': ['scout', 'engineer'], 'type': 'Promotional', 'image': '/w/images/thumb/8/86/Item_icon_Lugermorph.png/100px-Item_icon_Lugermorph.png'}

    def capper():
        return {"name": "C.A.P.P.E.R", 'class': ['scout', 'engineer'], 'type': 'Uncrate', 'image': '/w/images/thumb/a/a6/Item_icon_C.A.P.P.E.R.png/100px-Item_icon_C.A.P.P.E.R.png'}

    def winger():
        return {"name": "Winger", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/4/4e/Item_icon_Winger.png/100px-Item_icon_Winger.png'}

    def pretty_boys_pocket_pistol():
        return {"name": "Pretty Boy's Pocket Pistol", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/f/f6/Item_icon_Pretty_Boy%27s_Pocket_Pistol.png/100px-Item_icon_Pretty_Boy%27s_Pocket_Pistol.png'}

    def flying_guillotine():
        return {"name": "Flying Guillotine", 'class': 'scout', 'type': 'Promotional', 'image': '/w/images/thumb/5/5a/Item_icon_Flying_Guillotine.png/100px-Item_icon_Flying_Guillotine.png'}

    def bonk_atomic_punch():
        return {"name": "Bonk! Atomic Punch", 'class': 'scout', 'type': 'Unlock', 'image': '/w/images/thumb/8/8f/Item_icon_Bonk%21_Atomic_Punch.png/100px-Item_icon_Bonk%21_Atomic_Punch.png'}

    def crit_a_cola():
        return {"name": "Crit-a-Cola", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/a/ae/Item_icon_Crit-a-Cola.png/100px-Item_icon_Crit-a-Cola.png'}

    def mad_milk():
        return {"name": "Mad Milk", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/5/56/Item_icon_Mad_Milk.png/100px-Item_icon_Mad_Milk.png'}

    def mutated_milk():
        return {"name": "Mutated Milk", 'class': 'scout', 'type': 'Uncrate', 'image': '/w/images/thumb/b/bd/Item_icon_Mutated_Milk.png/100px-Item_icon_Mutated_Milk.png'}

    def bat():
        return {"name": "Bat", 'class': 'scout', 'type': 'Stock', 'image': '/w/images/thumb/b/b5/Item_icon_Bat.png/100px-Item_icon_Bat.png'}

    def holy_mackerel():
        return {"name": "Holy Mackerel", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/8/86/Item_icon_Holy_Mackerel.png/100px-Item_icon_Holy_Mackerel.png'}

    def unarmed_combat():
        return {"name": "Unarmed Combat", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/9/96/Item_icon_Unarmed_Combat.png/100px-Item_icon_Unarmed_Combat.png'}

    def batsaber():
        return {"name": "Batsaber", 'class': 'scout', 'type': 'Uncrate', 'image': '/w/images/thumb/e/ef/Item_icon_Batsaber.png/100px-Item_icon_Batsaber.png'}

    def sandman():
        return {"name": "Sandman", 'class': 'scout', 'type': 'Unlock', 'image': '/w/images/thumb/7/70/Item_icon_Sandman.png/100px-Item_icon_Sandman.png'}

    def candy_cane():
        return {"name": "Candy Cane", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/0/05/Item_icon_Candy_Cane.png/100px-Item_icon_Candy_Cane.png'}

    def boston_basher():
        return {"name": "Boston Basher", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/b/b5/Item_icon_Boston_Basher.png/100px-Item_icon_Boston_Basher.png'}

    def three_rune_blade():
        return {"name": "Three-Rune Blade", 'class': 'scout', 'type': 'Promotional', 'image': '/w/images/thumb/f/f6/Item_icon_Three-Rune_Blade.png/100px-Item_icon_Three-Rune_Blade.png'}

    def sun_on_a_stick():
        return {"name": "Sun-on-a-Stick", 'class': 'scout', 'type': 'Promotional', 'image': '/w/images/thumb/0/06/Item_icon_Sun-on-a-Stick.png/100px-Item_icon_Sun-on-a-Stick.png'}

    def fan_owar():
        return {"name": "Fan O'War", 'class': 'scout', 'type': 'Promotional', 'image': '/w/images/thumb/f/f4/Item_icon_Fan_O%27War.png/100px-Item_icon_Fan_O%27War.png'}

    def atomizer():
        return {"name": "Atomizer", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/2/29/Item_icon_Atomizer.png/100px-Item_icon_Atomizer.png'}

    def wrap_assassin():
        return {"name": "Wrap Assassin", 'class': 'scout', 'type': 'Craft', 'image': '/w/images/thumb/6/6b/Item_icon_Wrap_Assassin.png/100px-Item_icon_Wrap_Assassin.png'}

        