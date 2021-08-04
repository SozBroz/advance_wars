#!/usr/bin/python3
import pygame
import sys
import csv
from image_index import fetch_picture_symbol_dict, fetch_terrain_symbol_dict, fetch_movement_dict, fetch_unit_pictures_dict, fetch_unit_dict
from aw_movement import fetch_movement_data
from aw_units import fetch_unit_attributes_data, fetch_unit_damage_data
from aw_class import player, controlled_unit, controllable_structure, controllable_co
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

picture_symbol_dict = fetch_picture_symbol_dict()
terrain_symbol_dict = fetch_terrain_symbol_dict()
unit_symbol_dict = fetch_unit_pictures_dict()
unit_dict = fetch_unit_dict()
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

class Map:
	def __init__(self, map_location):
		self.fetch_raw_map(map_location)
		self.xy = (len(self.raw_map), len(self.raw_map[1]))
		self.map_layout_for_units()
		self.initialize_units_lists(map_location.split("/")[1].split(".")[0])
		self.set_ownership_of_color(map_location.split("/")[1].split(".")[0])

	def fetch_raw_map(self, file_path):
		with open(file_path) as csvfile:
			map_dump_raw = csvfile.readlines()

		for index,line in enumerate(map_dump_raw):
			map_dump_raw[index] = line.strip().split(",")
		
		self.raw_map = map_dump_raw

	def map_layout_for_units(self):
		processed_map = []
		for x in range(0,self.xy[0]):
			processed_map.append([])
			for y in range(0,self.xy[1]):
				processed_map[x].append(terrain_symbol_dict[self.raw_map[x][y]])

		self.processed_map = processed_map

	def visualize(self):
		pygame.init()
		surface = pygame.display.set_mode((900,900))
		self.active_unit_list = []
		for x in range(0,self.xy[0]):
			for y in range(0,self.xy[1]):
				surface.blit(picture_symbol_dict[self.raw_map[x][y]], (y*32,x*32))

		for unit in self.p1_list:
			surface.blit(unit_symbol_dict["p1"][unit[0]], (unit[1]*64, unit[2]*64))

		for unit in self.p2_list:
			self.active_unit_list.append(surface.blit(unit_symbol_dict["p2"][unit[0]], (unit[1]*32, unit[2]*32)))			

		pygame.display.flip()

	def on_board(self, xy):
		if xy[0] >= 0 and xy[0] < self.xy[0] and xy[1] >= 0 and xy[1] < self.xy[1]:
			return True

		return False

	def initialize_units_lists(self, map_name):
		self.p1_list = [] 
		self.p2_list = [] 
		if map_name == "alovesupreme":
			self.p2_list.append(["Infantry",0,16])
			#Insert
		

	def set_ownership_of_color(self, map_name):
		self.tileset = {"p1":{}, "p2":{}, "Grey Sky": {}, "Pink Cosmos": {}}
		self.tileset["Grey Sky"]["HQ"] = '90'
		self.tileset["Grey Sky"]["Com Tower"] = '137'
		self.tileset["Grey Sky"]["Lab"] = '143'
		self.tileset["Grey Sky"]["City"] = '86'
		self.tileset["Grey Sky"]["Base"] = '87'
		self.tileset["Grey Sky"]["Airport"] = '88'
		self.tileset["Grey Sky"]["Port"] = '89'

		self.tileset["Pink Cosmos"]["HQ"] = '160'
		self.tileset["Pink Cosmos"]["Com Tower"] = '159'
		self.tileset["Pink Cosmos"]["Lab"] = '161'
		self.tileset["Pink Cosmos"]["City"] = '158'
		self.tileset["Pink Cosmos"]["Base"] = '157'
		self.tileset["Pink Cosmos"]["Airport"] = '163'
		self.tileset["Pink Cosmos"]["Port"] = '162'

		if map_name == "alovesupreme":
			self.tileset["p1"] = self.tileset["Grey Sky"]
			self.tileset["p2"] = self.tileset["Pink Cosmos"]

		
infantry_movement = 3



board = Map("maps/alovesupreme.map")
print(board.raw_map)
print(board.processed_map)
print(board.xy)
board.visualize()
while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			for unit in board.active_unit_list:
				if unit.collide_point(pos):
					print("hi")
input()
