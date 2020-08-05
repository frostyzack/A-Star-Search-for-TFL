import urllib.request
import json
import math
from TubeMap import Tube_map

# A* Search helper functions
# G Score getter between nodes
def api_get_duration_between_nodes(start_node, end_node):
    # Get endpoint for line data between two stations using their ics codes
    endpoint = str('https://api.tfl.gov.uk/journey/journeyresults/' + str(start_node.getIcsCode()) + '/to/' + str(
        end_node.getIcsCode()))
    response = urllib.request.urlopen(endpoint).read()
    json_obj = str(response, 'utf-8')
    # Get the json data in pythonic form
    data = json.loads(json_obj)
    # Return the value of the duration for the journey between both stations based on next incoming train
    return data['journeys'][0]['duration']

def eucledian_heuristic(start_node, destination_node):
    # Start_node node here is the current_node node for which you are finding the eucledian distance heuristic
    eucledian = ((start_node.getLatitude() + start_node.getLongitude()) ** 2 + (
                destination_node.getLatitude() + destination_node.getLongitude()) ** 2) ** 0.5
    return eucledian

def find_lowest_f_score(f_scores, visited_nodes):
    lowest_f_score_node = None
    # currently all f scores are of infinity value
    lowest_f_score_value = math.inf
    for node in visited_nodes:
        value = f_scores[node]  # value of that node's f score
        if value < lowest_f_score_value:
            # update to new lowest f score
            lowest_f_score_value = value
            # make that node the one with the lowest f score
            lowest_f_score_node = node
            # return that node with lowest f score
    return lowest_f_score_node

def reconstruct_path(path_came_from, current_node):
    total_path = [current_node]  # add current_node to total path
    while current_node in path_came_from.keys():
        current_node = path_came_from[current_node]
        total_path.append(current_node)
    total_path.reverse()
    named_path = []
    for i in total_path:
        named_path.append(i.getName())
    return named_path


# The A* Search Function
def a_star_search(start_node, destination_node, graph):
    closed_set = set()
    open_set = {start_node}
    came_from = dict()

    g_score = {v: math.inf for v in list(graph.keys())}
    g_score[start_node] = 0

    f_score = {v: math.inf for v in list(graph.keys())}
    f_score[start_node] = 1

    while open_set:
        current_node = find_lowest_f_score(f_score, open_set)
        if current_node == destination_node:
            return reconstruct_path(came_from, current_node)

        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbour in graph[current_node]:
            if neighbour in closed_set:
                continue
            if neighbour not in open_set:
                open_set.add(neighbour)
            tentative_g_score = g_score[current_node] + api_get_duration_between_nodes(current_node, neighbour)
            if tentative_g_score >= g_score[neighbour]:
                continue  # not a better path

            came_from[neighbour] = current_node
            g_score[neighbour] = tentative_g_score
            f_score[neighbour] = g_score[neighbour] + eucledian_heuristic(neighbour, destination_node)

Search = a_star_search(Tube_map.dgeware_road, Tube_map.south_kensington, Tube_map)
print(Search)