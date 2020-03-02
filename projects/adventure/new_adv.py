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
room_graph = literal_eval(open(map_file, "r").read())
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
stack = []
# Add the starting room to the stack
stack.append(world.starting_room)
print("start", stack)
# Create an empty set to store visited nodes
visited = dict()
# While the stack is not empty...
while len(stack) > 0:
    # pop, the first room
    room = stack.pop()
    # Check if it's been visited
    # If it has not been visited...
    if room.id not in visited:
        # Mark it as visited
        print("stack", room.name)
        visited[room.id] = dict()
        if room.w_to is not None:
            visited[room.id]["w"] = "?"
        if room.n_to is not None:
            visited[room.id]["n"] = "?"
        if room.s_to is not None:
            visited[room.id]["s"] = "?"
        if room.e_to is not None:
            visited[room.id]["e"] = "?"
        # check if its neighbors have been visited
        # if not, go to one of the directions
    if room.w_to and visited[room.id]["w"] == "?":
        traversal_path.append("w")
        stack.append(room.w_to)
        visited[room.id]["w"] = room.w_to.id
        if room.w_to.id not in visited:
            visited[room.w_to.id] = dict()
            if room.w_to.w_to is not None:
                visited[room.w_to.id]["w"] = "?"
            if room.w_to.n_to is not None:
                visited[room.w_to.id]["n"] = "?"
            if room.w_to.s_to is not None:
                visited[room.w_to.id]["s"] = "?"
            if room.w_to.e_to is not None:
                visited[room.w_to.id]["e"] = "?"
            visited[room.w_to.id]["e"] = room.id
        else:
            visited[room.w_to.id]["e"] = room.id
            
    elif room.s_to and visited[room.id]["s"] == "?":
        
        traversal_path.append("s")
        stack.append(room.s_to)
        visited[room.id]["s"] = room.s_to.id
        if room.s_to.id not in visited:
            visited[room.s_to.id] = dict()
            if room.s_to.w_to is not None:
                visited[room.s_to.id]["w"] = "?"
            if room.s_to.n_to is not None:
                visited[room.s_to.id]["n"] = "?"
            if room.s_to.s_to is not None:
                visited[room.s_to.id]["s"] = "?"
            if room.s_to.e_to is not None:
                visited[room.s_to.id]["e"] = "?"
            visited[room.s_to.id]["n"] = room.id
        else:
            visited[room.s_to.id]["n"] = room.id

    elif room.n_to and visited[room.id]["n"] == "?":

        traversal_path.append("n")
        stack.append(room.n_to)
        visited[room.id]["n"] = room.n_to.id
        
        if room.n_to.id not in visited:
            visited[room.n_to.id] = dict()
            if room.n_to.w_to is not None:
                visited[room.n_to.id]["w"] = "?"
            if room.n_to.n_to is not None:
                visited[room.n_to.id]["n"] = "?"
            if room.n_to.s_to is not None:
                visited[room.n_to.id]["s"] = "?"
            if room.n_to.e_to is not None:
                visited[room.n_to.id]["e"] = "?"
            visited[room.n_to.id]["s"] = room.id
        else:
            visited[room.n_to.id]["s"] = room.id
    elif room.e_to and visited[room.id]["e"] == "?":

        traversal_path.append("e")
        stack.append(room.e_to)
        visited[room.id]["e"] = room.e_to.id

        if room.e_to.id not in visited:
            visited[room.e_to.id] = dict()
            if room.e_to.w_to is not None:
                visited[room.e_to.id]["w"] = "?"
            if room.e_to.n_to is not None:
                visited[room.e_to.id]["n"] = "?"
            if room.e_to.s_to is not None:
                visited[room.e_to.id]["s"] = "?"
            if room.e_to.e_to is not None:
                visited[room.e_to.id]["e"] = "?"
            visited[room.e_to.id]["w"] = room.id
        else:
            visited[room.e_to.id]["w"] = room.id

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
            if (visited_room.n_to and visited[visited_room.id]["n"] == '?') or (visited_room.s_to and visited[visited_room.id]["s"] == '?') or (visited_room.w_to and visited[visited_room.id]["w"] == '?') or (visited_room.e_to and visited[visited_room.id]["e"] == '?'):
                print("queue", visited_room.name)
                queue.clear()
                traversal_path.extend(path)
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
print(visited)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
print("traversal_path", traversal_path)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
