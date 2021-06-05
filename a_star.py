import math


def calculateG(parent, child):
    return parent["g"] + parent["children"][child]["distance"]


def isDestination(node, goalNode):
    return node["name"] == goalNode["name"]


def defineLowestF(nodeList):
    lowestF = math.inf
    for node in nodeList:
        if node["f"] < lowestF:
            lowestF = node["f"]

    return lowestF


def pathTracer(node, graph, startingNode):
    path = []

    path.append(graph[node["name"]])

    while node["name"] != startingNode["name"]:
        node = graph[node["parent"]]
        path.append(node)

    return path[::-1]


def printPath(path):
    for node in path:
        print("Nó: " + str(node["name"]) + "\nf: " + str(node["f"]) +
              "\ng: " + str(node["g"]) + "\nh: " + str(node["h"]) + "\n")


def a_star_search(graph, startingNode, goalNode):
    openNodes = []
    closedNodes = []

    graph[startingNode["name"]]["f"] = graph[startingNode["name"]
                                             ]["g"] + graph[startingNode["name"]]["h"]

    openNodes.append(graph[startingNode["name"]])

    while len(openNodes) > 0:
        currentNode = openNodes[0]

        for node in openNodes:
            if node["f"] < currentNode["f"]:
                currentNode = graph[node["name"]]

        openNodes.remove(graph[currentNode["name"]])
        closedNodes.append(graph[currentNode["name"]])

        if isDestination(currentNode, goalNode):
            path = pathTracer(graph[currentNode["name"]],
                              graph, graph[startingNode["name"]])

            printPath(path)
            return

        for child in currentNode["children"]:
            graph[child]["g"] = calculateG(currentNode, child)
            graph[child]["f"] = graph[child]["g"] + graph[child]["h"]

            if graph[child] in openNodes and graph[child]["f"] > defineLowestF(openNodes):
                continue

            if graph[child] in closedNodes and graph[child]["f"] > defineLowestF(openNodes):
                continue

            graph[child]["parent"] = currentNode["name"]
            openNodes.append(graph[child])
