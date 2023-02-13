class Graph:

    """A graph connects nodes by edges.  Each edge can also
    have a length associated with it.  The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C.  You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more edges with g.connect('B', 'C', 3), then
    inverse link is also added.  You can use g.get_nodes() to get a list of nodes,
    g.get_edges('A') to get a dict of edges out of A, and g.get_distance('A', 'B') to get the
    length of the edge from A to B. """

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.add_connection(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.add_connection(A, B, distance)
        if not self.directed:
            self.add_connection(B, A, distance)

    def add_connection(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get_edges(self, a):
        return self.graph_dict.setdefault(a, {})

    def get_distance(self, a, b):
        links = self.graph_dict.setdefault(a, {})
        return links.get(b)

    def get_nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


def UndirectedGraph(graph_dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(graph_dict = graph_dict, directed=False)


class GraphProblem():

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def goal_test(self, state):
        """Return True if the state is the goal. """
        return state == self.goal

    def get_actions_from(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get_edges(A).keys())

    def get_path_cost(self, A, B):
        return self.graph.get_distance(A, B)


class Node:
    """A node in a search tree."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        pass


    def create_child_node(self, problem, action):
        # create a child node that is generated by the given action
        return None

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        # create a list with nodes that can be expanded form this node
        # first get all actions and then create the successor nodes
        return None

    def get_path_from_root(self):
        """Return a list of nodes forming the path from the root to this node."""
        # Hint: use self.parent to create the list of nodes back to the root and reverse it
        return None

    def get_solution(self):
        """Return the sequence of actions to go from the root to this node."""
        # Hint: use the self.get_path_from_root() function
        return None


