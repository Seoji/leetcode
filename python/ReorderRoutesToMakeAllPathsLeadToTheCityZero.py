# Runtime: 909ms
# Memory: 49.73MB

from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Perform depth-first search to count reorders starting from node u.
        def dfs(node):
            visited[node] = True  # Mark the current node as visited.
            count = 0  # Initialize the reorder count.

            # Iterate over connected nodes of the current node.
            for connected_node in adjacency_list[node]:
                if not visited[connected_node]:
                    # If the edge from the current node to the connected node is in
                    # the original direction, increase the reorder count.
                    if (node, connected_node) in directed_edges:
                        count += 1
                    # Add the result of recursively calling dfs on the connected node.
                    count += dfs(connected_node)
            return count

        # Create an adjacency list and a set to store directed edges.
        adjacency_list = defaultdict(list)
        directed_edges = set()

        # Populate the adjacency list and directed edges set.
        for a, b in connections:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
            directed_edges.add((a, b))

        # Initialize a list to keep track of visited nodes.
        visited = [False] * n

        # Start the depth-first search from node 0 and return the reorder count.
        return dfs(0)


# my solution
# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # edge_cnt_dict = {0:0}
        # edge_cnt_key_cnt = 1
        # result = 0

        # connections = deque(connections)

        # while connections:
        #     connection = connections.popleft()

        #     # if not connection[0] in edge_cnt_dict and not connection[1] in edge_cnt_dict:
                
        #     #     continue

        #     if connection[0] in edge_cnt_dict and connection[1] not in edge_cnt_dict:
        #         edge_cnt_dict[connection[1]] = edge_cnt_dict[connection[0]] + 1
        #         result += 1
        #         continue

        #     if connection[1] in edge_cnt_dict and connection[0] not in edge_cnt_dict:
        #         edge_cnt_dict[connection[0]] = edge_cnt_dict[connection[1]] + 1
        #         continue
            
        #     connections.append(connection)

        # while edge_cnt_key_cnt != n:
        #     temp = []
        #     for connection in connections:
        #         if not connection[0] in edge_cnt_dict and not connection[1] in edge_cnt_dict:
        #             temp.append(connection)
        #             continue

        #         if connection[0] in edge_cnt_dict and connection[1] not in edge_cnt_dict:
        #             edge_cnt_dict[connection[1]] = edge_cnt_dict[connection[0]] + 1
        #             edge_cnt_key_cnt += 1
        #             if edge_cnt_dict[connection[0]] < edge_cnt_dict[connection[1]]:
        #                 result += 1
        #             continue

        #         if connection[1] in edge_cnt_dict and connection[0] not in edge_cnt_dict:
        #             edge_cnt_dict[connection[0]] = edge_cnt_dict[connection[1]] + 1
        #             edge_cnt_key_cnt += 1
        #             continue
                
        #     connections = temp
        # print(edge_cnt_dict)
        # return result
