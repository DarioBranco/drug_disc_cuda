
def GraphtoCypher(G,id,NameNode,NameCompound): #convert grap object to cypher query (NameNode=Atom)
    stringa="CREATE (c_"+str(id)+":"+NameCompound+"_ {idComp: '"+str(id)+"'})\n"
    for nod in G.nodes():
        stringa+="CREATE (a_"+str(nod)+":"+str(NameNode)+"{ name: '"+str(G.node[nod]['name'])+"'})"+"\n"
    stringa+="CREATE"+"\n"
    for nod in G.nodes():
        stringa+="(c_"+str(id)+")-[:RELATED]->(a_"+str(nod)+"),\n"
    stringa=stringa[:-2]
    stringa+="\n CREATE \n"
    for edge in G.edges(data=True):
        stringa+="(a_"+str(edge[0])+")-[:BOND_WITH {type2: "+chr(34)+str(edge[2]['type2'])+chr(34)+" }]->(a_"+str(edge[1])+"),\n"
    stringa=stringa[:-2]
    stringa+="\n;"
    return stringa
