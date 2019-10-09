from util import Queue


class Graph():
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can not create edge based on given vertices!")

def earliest_ancestor(ancestors, starting_node):
    # ansector_graph = {}
    # for ancestor in ancestors:
    #     ansector_graph[ancestor[1]] = []
    # for ancestor in ancestors:
    #     ansector_graph[ancestor[1]].append(ancestor[0])
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])

    
    # if ansector_graph[starting_node] == [] or starting_node not in ansector_graph:
    #     return -1

    longest_path = []
    
    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if (len(path) >= max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    print(graph.vertices)

    return earliest_ancestor








# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#             [1, 1, 0, 1, 1],
#             [0, 0, 1, 0, 0],
#             [1, 0, 1, 0, 0],
#             [1, 1, 0, 0, 0]]

# islands =  [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#             [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#             [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#             [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#             [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#             [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#             [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#             [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#             [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#             [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# # island_counter(islands) # 1st returns 4 / 2nd returns 13

# def island_counter(islands):
#     # visited cache
#     # count of islands
#     visited = set()
#     island_count = 0
#     q = Queue()
#     for y in range(0, len(islands)):
#         for x in range(0, len(islands[y])):
#             if islands[y][x] == 1 and (y,x) not in visited:
#                 island_count += 1
#                 print([y, x])
#                 q.enqueue([y,x])
#                 visited.add((y,x))
#                 while q.size() > 0:
#                     v = q.dequeue()
#                     y_cord = v[0]
#                     x_cord = v[1]
#                     if y_cord > 0:
#                         if (y_cord-1, x_cord) not in visited and islands[y_cord-1][x_cord] == 1:
#                             visited.add((y_cord-1, x_cord))
#                             q.enqueue([y_cord-1, x_cord])
#                     if y_cord < len(islands)-1:
#                         if (y_cord+1, x_cord) not in visited and islands[y_cord+1][x_cord] == 1:
#                             visited.add((y_cord+1, x_cord))
#                             q.enqueue([y_cord+1, x_cord])
#                     if x_cord < len(islands[y_cord])-1:
#                         if (y_cord, x_cord+1) not in visited and islands[y_cord][x_cord+1] == 1:
#                             visited.add((y_cord, x_cord+1))
#                             q.enqueue([y_cord, x_cord+1])
#                     if x_cord > 0:
#                         if (y_cord, x_cord-1) not in visited and islands[y_cord][x_cord-1] == 1:
#                             visited.add((y_cord, x_cord-1))
#                             q.enqueue([y_cord, x_cord-1])
    
#     return island_count

# print(island_counter(islands))