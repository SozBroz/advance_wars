#!/usr/bin/python3
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

def fetch_picture_symbol_dict():
	global terrain_chart
	terrain_chart_dict = {}
	for i, line in enumerate(terrain_chart.split("\n")):
		if i == 0:
			continue

		broken_up_line = line.split("\t")
		for index, entry in enumerate(broken_up_line):
			broken_up_line[index] = entry.strip()

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
		
	print(terrain_chart_dict)
	return terrain_chart_dict

fetch_picture_symbol_dict()