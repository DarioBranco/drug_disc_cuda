import networkx as nx
from neo4j import GraphDatabase


class GraphController:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(
            uri, auth=(user, password), database="Compounds"
        )

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.execute_write(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run(
            "CREATE (a:Greeting) "
            "SET a.message = $message "
            "RETURN a.message + ', from node ' + id(a)",
            message=message,
        )
        return result.single()[0]

    # execute all queries in a file in neo4j
    def execute_queries_in_file(self, file_path):
        with open(file_path, "r") as f:
            query = f.read()
            with self.driver.session() as session:
                session.run(query)

    def execute_queries_in_string(self, stringQuery):
        with self.driver.session() as session:
            session.run(stringQuery)

    def combinations(self, iterable, r, num_iter):
        # combinations('ABCD', 2) --> AB AC AD BC BD CD
        # combinations(range(4), 3) --> 012 013 023 123
        iterazioni_comb = 0
        num10000 = 0
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            iterazioni_comb += 1
            print(
                "Iterazione: "
                + str(num_iter)
                + " combinazioni: "
                + str(num10000)
                + " volte "
                + str(iterazioni_comb)
            )
            if iterazioni_comb == 10000:
                num10000 = num10000 + 1
                iterazioni_comb = 0
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple(pool[i] for i in indices)

    def mat3dtolist(mat):
        lista = []
        percentuale = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for k in range(len(mat[0][0])):
                    if mat[i][j][k] != 0:
                        lista.append(mat[i][j][k])
                    perc = percentuale / (len(mat) * len(mat[0]) * len(mat[0][0])) * 100
                    print(" %2.2f" % (perc) + "%\n")
                    percentuale = percentuale + 1
        return lista

    # funzione che conta il numero di occorrenze(già ottimizzata) in una lista
    def conta_occorrenze_lista(self,lista):
        lista_occorrenze = [[]]
        conta = 0
        conta_cicli = 0
        for e in lista:
            conta = 0
            if e not in lista[0:conta]:
                for j in range(len(lista[0:conta]), len(lista) - 1):
                    GM = nx.algorithms.isomorphism.GraphMatcher(
                        e, lista[j], node_match=lambda n1, n2: True
                    )
                    if GM.is_isomorphic():
                        conta = conta + 1
            perc = conta / len(lista) * 100
            lista_occorrenze.append([e, conta, perc])
            conta_cicli = conta_cicli + 1
            perc2 = conta_cicli / len(lista) * 100
            print(" %2.2f" % (perc2) + "%\n")
        return lista_occorrenze

    def findSubGraphs(
        self, id1, id2, num_iterazione, nodeMatchAttr, raggiomax, deepmax
    ):
        # ritorna la lista di tutti i sottografi comuni fra i due grafi
        # rappresentati da id1 e id2 con attributo di comparazione nodeMatchAttr e edgeMatchAttr
        n = 19
        mat3d = []
        print("\n\n")
        conta_nodi = 1
        conta_iter = 0
        raggio = 0
        num_sottografi_trovati = 0
        query1 = (
            "MATCH (a:Atom)-[b:BOND_WITH]-(d:Atom) MATCH( (c:Compound)-[r:RELATED]->(a:Atom)) WHERE c.idComp='"
            + str(id1)
            + "' RETURN a,b"
        )
        query2 = (
            "MATCH (a:Atom)-[b:BOND_WITH]-(d:Atom) MATCH( (c:Compound)-[r:RELATED]->(a:Atom)) WHERE c.idComp='"
            + str(id2)
            + "' RETURN a,b"
        )

        # results1=cypher.run(query1)
        # results2=cypher.run(query2)

        G1 = self.import_graph_from_neo4j_to_networkx(query1)
        G2 = self.import_graph_from_neo4j_to_networkx(query2)

        numnodes = len(list(G2.nodes()))
        # data=neonx.write_to_neo("http://localhost:7474/db/data",G1,"sottografi_1")
        # data2=neonx.write_to_neo("http://localhost:7474/db/data",G2,"sottografi_2")
        G2 = G2.to_undirected()
        G1 = G1.to_undirected()
        i = 100
        for n in list(G2.nodes):
            SG2 = nx.ego_graph(G2, n, raggiomax, True)
            for deep in range(3, deepmax):
                for SG in (
                    SG2.subgraph(s) for s in self.combinations(SG2, deep, conta_iter)
                ):
                    if nx.is_connected(SG):
                        trovato = False
                        GM = nx.algorithms.isomorphism.GraphMatcher(
                            G1, SG, node_match=nodeMatchAttr
                        )
                        # nx.draw(SG,with_labels=True)
                        # plt.show()
                        if GM.subgraph_is_isomorphic():
                            print("trovato2")
                            for element in mat3d:
                                GM2 = nx.algorithms.isomorphism.GraphMatcher(
                                    SG, element, node_match=nodeMatchAttr
                                )
                                if GM2.is_isomorphic():
                                    print("trovato")
                                    trovato = True
                                    self.execute_queries_in_string(
                                        self.GraphtoCypher(SG, i)
                                    )

                                    # session.driver.session().run(GraphtoCypher(SG,i))
                                    if i == 100:
                                        print(self.GraphtoCypher(SG, i))
                                    i += 1
                                    break
                            if trovato == False:
                                mat3d.append(SG)
            conta_iter += 1
        return mat3d, numnodes

    def GraphtoCypher(
        G, id, NameNode="Atom", NameCompound="Compound"
    ):  # convert grap object to cypher query (NameNode=Atom)
        stringa = (
            "CREATE (c_"
            + str(id)
            + ":"
            + NameCompound
            + "_ {idComp: '"
            + str(id)
            + "'})\n"
        )
        for nod in G.nodes():
            stringa += (
                "CREATE (a_"
                + str(nod)
                + ":"
                + str(NameNode)
                + "{ symbol: '"
                + str(
                    next(self.get_frozenset_elements(G.nodes[nod]["symbol"]["symbol"]))
                )
                + "'})"
                + "\n"
            )
        stringa += "CREATE" + "\n"
        for nod in G.nodes():
            stringa += "(c_" + str(id) + ")-[:RELATED]->(a_" + str(nod) + "),\n"
        stringa = stringa[:-2]
        stringa += "\n CREATE \n"
        for edge in G.edges(data=True):
            stringa += (
                "(a_" + str(edge[0]) + ")-[:BOND_WITH]->(a_" + str(edge[1]) + "),\n"
            )
        stringa = stringa[:-2]
        stringa += "\n;"
        return stringa

    def import_graph_from_neo4j_to_networkx(self, query):
        graph = nx.Graph()
        query2 = query
        # query2="MATCH (a:Atom)-[b:BOND_WITH]-(d:Atom) MATCH( (c:Compound)-[r:RELATED]->(a:Atom)) WHERE c.idComp='1' RETURN a,b"

        with self.driver.session() as session:
            results = session.run(query2)
            G1 = nx.MultiDiGraph()
            nodes = list(results.graph()._nodes.values())
            for node in nodes:
                G1.add_node(node.id, name=node._labels, symbol=node._properties)
            rels = list(results.graph()._relationships.values())
            for rel in rels:
                G1.add_edge(
                    rel.start_node.id,
                    rel.end_node.id,
                    key=rel.id,
                    type=rel.type,
                    properties=rel._properties,
                )
            return G1

    def get_frozenset_elements(frozen_set):
        for i in frozen_set:
            yield i

    # funzione che controlla il terzo set di dati
    def check_3_set(id1, NomeLabelComposto, nodeMatchAttr, edgeMatchAttr):
        query1 = (
            "MATCH (a:Atom)-[b:BOND_WITH]-(d:Atom) MATCH( (c:Compound)-[r:RELATED]->(a:Atom)) WHERE c.idComp='"
            + str(id1)
            + "' RETURN a,b"
        )
        querynumSubcompound = "MATCH (n:" + NomeLabelComposto + ") RETURN count(n)"
        numSubcompound = cypher.run(querynumSubcompound)[0][0]
        conta_iter = 0
        listaresults = []
        results1 = cypher.run(query1)
        G1 = results1.get_graph()
        G1 = G1.to_undirected()
        print(numSubcompound)
        for i in range(1, numSubcompound):
            query2 = (
                "MATCH (a:Atom)-[b:BOND_WITH]-(d:Atom) MATCH((c:"
                + NomeLabelComposto
                + ")-[r:RELATED]->(a:Atom)) WHERE c.idComp='"
                + str(i)
                + "' RETURN a,b"
            )
            results2 = cypher.run(query2)
            print(results2)
            if results2 is not None:
                G2 = results2.get_graph()
                G2 = G2.to_undirected()
                GM2 = nx.algorithms.isomorphism.GraphMatcher(
                    G1, G2, node_match=nodeMatchAttr, edge_match=edgeMatchAttr
                )
                if GM2.subgraph_is_isomorphic():
                    listaresults.append(G2)
        return listaresults
