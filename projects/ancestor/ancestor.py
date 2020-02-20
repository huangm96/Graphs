
def earliest_ancestor(ancestors, starting_node):
    # directed acycle tree
    # find relationship, get node's parents
    # return the path, if no parent is found.

    # create a dic to store the parents for each node.
    nodes_dic = {}
    for item in ancestors:
        if item[1] not in nodes_dic:
            nodes_dic[item[1]] = {item[0]}
        else:
            nodes_dic[item[1]].add(item[0])
    if starting_node not in nodes_dic:
        # if starting_node is not in the dic which means it has no parent
        return - 1
    else:
        stack = [[starting_node]]
        # create a dict to store the olest_ancestor for all possible paths
        oldest_ancestors = {}

        # while stack list is not empty
        while len(stack) > 0:
            # get the last path from the list
            path = stack.pop()

            # get the last element from the path
            path_last = path[-1]
            # if the last element is in the dic, means it has older generation, keep finding
            if path_last in nodes_dic:
                for item in nodes_dic[path_last]:
                    new_path = path.copy()
                    new_path.append(item)
                    stack.append(new_path)
            # not in the dic, means no older generation, add to the oldest_ancestors list
            else:
                if len(path) not in oldest_ancestors:
                    oldest_ancestors[len(path)]={path_last}
                else:
                    oldest_ancestors[len(path)].add(path_last)
        print(oldest_ancestors)
        # older generation means longer path, so find the longest path in the dic
        # if there is more than 1 item in the longest path, find the min number.
        return min(oldest_ancestors[max(oldest_ancestors)])
                
        
    
    
