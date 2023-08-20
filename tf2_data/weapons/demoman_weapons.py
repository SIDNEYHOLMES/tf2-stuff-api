from flask import url_for

class DemomanWeapons:
    
    def grenade_launcher():
        return {"name": "Grenade Launcher", 'class': 'demoman', 'type': 'Stock', 'image': '/w/images/thumb/e/e6/Item_icon_Grenade_Launcher.png/100px-Item_icon_Grenade_Launcher.png'}

    def loch_n_load():
        return {"name": "Loch-n-Load", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/6/62/Item_icon_Loch-n-Load.png/100px-Item_icon_Loch-n-Load.png'}

    def ali_babas_wee_booties():
        return {"name": "Ali Baba's Wee Booties", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/a/a4/Item_icon_Ali_Baba%27s_Wee_Booties.png/100px-Item_icon_Ali_Baba%27s_Wee_Booties.png'}

    def bootlegger():
        return {"name": "Bootlegger", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/4/4c/Item_icon_Bootlegger.png/100px-Item_icon_Bootlegger.png'}

    def loose_cannon():
        return {"name": "Loose Cannon", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/7/70/Item_icon_Loose_Cannon.png/100px-Item_icon_Loose_Cannon.png'}

    def base_jumper():
        return {"name": "B.A.S.E. Jumper", 'class': ['soldier', 'demoman'], 'type': 'Craft', 'image': '/w/images/thumb/b/b2/Item_icon_B.A.S.E._Jumper.png/100px-Item_icon_B.A.S.E._Jumper.png'}

    def iron_bomber():
        return {"name": "Iron Bomber", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/c/cd/Item_icon_Iron_Bomber.png/100px-Item_icon_Iron_Bomber.png'}

    def stickybomb_launcher():
        return {"name": "Stickybomb Launcher", 'class': 'demoman', 'type': 'Stock', 'image': '/w/images/thumb/7/7c/Item_icon_Stickybomb_Launcher.png/100px-Item_icon_Stickybomb_Launcher.png'}

    def scottish_resistance():
        return {"name": "Scottish Resistance", 'class': 'demoman', 'type': 'Unlock', 'image': '/w/images/thumb/2/2c/Item_icon_Scottish_Resistance.png/100px-Item_icon_Scottish_Resistance.png'}

    def chargin_targe():
        return {"name": "Chargin' Targe", 'class': 'demoman', 'type': 'Unlock', 'image': '/w/images/thumb/7/7a/Item_icon_Chargin%27_Targe.png/100px-Item_icon_Chargin%27_Targe.png'}

    def sticky_jumper():
        return {"name": "Sticky Jumper", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/5/56/Item_icon_Sticky_Jumper.png/100px-Item_icon_Sticky_Jumper.png'}

    def splendid_screen():
        return {"name": "Splendid Screen", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/c/c3/Item_icon_Splendid_Screen.png/100px-Item_icon_Splendid_Screen.png'}

    def tide_turner():
        return {"name": "Tide Turner", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/c/cd/Item_icon_Tide_Turner.png/100px-Item_icon_Tide_Turner.png'}

    def quickiebomb_launcher():
        return {"name": "Quickiebomb Launcher", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/f/f9/Item_icon_Quickiebomb_Launcher.png/100px-Item_icon_Quickiebomb_Launcher.png'}

    def bottle():
        return {"name": "Bottle", 'class': 'demoman', 'type': 'Stock', 'image': '/w/images/thumb/b/b2/Item_icon_Bottle.png/100px-Item_icon_Bottle.png'}

    def scottish_handshake():
        return {"name": "Scottish Handshake", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/1/1a/Item_icon_Scottish_Handshake.png/100px-Item_icon_Scottish_Handshake.png'}

    def eyelander():
        return {"name": "Eyelander", 'class': 'demoman', 'type': 'Unlock', 'image': '/w/images/thumb/9/94/Item_icon_Eyelander.png/100px-Item_icon_Eyelander.png'}

    def horseless_headless_horsemanns_headtaker():
        return {"name": "Horseless Headless Horsemann's Headtaker", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/1/1f/Item_icon_Horseless_Headless_Horsemann%27s_Headtaker.png/100px-Item_icon_Horseless_Headless_Horsemann%27s_Headtaker.png'}

    def nessies_nine_iron():
        return {"name": "Nessie's Nine Iron", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/5/5a/Item_icon_Nessie%27s_Nine_Iron.png/100px-Item_icon_Nessie%27s_Nine_Iron.png'}

    def scotsmans_skullcutter():
        return {"name": "Scotsman's Skullcutter", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/c/c6/Item_icon_Scotsman%27s_Skullcutter.png/100px-Item_icon_Scotsman%27s_Skullcutter.png'}

    def pain_train():
        return {"name": "Pain Train", 'class': ['soldier', 'demoman'], 'type': 'Craft', 'image': '/w/images/thumb/4/4b/Item_icon_Pain_Train.png/100px-Item_icon_Pain_Train.png'}

    def ullapool_caber():
        return {"name": "Ullapool Caber", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/a/a5/Item_icon_Ullapool_Caber.png/100px-Item_icon_Ullapool_Caber.png'}

    def claidheamh_mòr():
        return {"name": "Claidheamh Mòr", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/0/0f/Item_icon_Claidheamh_M%C3%B2r.png/100px-Item_icon_Claidheamh_M%C3%B2r.png'}

    def half_zatoichi():
        return {"name": "Half-Zatoichi", 'class': ['soldier', 'demoman'], 'type': 'Promotional', 'image': '/w/images/thumb/a/a9/Item_icon_Half-Zatoichi.png/100px-Item_icon_Half-Zatoichi.png'}

    def persian_persuader():
        return {"name": "Persian Persuader", 'class': 'demoman', 'type': 'Craft', 'image': '/w/images/thumb/9/98/Item_icon_Persian_Persuader.png/100px-Item_icon_Persian_Persuader.png'}