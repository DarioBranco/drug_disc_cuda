CREATE (c_1:Compound{idComp: '1'})
CREATE (a_1:Atom {symbol: 'C'})
CREATE (a_2:Atom {symbol: 'O'})
CREATE (a_3:Atom {symbol: 'C'})
CREATE (a_4:Atom {symbol: 'O'})
CREATE (a_5:Atom {symbol: 'C'})
CREATE (a_6:Atom {sy  mbol: 'C'})
CREATE (a_7:Atom {symbol: 'F'})
CREATE (a_8:Atom {symbol: 'C'})
CREATE (a_9:Atom {symbol: 'O'})
CREATE (a_10:Atom {symbol: 'C'})


CREATE
(c_1)-[:RELATED]->(a_1),
(c_1)-[:RELATED]->(a_2),
(c_1)-[:RELATED]->(a_3),
(c_1)-[:RELATED]->(a_4),
(c_1)-[:RELATED]->(a_5),
(c_1)-[:RELATED]->(a_6),
(c_1)-[:RELATED]->(a_7),
(c_1)-[:RELATED]->(a_8),
(c_1)-[:RELATED]->(a_9),
(c_1)-[:RELATED]->(a_10)


CREATE
(a_1)-[:BOND_WITH]->(a_6),
(a_1)-[:BOND_WITH]->(a_7),
(a_3)-[:BOND_WITH]->(a_1),
(a_6)-[:BOND_WITH]->(a_3),
(a_6)-[:BOND_WITH]->(a_2),
(a_1)-[:BOND_WITH]->(a_2),
(a_2)-[:BOND_WITH]->(a_4),
(a_2)-[:BOND_WITH]->(a_9),
(a_4)-[:BOND_WITH]->(a_9),
(a_4)-[:BOND_WITH]->(a_5),
(a_5)-[:BOND_WITH]->(a_8),
(a_10)-[:BOND_WITH]->(a_5),
(a_5)-[:BOND_WITH]->(a_3)
;
