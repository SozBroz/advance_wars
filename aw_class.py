#!/usr/bin/env python

class player:
	def __init__(self, color, co, team, automated):
		self.color = color
		self.co = co
		self.team = team
		self.units = []
		self.structures = []
		self.gold = []
		self.units_that_can_move = []
		self.structures_that_can_build = []
		self.automated = automated

	def init_map(self, board):
		for unit in board.units:
			if unit.color == self.color:
				self.units.append(unit)

		for structure in board.structures:
			if structure.color == self.color:
				self.structures.append(structure)

	def repair(self, unit, restored_hp):
		unit.health+= min(restored_hp, 10)
		self.gold-= restored_hp * MASTER_UNITS[unit.name]["Cost"] * self.co.amplifier["cost"] / 10

	def refuel(self, unit):
		unit.fuel = MASTER_UNITS[unit.name]["Fuel"]
		unit.ammo = MASTER_UNITS[unit.name]["Ammo"]

	def start_turn(self):
		print("Starting turn")
		#Income
		for structure in structures:
			self.gold += structure.income * global_amplifier["income"] * self.co.amplifier["income"]

		#Repair, refuel and initialize
		for unit in self.units:
			#Structure Repair and refuel
			for structure in self.structures:
				if strcture.can_repair and structure.coords == unit.coords:
					self.refuel(unit)
					if unit.unit.health < 10:
						restored_hp = max(2 * self.co.amplifier["repair"], ((unit.cost * self.co.amplifier["cost"] / 10) * 2 * self.co.amplifier["repair"]))
						self.repair(unit, restored_hp)

			if unit.name == "APC":
				for other_unit in self.units:
					if adjacent(unit.coords, other_unit.coords):
						self.repair(other_unit)

			if unit.stunned == False:
				unit.cooldown-= 1
				self.units_that_can_move.append(unit)

		for structure in self.structures:
			if self.can_build(structure):
				self.structures_that_can_build.append(structure)

	def can_move(self, unit):
		if unit.can_move:
			return True

	def can_build(self, structure):
		if self.structure.can_build == False:
			return False

		for unit in self.units:
			if unit.coords == structure.coords:
				return False 

		return True

	def your_turn(self):
		#power / units
		selection = -1
		while selection != 99:
			if player.co.super_power_can_be_used():
				if input("Activate super power?") == "y":
					player.co.super_power_activate()

			if player.co.power_can_be_used():
				if input("Activate power?") == "y":
					player.co.power_activate()

			for number, unit in enumerate(self.units_that_can_move):
				print(number, ": ", unit.status)

			selection = input("which unit?")
			if selection >= 0 and selection < len(self.units_that_can_move):
				for number, option in enumerate(self.units_that_can_move[selection].options):
					print(number, ": ", option)

			selection2 = input("which option?")
			if selection2 >= 0 and selection2 < len(self.units_that_can_move[selection].options):
				unit.action = self.units_that_can_move[selection].option(selection2)

		selection = -1

		#production
		while selection != 99:
			for number, structure in enumerate(self.structures_that_can_build):
				print(number, ": ", structure.status)

			selection = input("which structure?")
			if selection >= 0 and selection < len(self.structures_that_can_build):
				for number, option in enumerate(self.structures_that_can_build[selection].options):
					print(number, ": ", option)

			selection2 = input("which option?")
			if selection2 >= 0 and selection2 < len(self.structures_that_can_build[selection].options):
				unit.action = self.structures_that_can_build[selection].option(selection2)

		print("Turn over")

	def automated_turn(self):
		raise not_implemented_error

	def full_turn(self):
		self.start_turn()

		if self.automated == False:
			self.your_turn()
		else:
			self.automated_turn()

class controlled_unit:
	def __init__(self, name, color, coordinates, index, cooldown = 1, hp = 10):
		self.coordinates = coordinates
		self.color = color
		self.name = name
		self.ammo = MASTER_UNITS[name]["Ammo"]
		self.fuel = MASTER_UNITS[name]["Fuel"]
		self.vision = MASTER_UNITS[name]["Vision"]
		self.cooldown = cooldown
		self.hp = hp
		self.option_list = []

	def direct_health_manipulation(self, amount):
		self.hp += amount

	def option(self, option):
		#attempt to move, shoot
		self.cooldown+=1

	def options(self):
		#return a list of potential options
		option_list = []

		#determine base movement, apply modifiers
		#Read map to determine movement options
		#Determine what you can attack
			#calculate damage ranges
		#if infantry Determine what you can capture
		#if indirect determine if you can shoot anything before moving
		

		raise not_implemented_error

	def status(self):
		print(self.coordinates, self.color, self.name, self.ammo, self.fuel, self.cooldown, self.fuel)

	def can_move(self):
		if self.cooldown == 0:
			return True

		return False


class controllable_structure:
	def __init__(self, name, color, coords, player):
		self.name = name
		self.color = color
		self.coords = coords
		self.player = player

class controllable_co:
	def __init__(self, name, player):
		self.name = name
		self.random_low = 0
		self.random_high = 10
		self.num_of_power_used = 0
		self.stars_power = 5
		self.stars_super_power = 9
		self.star_power = 0
		self.in_power = False
		self.in_super_power = False
		self.player = player
		self.amplifier = {"repair": 1, "cost": 1, "income": 1,
		"direct_movement_flat_modifier": 0}
		if self.name == "Sasha":
			self.amplifier["income"] = 1.1
			self.star_power = 2
			self.star_super_power = 6

	def defense_modifier(self, unit):
		power = 1
		if self.in_power or self.in_super_power:
			power+= 0.1
		
		return 1.0

	def offense_modifier(self, unit):
		power = 1.0
		if self.in_power or self.in_super_power:
			power+= 0.1

		if self.name == "Hawke":
			power+= 0.1

		elif self.name == "Max":
			#Todo
			#Indirects have -1 range
			if is_direct_unit(unit):
				power+= 0.2
			elif is_indirect(unit):
				power-= 0.1
			
			if self.in_power:
				#Todo
				#Direct Combat units gain +1 movement
				if is_direct_unit(unit):
					power+= 0.1

			elif self.in_super_power:
				#Todo
				#Direct Combat units gain +2 movement
				if is_direct_unit(unit):
					power+= 0.3
				
		return power

	def power_activate(self):
		if self.name == "Hawke":
			for unit in self.player.units:
				unit.direct_health_manipulation(unit, 1)

			for player in self.player.oponents:
				for unit in self.player.units:
					unit.direct_health_manipulation(unit, -1)

		elif self.name == "Sasha":
			for player in self.player.oponents:
				player.star_power-= min(0, self.player.stars_super_power * (1 + 0.2 * self.num_of_power_used) * self.co.player.gold / 5000)

		self.in_power = True
		self.num_of_power_used+= 1
		self.star_power-= self.player.stars_power * (1 + 0.2 * self.num_of_power_used) * 9000

	def super_power_activate(self):
		if self.name == "Hawke":
			for unit in self.player.units:
				unit.direct_health_manipulation(unit, 2)

			for player in self.player.oponents:
				for unit in self.player.units:
					unit.direct_health_manipulation(unit, -2)

		elif self.name == "Sasha":
			pass #implemented under the battle calculations

		elif self.name == "Max":
			pass #implemented under offense amplifier

		self.in_super_power = True
		self.num_of_power_used +=1
		self.star_power = 0

	def super_power_can_be_used(self):
		if self.star_power > self.player.stars_super_power * (1 + 0.2 * self.num_of_power_used) * 9000:
			return True

		return False

	def power_can_be_used(self):
		if self.star_power > self.player.stars_power * (1 + 0.2 * self.num_of_power_used) * 9000:
			return True

		return False
			


def adjacent(center_coords, target_coords):
	if center_coords.x == target_coords.x:
		if center_coords.y == target_coords.y - 1 or center_coords.y == target_coords.y - 1:
			return true

	if center_coords.y == target_coords.y:
		if center_coords.x == target_coords.x - 1 or center_coords.x == target_coords.x - 1:
			return true

	return false

def is_direct_unit(unit):
	if MASTER_UNITS[unit.name]["Range"] == 1 and MASTER_UNITS[unit.name]["Name"] != "Mech" and MASTER_UNITS[unit.name]["Name"] != "Infantry":
		return True

	return False

def is_indirect_unit(unit):
	if MASTER_UNITS[unit.name]["Range"] != 1:
		return True

	return False
