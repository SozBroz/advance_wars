#!/usr/bin/python3
import pygame
symbols = """	1	.	Plain
	2	^	Mountain
	3	@	Wood
	4	{	HRiver
	5	}	VRiver
	6	~	CRiver
	7	I	ESRiver
	8	J	SWRiver
	9	K	WNRiver
	10	L	NERiver
	11	M	ESWRiver
	12	N	SWNRiver
	13	O	WNERiver
	14	P	NESRiver
	15	-	HRoad
	16	=	VRoad
	17	+	CRoad
	18	A	ESRoad
	19	B	SWRoad
	20	C	WNRoad
	21	D	NERoad
	22	E	ESWRoad
	23	F	SWNRoad
	24	G	WNERoad
	25	H	NESRoad
	26	[	HBridge
	27	]	VBridge
	28	,	Sea
	29	<	HShoal
	30	(	HShoalN
	31	>	VShoal
	32	)	VShoalE
	33	%	Reef
	34	a	Neutral City
	35	b	Neutral Base
	36	c	Neutral Airport
	37	d	Neutral Port
	38	e	Orange Star City
	39	f	Orange Star Base
	40	g	Orange Star Airport
	41	h	Orange Star Port
	42	i	Orange Star HQ
	43	j	Blue Moon City
	44	l	Blue Moon Base
	45	m	Blue Moon Airport
	46	n	Blue Moon Port
	47	o	Blue Moon HQ
	48	p	Green Earth City
	49	q	Green Earth Base
	50	r	Green Earth Airport
	51	s	Green Earth Port
	52	t	Green Earth HQ
	53	u	Yellow Comet City
	54	v	Yellow Comet Base
	55	w	Yellow Comet Airport
	56	x	Yellow Comet Port
	57	y	Yellow Comet HQ
	81	U	Red Fire City
	82	T	Red Fire Base
	83	S	Red Fire Airport
	84	R	Red Fire Port
	85	Q	Red Fire HQ
	86	Z	Grey Sky City
	87	Y	Grey Sky Base
	88	X	Grey Sky Airport
	89	W	Grey Sky Port
	90	V	Grey Sky HQ
	91	1	Black Hole City
	92	2	Black Hole Base
	93	3	Black Hole Airport
	94	4	Black Hole Port
	95	5	Black Hole HQ
	96		Brown Desert City
	97		Brown Desert Base
	98		Brown Desert Airport
	99		Brown Desert Port
	100		Brown Desert HQ
	101	k	VPipe
	102	z	HPipe
	103	!	NEPipe
	104	#	ESPipe
	105	$	SWPipe
	106	&	WNPipe
	107	*	NPipe End
	108	|	EPipe End
	109	\`	SPipe End
	110	'	WPipe End
	111	"	Missile Silo
	112	;	Missile Silo Empty
	113	:	HPipe Seam
	114	?	VPipe Seam
	115	/	HPipe Rubble
	116	0	VPipe Rubble
	117		Amber Blaze Airport
	118		Amber Blaze Base
	119		Amber Blaze City
	120		Amber Blaze HQ
	121		Amber Blaze Port
	122		Jade Sun Airport
	123		Jade Sun Base
	124		Jade Sun City
	125		Jade Sun HQ
	126		Jade Sun Port
	127		Amber Blaze Com Tower
	128		Black Hole Com Tower
	129		Blue Moon Com Tower
	130		Brown Desert Com Tower
	131		Green Earth Com Tower
	132		Jade Sun Com Tower
	133	_	Neutral Com Tower
	134		Orange Star Com Tower
	135		Red Fire Com Tower
	136		Yellow Comet Com Tower
	137		Grey Sky Com Tower
	138		Amber Blaze Lab
	139		Black Hole Lab
	140		Blue Moon Lab
	141		Brown Desert Lab
	142		Green Earth Lab
	143		Grey Sky Lab
	144		Jade Sun Lab
	145	6	Neutral Lab
	146		Orange Star Lab
	147		Red Fire Lab
	148		Yellow Comet Lab
	149		Cobalt Ice Airport
	150		Cobalt Ice Base
	151		Cobalt Ice City
	152		Cobalt Ice Com Tower
	153		Cobalt Ice HQ
	154		Cobalt Ice Lab
	155		Cobalt Ice Port
	156		Pink Cosmos Airport
	157		Pink Cosmos Base
	158		Pink Cosmos City
	159		Pink Cosmos Com Tower
	160		Pink Cosmos HQ
	161		Pink Cosmos Lab
	162		Pink Cosmos Port
	163		Teal Galaxy Airport
	164		Teal Galaxy Base
	165		Teal Galaxy City
	166		Teal Galaxy Com Tower
	167		Teal Galaxy HQ
	168		Teal Galaxy Lab
	169		Teal Galaxy Port
	170		Purple Lightning Airport
	171		Purple Lightning Base
	172		Purple Lightning City
	173		Purple Lightning Com Tower
	174		Purple Lightning HQ
	175		Purple Lightning Lab
	176		Purple Lightning Port
	181		Acid Rain Airport
	182		Acid Rain Base
	183		Acid Rain City
	184		Acid Rain Com Tower
	185		Acid Rain HQ
	186		Acid Rain Lab
	187		Acid Rain Port
	188		White Nova Airport
	189		White Nova Base
	190		White Nova City
	191		White Nova Com Tower
	192		White Nova HQ
	193		White Nova Lab
	194		White Nova Port""".split("\n")

terrain_chart = """Terrain	Defense	F	B	T	W	A	S	L	P	F	B	T	W	A	S	L	P	F	B	T	W	A	S	L	P
	  1  	 1 	 1 	 1 	 2 	 1 	 - 	 - 	 - 	 1 	 1 	 2 	 3 	 1 	 - 	 - 	 - 	 2 	 1 	 2 	 3 	 2 	 - 	 - 	 - 
	  4  	 2 	 1 	 - 	 - 	 1 	 - 	 - 	 - 	 2 	 1 	 - 	 - 	 1 	 - 	 - 	 - 	 4 	 2 	 - 	 - 	 2 	 - 	 - 	 - 
	  2  	 1 	 1 	 2 	 3 	 1 	 - 	 - 	 - 	 1 	 1 	 3 	 4 	 1 	 - 	 - 	 - 	 2 	 1 	 2 	 3 	 2 	 - 	 - 	 - 
	  0  	 2 	 1 	 - 	 - 	 1 	 - 	 - 	 - 	 2 	 1 	 - 	 - 	 1 	 - 	 - 	 - 	 2 	 1 	 - 	 - 	 2 	 - 	 - 	 - 
	  0  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  0  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  0  	 - 	 - 	 - 	 - 	 1 	 1 	 1 	 - 	 - 	 - 	 - 	 - 	 1 	 1 	 1 	 - 	 - 	 - 	 - 	 - 	 2 	 2 	 2 	 - 
	  0  	 1 	 1 	 1 	 1 	 1 	 - 	 1 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 1 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 1 	 - 
	  1  	 - 	 - 	 - 	 - 	 1 	 2 	 2 	 - 	 - 	 - 	 - 	 - 	 1 	 2 	 2 	 - 	 - 	 - 	 - 	 - 	 2 	 2 	 2 	 - 
	  3  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  3  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 1 
	  3  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  3  	 1 	 1 	 1 	 1 	 1 	 1 	 1 	 - 	 1 	 1 	 1 	 1 	 1 	 1 	 1 	 - 	 1 	 1 	 1 	 1 	 2 	 2 	 2 	 - 
	  4  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  0  	 - 	 - 	 - 	 - 	 - 	 - 	 - 	 1 	 - 	 - 	 - 	 - 	 - 	 - 	 - 	 1 	 - 	 - 	 - 	 - 	 - 	 - 	 - 	 1 
	  3  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  3  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - 
	  3  	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 1 	 - 	 - 	 - 	 1 	 1 	 1 	 1 	 2 	 - 	 - 	 - """

terrain_row_names = "Plain,Mountain,Wood,River,Road,Bridge,Sea,Shoal,Reef,City,Base,Airport,Port,HQ,Pipe,Missile,Com Tower,Lab".split(",")

unit_dict = {"Infantry": 0, "Mech": 1, "APC": 2, "Oozium": 3, "Recon": 4, "Tank": 5,
"Md.Tank": 6, "Neotank": 7, "Mega Tank": 8, "Artillery": 9, "Rocket": 10, "Piperunner": 11,
"Missile": 12, "Anti-Air": 13, "T-Copter": 14, "B-Copter": 15, "Fighter": 16, "Bomber": 17,
"Stealth": 18, "Black Bomb": 19, "Black Boat": 20, "Lander": 21, "Cruiser": 22, "Sub": 23,
"Battleship": 24, "Carrier": 25 }

def fetch_unit_dict():
	global unit_dict 
	return unit_dict

def fetch_movement_dict():
	global terrain_chart
	terrain_chart_dict = {}
	for i, line in enumerate(terrain_chart.split("\n")):
		if i == 0:
			continue

		broken_up_line = line.split("\t")
		for index, entry in enumerate(broken_up_line[1:]):
			broken_up_line[index + 1] = entry.strip()
			if "-" in broken_up_line[index + 1]:
				broken_up_line[index + 1] = 9999
			else:
				broken_up_line[index + 1] = int(broken_up_line[index + 1])

		terrain_chart_dict[terrain_row_names[i - 1]] = {"Defense": broken_up_line[1], 
		"Clear":{
		"F":broken_up_line[2],
		"B":broken_up_line[3],
		"T":broken_up_line[4],
		"W":broken_up_line[5],
		"A":broken_up_line[6],
		"S":broken_up_line[7],
		"L":broken_up_line[8],
		"P":broken_up_line[9]},
		"Rain":{
		"F":broken_up_line[10],
		"B":broken_up_line[11],
		"T":broken_up_line[12],
		"W":broken_up_line[13],
		"A":broken_up_line[14],
		"S":broken_up_line[15],
		"L":broken_up_line[16],
		"P":broken_up_line[17]},
		"Snow":{
		"F":broken_up_line[18],
		"B":broken_up_line[19],
		"T":broken_up_line[20],
		"W":broken_up_line[21],
		"A":broken_up_line[22],
		"S":broken_up_line[23],
		"L":broken_up_line[24],
		"P":broken_up_line[25]},
		}
		
	return terrain_chart_dict


def fetch_picture_symbol_dict():
	global symbols
	symbol_dict = {}

	for symbol in symbols:
		name = symbol.split("\t")[3].replace(" ", "").lower() + ".gif"
		representation = pygame.image.load("images/" + name)
		representation = pygame.transform.scale(representation, (32, 32))
		#representation.set_colorkey((0,0,0))

		symbol_dict[symbol.split("\t")[1]] = representation

	return symbol_dict

def fetch_terrain_symbol_dict():
	global terrain_chart
	global symbols
	symbol_dict = {}

	for symbol in symbols:
		for terrain in terrain_row_names:
			if terrain in symbol.split("\t")[3]:
				symbol_dict[symbol.split("\t")[1]] = terrain
				break

	return symbol_dict

def fetch_unit_pictures_dict():
	global unit_dict
	symbol_dict = {"p1": {}, "p2": {}, "p3": {}, "p4": {}}
	for unit in unit_dict:
		representation = pygame.image.load("images/" + "tile" + "%03d" % unit_dict[unit] + ".png")

		symbol_dict["p1"][unit] = representation
		representation = pygame.image.load("images/" + "tile" + "%03d" % (unit_dict[unit] + 26) + ".png")
		representation = pygame.transform.scale(representation, (16, 16))

		symbol_dict["p2"][unit] = representation

		representation = pygame.image.load("images/" + "tile" + "%03d" % (unit_dict[unit] + 26*2) + ".png")
		symbol_dict["p3"][unit] = representation
		representation = pygame.image.load("images/" + "tile" + "%03d" % (unit_dict[unit] + 26*3) + ".png")
		symbol_dict["p4"][unit] = representation

	return symbol_dict

if __name__ == "__main__":
	print(fetch_picture_symbol_dict())
	print(fetch_terrain_symbol_dict())
	print(fetch_movement_dict())
	print(fetch_unit_pictures_dict())

	if len(fetch_picture_symbol_dict()) == len(fetch_terrain_symbol_dict()):
		print("fetch_picture_symbol_dict and fetch_terrain_symbol_dict are synced")
	else:
		print("WARNING!!!!!!!!!!!!!!!\n fetch_picture_symbopassl_dict and fetch_terrain_symbol_dict are NOT synced")