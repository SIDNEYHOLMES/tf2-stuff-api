from flask import url_for

class SoldierWeapons:
    
    def rocket_launcher():
        return {"name": "Rocket Launcher", 'class': 'soldier', 'type': 'Stock', 'image': '/w/images/thumb/f/fe/Item_icon_Rocket_Launcher.png/100px-Item_icon_Rocket_Launcher.png'}

    def original():
        return {"name": "Original", 'class': 'soldier', 'type': 'Promotional', 'image': '/w/images/thumb/8/88/Item_icon_Original.png/100px-Item_icon_Original.png'}

    def direct_hit():
        return {"name": "Direct Hit", 'class': 'soldier', 'type': 'Unlock', 'image': '/w/images/thumb/e/e7/Item_icon_Direct_Hit.png/100px-Item_icon_Direct_Hit.png'}

    def black_box():
        return {"name": "Black Box", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/d/d2/Item_icon_Black_Box.png/100px-Item_icon_Black_Box.png'}

    def rocket_jumper():
        return {"name": "Rocket Jumper", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/5/53/Item_icon_Rocket_Jumper.png/100px-Item_icon_Rocket_Jumper.png'}

    def liberty_launcher():
        return {"name": "Liberty Launcher", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/2/24/Item_icon_Liberty_Launcher.png/100px-Item_icon_Liberty_Launcher.png'}

    def cow_mangler_5000():
        return {"name": "Cow Mangler 5000", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/4/46/Item_icon_Cow_Mangler_5000.png/100px-Item_icon_Cow_Mangler_5000.png'}

    def beggars_bazooka():
        return {"name": "Beggar's Bazooka", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/7/77/Item_icon_Beggar%27s_Bazooka.png/100px-Item_icon_Beggar%27s_Bazooka.png'}

    def air_strike():
        return {"name": "Air Strike", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/f/f8/Item_icon_Air_Strike.png/100px-Item_icon_Air_Strike.png'}

    def shotgun():
        return {"name": "Shotgun", 'class': ['soldier', 'pyro', 'heavy', 'engineer'], 'type': 'Stock', 'image': '/w/images/thumb/5/5f/Item_icon_Shotgun.png/100px-Item_icon_Shotgun.png'}

    def reserve_shooter():
        return {"name": "Reserve Shooter", 'class': ['soldier', 'pyro'], 'type': 'Craft', 'image': '/w/images/thumb/3/34/Item_icon_Reserve_Shooter.png/100px-Item_icon_Reserve_Shooter.png'}

    def buff_banner():
        return {"name": "Buff Banner", 'class': 'soldier', 'type': 'Unlock', 'image': '/w/images/thumb/7/7c/Item_icon_Buff_Banner.png/100px-Item_icon_Buff_Banner.png'}

    def gunboats():
        return {"name": "Gunboats", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/0/0c/Item_icon_Gunboats.png/100px-Item_icon_Gunboats.png'}

    def battalions_backup():
        return {"name": "Battalion's Backup", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/d/d8/Item_icon_Battalion%27s_Backup.png/100px-Item_icon_Battalion%27s_Backup.png'}

    def concheror():
        return {"name": "Concheror", 'class': 'soldier', 'type': 'Promotional', 'image': '/w/images/thumb/7/7e/Item_icon_Concheror.png/100px-Item_icon_Concheror.png'}

    def mantreads():
        return {"name": "Mantreads", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/6/6a/Item_icon_Mantreads.png/100px-Item_icon_Mantreads.png'}

    def righteous_bison():
        return {"name": "Righteous Bison", 'class': 'soldier', 'type': 'Promotional', 'image': '/w/images/thumb/1/1d/Item_icon_Righteous_Bison.png/100px-Item_icon_Righteous_Bison.png'}

    def base_jumper():
        return {"name": "B.A.S.E. Jumper", 'class': ['soldier', 'demoman'], 'type': 'Craft', 'image': '/w/images/thumb/b/b2/Item_icon_B.A.S.E._Jumper.png/100px-Item_icon_B.A.S.E._Jumper.png'}

    def panic_attack():
        return {"name": "Panic Attack", 'class': ['soldier', 'pyro', 'heavy', 'engineer'], 'type': 'Craft', 'image': '/w/images/thumb/b/be/Item_icon_Panic_Attack.png/100px-Item_icon_Panic_Attack.png'}

    def shovel():
        return {"name": "Shovel", 'class': 'soldier', 'type': 'Stock', 'image': '/w/images/thumb/7/73/Item_icon_Shovel.png/100px-Item_icon_Shovel.png'}

    def equalizer():
        return {"name": "Equalizer", 'class': 'soldier', 'type': 'Unlock', 'image': '/w/images/thumb/b/ba/Item_icon_Equalizer.png/100px-Item_icon_Equalizer.png'}

    def pain_train():
        return {"name": "Pain Train", 'class': ['soldier', 'demoman'], 'type': 'Craft', 'image': '/w/images/thumb/4/4b/Item_icon_Pain_Train.png/100px-Item_icon_Pain_Train.png'}

    def half_zatoichi():
        return {"name": "Half-Zatoichi", 'class': ['soldier', 'demoman'], 'type': 'Promotional', 'image': '/w/images/thumb/a/a9/Item_icon_Half-Zatoichi.png/100px-Item_icon_Half-Zatoichi.png'}

    def disciplinary_action():
        return {"name": "Disciplinary Action", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/c/cf/Item_icon_Disciplinary_Action.png/100px-Item_icon_Disciplinary_Action.png'}

    def market_gardener():
        return {"name": "Market Gardener", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/a/ac/Item_icon_Market_Gardener.png/100px-Item_icon_Market_Gardener.png'}

    def escape_plan():
        return {"name": "Escape Plan", 'class': 'soldier', 'type': 'Craft', 'image': '/w/images/thumb/0/0c/Item_icon_Escape_Plan.png/100px-Item_icon_Escape_Plan.png'}
