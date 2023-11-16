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
def allWeapons():
  weapon_method_list = [ScoutWeapons, SoldierWeapons, PyroWeapons, DemomanWeapons, HeavyWeapons, EngineerWeapons, MedicWeapons, SniperWeapons, SpyWeapons, GlobalWeapons]
  result_method_list = []
  while (len(result_method_list) < 10):
    curr_weapon = weapon_method_list[len(result_method_list)]
    result_method_list.append(curr_weapon)
  
  # print(result_method_list)
  return result_method_list

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
  "all": allWeapons()
  }
