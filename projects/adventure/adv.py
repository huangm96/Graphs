from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
using dfs to reach the depthest room which has non-unexplored neighbor
from this depthest room, use bfs to find the first room that has unexplored neighbor
use dfs to go to the end
use bfs to go back 
repeat until the explored room num reach the num of the room


'''
# dfs
# Create an empty stack
stack=[]
# Add A PATH TO the starting vertex_id to the stack
stack.append(world.starting_room)
print("herr", stack)
# Create an empty set to store visited nodes
visited = set()
# While the stack is not empty...
while len(stack) > 0:
    # pop, the first room
    room = stack.pop()
    # Check if it's been visited
    # If it has not been visited...
    if room.name not in visited:
        # Mark it as visited
        visited.add(room.name)
        # check if its neighbors have been visited
        # if not, go to one of the directions
        print(visited)
        if room.n_to and room.n_to.name not in visited:
            traversal_path.append("n")
            stack.append(room.n_to)
        elif room.s_to and room.s_to.name not in visited:
            traversal_path.append("s")
            stack.append(room.s_to)
        elif room.w_to and room.w_to.name not in visited:
            traversal_path.append("w")
            stack.append(room.w_to)
        elif room.e_to and room.e_to.name not in visited:
            traversal_path.append("e")
            stack.append(room.e_to)
        
        else:
            # if all neighbors have been visited, we use bfs to find the first room that has explored neighbor
            #
            print("end")
        


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
