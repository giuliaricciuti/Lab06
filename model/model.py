import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()

    def creaGrafo(self, anno, metodo, s):
        self._graph.clear()
        self._idMapProducts = {}
        self._products = DAO.getAllProducts(anno, metodo)
        for p in self._products:
            self._idMapProducts[p.Product_number] = p
        self._graph.add_nodes_from(self._products)
        self.addEdges(s)

    def addEdges(self, s):
        for n in self._graph.nodes:
            for n1 in self._graph.nodes:
                if n!=n1 and ((n1.tot_vendite/n.tot_vendite)>=(1+s)):
                    self._graph.add_edge(n, n1)

    def getRedditizi(self):
        self._products.sort(key = lambda x: x.tot_vendite)
        redditizi = []
        for n in self._graph.nodes:
            if len(self._graph.out_edges(n))==0:
                redditizi.append((n, len(self._graph.in_edges(n))))
        return redditizi[:5]


    def getMethods(self):
        return DAO.getAllMethods()

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()