# Tarefa 1 - A*
# Inteligencia artificial 2021.1 - CEFET MG - Belo Horizonte
# Nomes: 
#   Leonardo Leite Meira - 20183005069
#   Rafael Silvério de Sá - 20183012994

from a_star import a_star_search
from enum import Enum
import math

cities = Enum('cities', 'Arad, Bucareste, Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, RimnicuVilcea, Sibiu, Timisoara, Urziceni, Vaslui, Zerind')


graph = {
    cities.Arad: {
        "name": cities.Arad,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 366,
        "children": {
            cities.Zerind:
            {
                "distance": 75
            },
            cities.Timisoara:
            {
                "distance": 118
            },
            cities.Sibiu:
            {
                "distance": 140
            }
        }
    },
    cities.Bucareste: {
        "name": cities.Bucareste,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 0,
        "children": {
            cities.Giurgiu:
            {

                "distance": 90
            },
            cities.Urziceni:
            {

                "distance": 85
            },
            cities.Fagaras:
            {

                "distance": 211
            },
            cities.Pitesti:
            {

                "distance": 101
            }
        }
    },
    cities.Craiova: {
        "name": cities.Craiova,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 160,
        "children": {
            cities.Pitesti:
            {

                "distance": 138
            },
            cities.RimnicuVilcea:
            {

                "distance": 146
            },
            cities.Drobeta:
            {

                "distance": 120
            },
        }
    },
    cities.Drobeta: {
        "name": cities.Drobeta,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 242,
        "children": {
            cities.Mehadia:
            {

                "distance": 75
            },
            cities.Craiova:
            {

                "distance": 120
            },
        }
    },
    cities.Eforie: {
        "name": cities.Eforie,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 161,
        "children": {
            cities.Hirsova:
            {

                "distance": 86
            }
        }
    },
    cities.Fagaras: {
        "name": cities.Fagaras,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 176,
        "children": {
            cities.Sibiu:
            {

                "distance": 99
            },
            cities.Bucareste:
            {

                "distance": 211
            },
        }
    },
    cities.Giurgiu: {
        "name": cities.Giurgiu,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 77,
        "children": {
            cities.Bucareste:
            {

                "distance": 90
            }
        }
    },
    cities.Hirsova: {
        "name": cities.Hirsova,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 151,
        "children": {
            cities.Urziceni:
            {

                "distance": 98
            },
            cities.Eforie:
            {

                "distance": 86
            }
        }
    },
    cities.Iasi: {
        "name": cities.Iasi,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 226,
        "children": {
            cities.Neamt:
            {

                "distance": 87
            },
            cities.Vaslui:
            {

                "distance": 92
            }
        }
    },
    cities.Lugoj: {
        "name": cities.Lugoj,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 244,
        "children": {
            cities.Mehadia:
            {

                "distance": 70
            },
            cities.Timisoara:
            {

                "distance": 11
            }
        }
    },
    cities.Mehadia: {
        "name": cities.Mehadia,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 241,
        "children": {
            cities.Lugoj:
            {

                "distance": 70
            },
            cities.Drobeta:
            {

                "distance": 75
            }
        }
    },
    cities.Neamt: {
        "name": cities.Neamt,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 234,
        "children": {
            cities.Iasi:
            {

                "distance": 87
            }
        }
    },
    cities.Oradea: {
        "name": cities.Oradea,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 380,
        "children": {
            cities.Zerind:
            {

                "distance": 71
            },
            cities.Sibiu:
            {

                "distance": 151
            }
        }
    },
    cities.Pitesti: {
        "name": cities.Pitesti,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 100,
        "children": {
            cities.RimnicuVilcea:
            {

                "distance": 97
            },
            cities.Craiova:
            {

                "distance": 138
            },
            cities.Bucareste:
            {

                "distance": 101
            },
        }
    },
    cities.RimnicuVilcea: {
        "name": cities.RimnicuVilcea,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 193,
        "children": {
            cities.Pitesti:
            {

                "distance": 97
            },
            cities.Sibiu:
            {

                "distance": 80
            },
            cities.Craiova:
            {

                "distance": 146
            },
        }
    },
    cities.Sibiu: {
        "name": cities.Sibiu,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 253,
        "children": {
            cities.Oradea:
            {

                "distance": 151
            },
            cities.Fagaras:
            {

                "distance": 99
            },
            cities.RimnicuVilcea:
            {

                "distance": 80
            },
            cities.Arad:
            {

                "distance": 140
            },
        }
    },
    cities.Timisoara: {
        "name": cities.Timisoara,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 329,
        "children": {
            cities.Arad:
            {

                "distance": 118
            },
            cities.Lugoj:
            {

                "distance": 111
            }
        }
    },
    cities.Urziceni: {
        "name": cities.Urziceni,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 80,
        "children": {
            cities.Vaslui:
            {
                "distance": 142
            },
            cities.Hirsova:
            {
                "distance": 98
            },
            cities.Bucareste:
            {
                "distance": 85
            }
        }
    },
    cities.Vaslui: {
        "name": cities.Vaslui,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 199,
        "children": {
            cities.Iasi:
            {
                "distance": 92
            },
            cities.Urziceni:
            {
                "distance": 142
            }
        }
    },
    cities.Zerind: {
        "name": cities.Zerind,
        "parent": None,
        "f": math.inf,
        "g": 0,
        "h": 374,
        "children": {
            cities.Oradea:
            {
                "distance": 71
            },
            cities.Arad:
            {
                "distance": 75
            }
        }
    },
}

# print(graph[cities.Zerind]["h"])

a_star_search(graph, graph[cities.Arad], graph[cities.Bucareste])
