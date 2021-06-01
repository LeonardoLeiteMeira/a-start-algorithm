from enum import Enum
print("Hello world")

cities = Enum('cities','Arad,Bucareste,Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Lasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, RimnicuVilcea, Sibiu, Timisoara, Urziceni, Vaslui, Zerind')
cities.Drobeta

graph = {
	cities.Arad :{
		"h":366,
		"children":[{
			"name":cities.Zerind,
			"distance":75
		},
		{
			"name":cities.Timisoara,
			"distance":118
		},
		{
			"name":cities.Sibiu,
			"distance":140
		}]
	},
	cities.Bucareste: {
		"h":0,
		"children":[
			{
				"name":cities.Giurgiu,
				"distance":90
			},
			{
				"name":cities.Urziceni,
				"distance":85
			},
			{
				"name":cities.Fagaras,
				"distance":211
			},
			{
				"name":cities.Pitesti,
				"distance":101
			}
		]
	},
	cities.Craiova: {
		"h":160,
		"children":[
			{
				"name":cities.Pitesti,
				"distance":138
			},
			{
				"name":cities.RimnicuVilcea,
				"distance":146
			},
			{
				"name":cities.Drobeta,
				"distance":120
			},
		]
	},
	cities.Drobeta: {
		"h":242,
		"children":[
			{
				"name":cities.Mehadia,
				"distance":75
			},
			{
				"name":cities.Craiova,
				"distance":120
			},
		]
	},
	cities.Eforie: {
		"h":161,
		"children":[
			{
				"name":cities.Hirsova,
				"distance":86
			}
		]
	},
	cities.Fagaras: {
		"h":176,
		"children":[
			{
				"name":cities.Sibiu,
				"distance":99
			},
			{
				"name":cities.Bucareste,
				"distance":211
			},
		]
	},
	cities.Giurgiu: {
		"h":77,
		"children":[
			{
				"name":cities.Bucareste,
				"distance":90
			}
		]
	},
	cities.Hirsova: {
		"h":151,
		"children":[]
	},
	cities.Lasi: {
		"h":226,
		"children":[]
	},
	cities.Lugoj: {
		"h":244,
		"children":[]
	},
	cities.Mehadia: {
		"h":241,
		"children":[]
	},
	cities.Neamt: {
		"h":234,
		"children":[]
	},
	cities.Oradea: {
		"h":380,
		"children":[]
	},
	cities.Pitesti: {
		"h":100,
		"children":[]
	},
	cities.RimnicuVilcea: {
		"h":193,
		"children":[]
	},
	cities.Sibiu: {
		"h":253,
		"children":[]
	},
	cities.Timisoara: {
		"h":329,
		"children":[]
	},
	cities.Urziceni: {
		"h":80,
		"children":[]
	},
	cities.Vaslui: {
		"h":199,
		"children":[]
	},
	cities.Zerind: {
		"h":374,
		"children":[]
	},
}

print(graph[cities.Zerind]["h"])

