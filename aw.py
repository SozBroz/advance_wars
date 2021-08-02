#!/usr/bin/env python
from aw_movement import fetch_movement_data
from aw_units import fetch_unit_attributes_data, 
from aw_class import player, fetch_unit_damage_data, controlled_unit, controllable_structure, controllable_co
from random import randint
#damage calculator
#f = [(b * s / 100) + r] * a/10 * (200 - (d + dtr * hp)) / 100
#f = Final damage 
#b = base damage
#s = strength modifier of CO
#d = defense modifier of CO
#r = random damage roll
#a = HP of attacker
#dtr = terrain Defense rating
#t = [(b * s / d) * (a * .1)]
#h = hp lost by defender
BASE_DAMAGE_TABLE = fetch_unit_damage_data()
MASTER_UNIT_TABLE = fetch_unit_attributes_data()
def battle(unit1, unit2, co1, co2):
	#unit one attacks unit 2
	damage_first_way = damage_calculator(unit1, unit2, co1, co2)
	if co1.name == "Sasha" and co1.in_super_power:
		co1.player.gold+= MASTER_UNITS[unit.name]["Cost"] * self.co1.amplifier["cost"] * min(damage_second_way, unit2.hp) / 10
	unit2.hp = max(0, unit1.hp - damage_first_way)
	#check if unit two can fireback
	damage_second_way = damage_calculator(unit2, unit1, co2, co1)
	unit1.hp = max(0, unit1.hp - damage_second_way)

	#calculate the new starpowers
	if not (co1.in_power or co1.in_super_power):
		co1.star_power = min((co1.star_power + MASTER_UNITS[unit.name]["Cost"] * self.co2.amplifier["cost"] * damage_first_way / 10) * 0.5 + (MASTER_UNITS[unit.name]["Cost"] * self.co1.amplifier["cost"] * damage_second_way / 10), player.stars_super_power * (1 + 0.2 * self.num_of_power_used) * 9000)  

	#check for sashas super co power
	

def damage_calculator(unit1, unit2, co1, co2):
	defense_modifier_type_check = 1 #If it's flying we ignore the terrain for defense
	if MASTER_UNIT_TABLE[unit1.name]["Movement Type"] == "Air":
		defense_modifier_type_check = 0
	
	final_damage = ((BASE_DAMAGE_TABLE[unit1.name][unit2.name] * co1.strength_modifier(unit1)) / 100 + (randint(co1.random_low, co1.random_high)) / 100) * unit1.hp / 10 * (200 - (co2.defense_modifier(unit1) + board[unit2.coords].defense_modifier * defense_modifier_type_check + unit2.hp)) / 200
	return final_damage

#map
#r = road
#p = plain
#w = wood
#m = moutain
#R = river
#b = bridge
#s = shoal
#S = sea
#e = reef
#c = city
#f = factory
#a = airport
#h = harbor
#H = HQ
#C = Comm towers

