#!/usr/bin/env python
unit_text_dump = """																				
	45	50	50	120	-	-	120	75	-	-	65	105	-	10	105	1	55	5	25	60	55	75	-	120	25
	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	75	70	75	-	40	55	-	-	45	65	-	90	55	45	85	15	80	40	70	80	80	-	60	-	70
	25	60	65	65	25	25	-	-	25	55	-	75	25	25	75	10	65	20	55	55	65	-	25	95	55
	85	80	80	-	50	95	-	-	60	95	-	95	95	55	90	25	90	50	80	90	85	-	95	-	80
	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	95	105	105	-	75	95	-	-	75	85	-	110	95	95	110	35	105	90	105	105	105	-	95	-	105
	-	-	-	115	-	-	120	100	-	-	100	-	-	-	-	-	-	-	-	-	-	100	-	115	-
	-	-	-	115	-	25	120	65	5	-	55	-	-	-	-	-	-	-	-	-	-	100	90	115	-
	-	-	-	100	-	-	120	100	-	-	55	-	-	-	-	-	-	-	-	-	-	85	-	100	-
	5	14	15	7	-	-	-	-	-	-	-	55	-	1	45	1	26	1	5	12	25	-	-	30	5
	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	105	105	105	12	10	35	-	-	10	45	-	105	35	55	95	25	105	45	85	105	105	-	10	45	85
	65	75	70	9	-	-	-	-	-	-	-	65	-	15	55	5	85	15	55	85	85	-	-	35	55
	195	195	195	22	45	105	-	-	45	65	-	135	75	125	125	65	195	115	180	195	195	-	45	55	180
	-	-	-	120	-	-	120	100	-	-	100	-	-	-	-	-	-	-	-	-	-	100	-	120	-
	115	125	115	22	15	40	-	-	15	50	-	125	50	75	115	35	125	55	105	125	125	-	15	55	105
	85	80	80	105	55	60	120	75	60	85	65	95	60	55	90	25	90	50	80	90	85	75	85	105	80
	4	45	45	12	-	-	-	-	-	-	-	70	-	1	65	1	28	1	6	35	55	-	-	35	6
	85	80	80	-	55	60	-	-	60	85	-	95	60	55	90	25	90	50	80	90	85	-	85	-	80
	50	85	75	85	45	65	120	70	45	35	45	90	65	70	90	15	85	60	80	85	85	55	55	95	75
	-	-	-	-	55	95	-	-	75	25	-	-	95	-	-	-	-	-	-	-	-	-	55	-	-
	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-	-
	65	75	70	10	1	10	-	-	1	5	-	75	10	15	70	10	85	15	55	85	85	-	1	40	55"""

headers_land = """
Unit	Icon	MP	Ammo	Fuel	Vision	Range	Movement Type	Cost	Built From
Anti-Air	GEAnti-air.gif	6	9	60	2	1	Treads	8000	GEBaseAW2.gif
APC	GEApc.gif	6	-	70	1	0	Treads	5000	GEBaseAW2.gif
Artillery	GEArtillery.gif	5	9	50	1	2-3	Treads	6000	GEBaseAW2.gif
Infantry	GEInfantry.gif	3	-	99	2	1	Foot	1000	GEBaseAW2.gif
Md.Tank	GEMd-tank.gif	5	8	50	1	1	Treads	16000	GEBaseAW2.gif
Mech	GEMech.gif	2	3	70	2	1	Boots	3000	GEBaseAW2.gif
Mega Tank	GEMegatank.gif	4	3	50	1	1	Treads	28000	GEBaseAW2.gif
Missile	GEMissile.gif	4	6	50	5	3-5	Tires	12000	GEBaseAW2.gif
Neotank	GENeotank.gif	6	9	99	1	1	Treads	22000	GEBaseAW2.gif
Piperunner	GEPiperunner.gif	9	9	99	4	2-5	Pipe	20000	GEBaseAW2.gif
Recon	GERecon.gif	8	-	80	5	1	Tires	4000	GEBaseAW2.gif
Rocket	GERocket.gif	5	6	50	1	3-5	Tires	15000	GEBaseAW2.gif
Tank	GETank.gif	6	9	70	3	1	Treads	7000	GEBaseAW2.gif"""

headers_air = """
Unit	Icon	MP	Ammo	Fuel	Vision	Range	Movement Type	Cost	Built From
B-Copter	GEB-copter.gif	6	6	99	3	1	Air	9000	GEAirportAW2.gif
Black Bomb	GEBlackbomb.gif	9	-	45	1	0	Air	25000	GEAirportAW2.gif
Bomber	GEBomber.gif	7	9	99	2	1	Air	22000	GEAirportAW2.gif
Fighter	GEFighter.gif	9	9	99	2	1	Air	20000	GEAirportAW2.gif
Stealth	GEStealth.gif	6	6	60	4	1	Air	24000	GEAirportAW2.gif
T-Copter	Get-copter.gif	6	-	99	2	0	Air	5000	GEAirportAW2.gif"""

headers_sea = """
Unit	Icon	MP	Ammo	Fuel	Vision	Range	Movement Type	Cost	Built From
Battleship	GEBattleship.gif	5	9	99	2	2-6	Sea	28000	GEPortAW2.gif
Black Boat	GEBlackboat.gif	7	-	60	1	0	Lander	7500	GEPortAW2.gif
Carrier	GECarrier.gif	5	9	99	4	3-8	Sea	30000	GEPortAW2.gif
Cruiser	GECruiser.gif	6	9	99	3	1	Sea	18000	GEPortAW2.gif
Lander	GELander.gif	6	-	99	1	0	Lander	12000	GEPortAW2.gif
Sub	GESub.gif	5	6	60	5	1	Sea	20000	GEPortAW2.gif"""

def unit_list():
	air_units = headers_air.split("\n")
	sea_units = headers_sea.split("\n")
	land_units = headers_land.split("\n")
	units_dict = []
	for air_unit in air_units[2:]:
		units_dict.append(air_unit.split("\t")[0])
	for sea_unit in sea_units[2:]:	
		units_dict.append(sea_unit.split("\t")[0])
	for land_unit in land_units[2:]:
		units_dict.append(land_unit.split("\t")[0])

	return units_dict

def fetch_unit_attributes_data():
	headers = "Unit	Icon	MP	Ammo	Fuel	Vision	Range	Movement Type	Cost	Built From"
	headers = headers.split("\t")
	air_units = headers_air.split("\n")
	sea_units = headers_sea.split("\n")
	land_units = headers_land.split("\n")
	units_dict = {}
	for air_unit in air_units[2:]:
		units_dict[air_unit.split("\t")[0]] = {}
		for counter, i in enumerate(air_unit.split("\t")[1:]):
			units_dict[air_unit.split("\t")[0]][headers[counter+1]] = i

	for sea_unit in sea_units[2:]:
		units_dict[sea_unit.split("\t")[0]] = {}
		for counter, i in enumerate(sea_unit.split("\t")[1:]):
			units_dict[sea_unit.split("\t")[0]][headers[counter+1]] = i

	for land_unit in land_units[2:]:
		units_dict[land_unit.split("\t")[0]] = {}
		for counter, i in enumerate(land_unit.split("\t")[1:]):
			units_dict[land_unit.split("\t")[0]][headers[counter+1]] = i

	return units_dict

def fetch_unit_damage_data():
	table_data = unit_text_dump.split("\n")
	table_header = ['Anti-Air', 'APC', 'Artillery', 'B-Copter', 'Battleship', 'Black Boat', 'Black Bomb', 
	'Bomber', 'Carrier',  'Cruiser', 'Fighter', 'Infantry', 'Lander', 'Md.Tank', 'Mech',
	'Mega Tank', 'Missile', 'Neotank', 'Piperunner', 'Recon', 'Rocket',  'Stealth', 'Sub', 'T-Copter', 'Tank']
	table_dict = {}
	for counter, name in enumerate(table_header):
		table_dict[name] = {}
		for counter2, name2 in enumerate(table_header):
			table_dict[name][name2] = table_data[counter + 1].split("\t")[counter2 + 1]

	return table_dict

if __name__ == "__main__":
	print(unit_list())
	print(fetch_unit_attributes_data())
	print(fetch_unit_damage_data())
		
