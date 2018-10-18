"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        '''
        add a vertex to the class. it takes in a vertex id and creates an instanc of the vertex class.
        '''
        self.vertices[vertex_id] = Vertex(vertex_id)
    def add_edge(self, v1, v2):
        '''
        add and undirected edge to the class
        '''
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].edges.add(v2)
            self.vertices[v2].edges.add(v1)
        else:
            raise IndexError("That vertex does not exist")

    
class Vertex:
    def __init__(self, vertex_id, x = None, y= None):
        self.id = vertex_id
        self.edges = set()  
    def __repr__(self):
        return f"{self.edges}"

