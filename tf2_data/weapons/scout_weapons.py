from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app)

class ScoutWeapons:
    
    @cache.cached(timeout=600)
    def scattergun():
        return {"name": "scattergun", 'class': 'scout', 'type': 'Stock', 'image': 'localhost:5000/image/class_weapon/scout/scattergun'}

    @cache.cached(timeout=600)
    def force_a_nature():
        return {"name": "force-A-Nature", 'class': 'scout', 'type': 'Unlock', 'image': 'localhost:5000/image/class_weapon/scout/force_a_nature'}

    @cache.cached(timeout=600)
    def shortstop():
        return {"name": "shortstop", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/shortstop'}

    @cache.cached(timeout=600)
    def soda_popper():
        return {"name": "soda popper", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/soda_popper'}

    @cache.cached(timeout=600)
    def baby_faces_blaster():
        return {"name": "baby face's blaster", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/baby_faces_blaster'}

    @cache.cached(timeout=600)
    def back_scatter():
        return {"name": "back scatter", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/back_scatter'}

    @cache.cached(timeout=600)
    def pistol():
        return {"name": "pistol", 'class': ['scout', 'engineer'], 'type': 'Stock', 'image': 'localhost:5000/image/class_weapon/scout/pistol'}

    @cache.cached(timeout=600)
    def lugermorph():
        return {"name": "lugermorph", 'class': ['scout', 'engineer'], 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/lugermorph'}

    @cache.cached(timeout=600)
    def capper():
        return {"name": "c.a.p.p.e.r", 'class': ['scout', 'engineer'], 'type': 'Uncrate', 'image': 'localhost:5000/image/class_weapon/scout/c.a.p.p.e.r'}

    @cache.cached(timeout=600)
    def winger():
        return {"name": "winger", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/winger'}

    @cache.cached(timeout=600)
    def pretty_boys_pocket_pistol():
        return {"name": "pretty boy's pocket pistol", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/pretty_boys_pocket_pistol'}

    @cache.cached(timeout=600)
    def flying_guillotine():
        return {"name": "flying guillotine", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/flying_guillotine'}

    @cache.cached(timeout=600)
    def bonk_atomic_punch():
        return {"name": "bonk! atomic punch", 'class': 'scout', 'type': 'Unlock', 'image': 'localhost:5000/image/class_weapon/scout/bonk_atomic_punch'}

    @cache.cached(timeout=600)
    def crit_a_cola():
        return {"name": "crit-a-cola", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/crit_a_cola'}

    @cache.cached(timeout=600)
    def mad_milk():
        return {"name": "mad milk", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/mad_milk'}

    @cache.cached(timeout=600)
    def mutated_milk():
        return {"name": "mutated milk", 'class': 'scout', 'type': 'Uncrate', 'image': 'localhost:5000/image/class_weapon/scout/mutated_milk'}

    @cache.cached(timeout=600)
    def bat():
        return {"name": "bat", 'class': 'scout', 'type': 'Stock', 'image': 'localhost:5000/image/class_weapon/scout/bat'}

    @cache.cached(timeout=600)
    def holy_mackerel():
        return {"name": "holy mackerel", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/holy_mackerel'}

    @cache.cached(timeout=600)
    def unarmed_combat():
        return {"name": "unarmed combat", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/unarmed_combat'}

    @cache.cached(timeout=600)
    def batsaber():
        return {"name": "batsaber", 'class': 'scout', 'type': 'Uncrate', 'image': 'localhost:5000/image/class_weapon/scout/batsaber'}

    @cache.cached(timeout=600)
    def sandman():
        return {"name": "sandman", 'class': 'scout', 'type': 'Unlock', 'image': 'localhost:5000/image/class_weapon/scout/sandman'}

    @cache.cached(timeout=600)
    def candy_cane():
        return {"name": "candy cane", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/candy_cane'}

    @cache.cached(timeout=600)
    def boston_basher():
        return {"name": "boston basher", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/boston_basher'}

    @cache.cached(timeout=600)
    def three_rune_blade():
        return {"name": "three-rune blade", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/three_rune_blade'}

    @cache.cached(timeout=600)
    def sun_on_a_stick():
        return {"name": "sun-on-a-stick", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/sun_on_a_stick'}

    @cache.cached(timeout=600)
    def fan_owar():
        return {"name": "fan o'war", 'class': 'scout', 'type': 'Promotional', 'image': 'localhost:5000/image/class_weapon/scout/fan_owar'}

    @cache.cached(timeout=600)
    def atomizer():
        return {"name": "atomizer", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/atomizer'}

    @cache.cached(timeout=600)
    def wrap_assassin():
        return {"name": "wrap assassin", 'class': 'scout', 'type': 'Craft', 'image': 'localhost:5000/image/class_weapon/scout/wrap_assassin'}
