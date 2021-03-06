import random
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # Create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle the list
        random.shuffle(possible_friendships)

        # Grab the first total_friendship pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        # avg_friendships = total_friendships /num_users
        # total_friendships = avg_friendships * num_users
        # N = total_friendships //2
        
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # add a path to the queue list
        q = [[user_id]]
        # While the queue is not empty...
        while len(q) > 0:
            # get the first path
            path = q.pop(0)
            # get the last element from the path
            path_last = path[-1]
            
            if path_last not in visited:
                visited[path_last] = path
                # add the friends of the user to the new path
                for neighbor in self.friendships[path_last]:
                    new_path = path.copy()
                    new_path.append(neighbor)
                    # add to queue
                    q.append(new_path)


        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)

    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)


    #Q1 
    # nums = num_users * avg_friendships // 2
    nums = 100 * 10 // 2
    print(f"Times would you need to call add_friendship(): {nums}")

    # Q2
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    connections = sg.get_all_social_paths(1)
    print(len(connections))
    total = 0
    for connection in connections:
        total += len(connections[connection])
    print(total / len(connections) - 1)
