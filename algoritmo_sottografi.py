import modulo_algoritmo_sottografi as af

# SET DI SATI IN INGRESSO
numgrafi = 2  # se numgrafi=3 allora si prendono i composti con id: 0,1,2 nel primo set e 1000 1001 1002
radius = 3  # il raggio rappresenta il numero di vicini presi in considerazione da un nodo di partenza
deep = 4  # Rappresenta la profondità di ricerca all'interno del cerchio di raggio=radius minimo 4

comb2 = 0
iteraz = 0
pathoutA1 = "./data"
pathoutA2 = "./data2"

matrix = []
matrix2 = []
comb = 0
num_iterazione = 0
start = time.time()
neo4jUsername = "neo4j"
neo4jPassword = "abCD12.,"
neo4jUri = "10.224.19.64"
print(neo4jUsername, neo4jPassword, neo4jUri)
graph_controller = GraphController(neo4jUri, neo4jUsername, neo4jPassword)

for i in range(0, numgrafi):
    for j in range(i, numgrafi):
        if i != j:
            num_iterazione += 1
            [mat3d, n] = af.findSubGraphs(
                i,
                j,
                num_iterazione,
                lambda n1, n2: n1["name"] == n2["name"],
                lambda e1, e2: e1["BOND_WITH"]["type2"] == e2["BOND_WITH"]["type2"],
                radius,
                deep,
            )
            comb = comb + 1
            matrix = matrix + mat3d
            af.to_files(mat3d, i, j, "Atom", "Sub" + str(i) + str(j), pathoutA1)
end = time.time()
lista_occorrenze = af.conta_occorrenze_lista(matrix, comb)

for i in range(1000, numgrafi + 1000):
    for j in range(i, numgrafi + 1000):
        if i != j:
            num_iterazione += 1
            [mat3d, n] = af.findSubGraphs(
                i,
                j,
                num_iterazione,
                lambda n1, n2: n1["name"] == n2["name"],
                lambda e1, e2: e1["BOND_WITH"]["type2"] == e2["BOND_WITH"]["type2"],
                radius,
                deep,
            )
            matrix2 = matrix2 + mat3d
            comb2 = comb2 + 1
            af.to_files(mat3d, i, j, "Atom", "Sub" + str(i) + str(j), pathoutA2)

lista_occorrenze2 = af.conta_occorrenze_lista(matrix2, comb2)


id1 = 0
for element in lista_occorrenze:
    if element[2] > 50:
        id1 += 1
        af.single_to_neo4j(element[0], id1, "Atom", "Composti1")

id2 = id1
for element2 in lista_occorrenze2:
    if element2[2] > 50:
        id2 += 1
        af.single_to_neo4j(element2[0], id2, "Atom", "Composti2")

listarisultati = af.check_3_set(
    1,
    "Composti1_",
    lambda n1, n2: n1["name"] == n2["name"],
    lambda e1, e2: e1["BOND_WITH"]["type2"] == e2["BOND_WITH"]["type2"],
)
id3 = 0
for element in listarisultati:
    print(id3)
    id3 += 1
    af.single_to_neo4j(element, id3, "Atom", "CompostiFinali")

# store timer results
end = time.time()

nomefile = "risultati_tempo.txt"
out_file = open(nomefile, "a+")
out_file.write(
    "Numero grafi "
    + str(numgrafi)
    + "\nRaggio "
    + str(radius)
    + "\nProfondità "
    + str(deep)
    + "\nTempo inizio: "
    + str(start)
    + "\n Tempo fine: "
    + str(end)
    + "\nTempo totale: "
    + str(end - start)
    + " secondi\n"
)
out_file.close()
