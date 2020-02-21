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
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/Michael_test.txt"
map_file = "maps/main_maze.txt"

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
# Add the starting room to the stack
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
    if room not in visited:
        # Mark it as visited
        print("stack",room.name)
        visited.add(room)
        # check if its neighbors have been visited
        # if not, go to one of the directions
    if room.n_to and room.n_to not in visited:
        traversal_path.append("n")
        stack.append(room.n_to)
    elif room.s_to and room.s_to not in visited:
        traversal_path.append("s")
        stack.append(room.s_to)
    elif room.w_to and room.w_to not in visited:
        traversal_path.append("w")
        stack.append(room.w_to)
    elif room.e_to and room.e_to not in visited:
        traversal_path.append("e")
        stack.append(room.e_to)
    
    elif len(visited) == len(room_graph):
        break

    else:
        # if all neighbors have been visited, use bfs to find the first room that has explored neighbor
        # dfs
        # Create an empty queue
        queue = []
        # Add the room(which has non-unexplored neighbor) TO the queue as the starting point of the path
        queue.append(room)
        paths = [[]]
        # While the stack is not empty...
        while len(queue) > 0:
            # pop, the first room
            visited_room = queue.pop(0)
            path = paths.pop(0)
            # check this visited_room to see if it has unexplored neighbor
            if (visited_room.n_to and visited_room.n_to not in visited) or (visited_room.s_to and visited_room.s_to not in visited) or (visited_room.w_to and visited_room.w_to not in visited) or (visited_room.e_to and visited_room.e_to not in visited):
                print("queue", visited_room.name)
                queue.clear()
                print(len(queue))
                traversal_path.extend(path)
                print(path)
                stack.append(visited_room)
            else:
                
                # add neighbor to the queue
                if visited_room.n_to:
                    new_path = path.copy()
                    new_path.append("n")
                    paths.append(new_path)
                    queue.append(visited_room.n_to)
                if visited_room.s_to:
                    new_path = path.copy()
                    new_path.append("s")
                    paths.append(new_path)
                    queue.append(visited_room.s_to)
                if visited_room.w_to:
                    new_path = path.copy()
                    new_path.append("w")
                    paths.append(new_path)
                    queue.append(visited_room.w_to)
                if visited_room.e_to:
                    new_path = path.copy()
                    new_path.append("e")
                    paths.append(new_path)
                    queue.append(visited_room.e_to)
            
  
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
