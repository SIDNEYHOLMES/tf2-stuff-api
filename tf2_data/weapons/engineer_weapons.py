from flask import url_for

class EngineerWeapons:
  
  def shotgun():
      return {"name": "Shotgun", 'class': ['soldier', 'pyro', 'heavy', 'engineer'], 'type': 'Stock', 'image': '/w/images/thumb/5/5f/Item_icon_Shotgun.png/100px-Item_icon_Shotgun.png'}

  def frontier_justice():
      return {"name": "Frontier Justice", 'class': 'engineer', 'type': 'Unlock', 'image': '/w/images/thumb/2/26/Item_icon_Frontier_Justice.png/100px-Item_icon_Frontier_Justice.png'}

  def widowmaker():
      return {"name": "Widowmaker", 'class': 'engineer', 'type': 'Promotional', 'image': '/w/images/thumb/b/b8/Item_icon_Widowmaker.png/100px-Item_icon_Widowmaker.png'}

  def pomson_6000():
      return {"name": "Pomson 6000", 'class': 'engineer', 'type': 'Craft', 'image': '/w/images/thumb/8/89/Item_icon_Pomson_6000.png/100px-Item_icon_Pomson_6000.png'}

  def rescue_ranger():
      return {"name": "Rescue Ranger", 'class': 'engineer', 'type': 'Craft', 'image': '/w/images/thumb/2/29/Item_icon_Rescue_Ranger.png/100px-Item_icon_Rescue_Ranger.png'}

  def panic_attack():
      return {"name": "Panic Attack", 'class': ['soldier', 'pyro', 'heavy', 'engineer'], 'type': 'Craft', 'image': '/w/images/thumb/b/be/Item_icon_Panic_Attack.png/100px-Item_icon_Panic_Attack.png'}

  def pistol():
      return {"name": "Pistol", 'class': ['scout', 'engineer'], 'type': 'Stock', 'image': '/w/images/thumb/5/52/Item_icon_Pistol.png/100px-Item_icon_Pistol.png'}

  def lugermorph():
      return {"name": "Lugermorph", 'class': ['scout', 'engineer'], 'type': 'Promotional', 'image': '/w/images/thumb/8/86/Item_icon_Lugermorph.png/100px-Item_icon_Lugermorph.png'}

  def capper():
      return {"name": "C.A.P.P.E.R", 'class': ['scout', 'engineer'], 'type': 'Uncrate', 'image': '/w/images/thumb/a/a6/Item_icon_C.A.P.P.E.R.png/100px-Item_icon_C.A.P.P.E.R.png'}

  def wrangler():
      return {"name": "Wrangler", 'class': 'engineer', 'type': 'Unlock', 'image': '/w/images/thumb/c/ce/Item_icon_Wrangler.png/100px-Item_icon_Wrangler.png'}

  def giger_counter():
      return {"name": "Giger Counter", 'class': 'engineer', 'type': 'Uncrate', 'image': '/w/images/thumb/5/5d/Item_icon_Giger_Counter.png/100px-Item_icon_Giger_Counter.png'}

  def short_circuit():
      return {"name": "Short Circuit", 'class': 'engineer', 'type': 'Promotional', 'image': '/w/images/thumb/3/36/Item_icon_Short_Circuit.png/100px-Item_icon_Short_Circuit.png'}

  def wrench():
      return {"name": "Wrench", 'class': 'engineer', 'type': 'Stock', 'image': '/w/images/thumb/7/7d/Item_icon_Wrench.png/100px-Item_icon_Wrench.png'}

  def golden_wrench():
      return {"name": "Golden Wrench", 'class': 'engineer', 'type': 'Distributed', 'image': '/w/images/thumb/9/95/Item_icon_Golden_Wrench.png/100px-Item_icon_Golden_Wrench.png'}

  def gunslinger():
      return {"name": "Gunslinger", 'class': 'engineer', 'type': 'Unlock', 'image': '/w/images/thumb/c/ca/Item_icon_Gunslinger.png/100px-Item_icon_Gunslinger.png'}

  def southern_hospitality():
      return {"name": "Southern Hospitality", 'class': 'engineer', 'type': 'Craft', 'image': '/w/images/thumb/e/ec/Item_icon_Southern_Hospitality.png/100px-Item_icon_Southern_Hospitality.png'}

  def jag():
      return {"name": "Jag", 'class': 'engineer', 'type': 'Craft', 'image': '/w/images/thumb/4/49/Item_icon_Jag.png/100px-Item_icon_Jag.png'}

  def eureka_effect():
      return {"name": "Eureka Effect", 'class': 'engineer', 'type': 'Craft', 'image': '/w/images/thumb/c/cf/Item_icon_Eureka_Effect.png/100px-Item_icon_Eureka_Effect.png'}

  def pda():
      return {"name": "PDA", 'class': 'engineer', 'type': 'StockPDA 1', 'image': '/w/images/thumb/1/16/Item_icon_PDA_Build.png/100px-Item_icon_PDA_Build.png'}

  def pda():
      return {"name": "PDA", 'class': 'engineer', 'type': 'StockPDA 2', 'image': '/w/images/thumb/2/26/Item_icon_PDA_Destroy.png/100px-Item_icon_PDA_Destroy.png'}
