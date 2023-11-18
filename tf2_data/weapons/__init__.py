import json

## IMPORT AND ADD CLASS INTO THIS FILE
from .scout_weapons import ScoutWeapons
from .soldier_weapons import SoldierWeapons
from .pyro_weapons import PyroWeapons
from .demoman_weapons import DemomanWeapons
from .heavy_weapons import HeavyWeapons
from .engineer_weapons import EngineerWeapons
from .medic_weapons import MedicWeapons
from .sniper_weapons import SniperWeapons
from .spy_weapons import SpyWeapons
from .global_weapons import GlobalWeapons

## all weapons iterates through weapon models and adds each return to the result list
ALL_WEAPON_CLASSES = {
  "scout": ScoutWeapons,
  "soldier": SoldierWeapons,
  "pyro": PyroWeapons,
  "demoman": DemomanWeapons,
  "heavy": HeavyWeapons,
  "engineer": EngineerWeapons,
  "medic": MedicWeapons,
  "sniper": SniperWeapons,
  "spy": SpyWeapons,
  "global": GlobalWeapons,
  }

def allWeapons():
    return list(ALL_WEAPON_CLASSES.keys())

ALL_WEAPON_CLASSES["all"] = allWeapons()
