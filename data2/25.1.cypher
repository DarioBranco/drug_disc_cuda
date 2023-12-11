CREATE (c_1:Compound{idComp: '7'})
CREATE (a_1:Atom {symbol: 'C'})
CREATE (a_2:Atom {symbol: 'F'})
CREATE (a_3:Atom {symbol: 'C'})
CREATE (a_4:Atom {symbol: 'F'})
CREATE (a_5:Atom {symbol: 'C'})
CREATE (a_6:Atom {symbol: 'O'})
CREATE (a_7:Atom {symbol: 'C'})
CREATE (a_8:Atom {symbol: 'F'})
CREATE (a_9:Atom {symbol: 'H'})
CREATE (a_10:Atom {symbol: 'F'})
CREATE (a_11:Atom {symbol: 'F'})
CREATE (a_12:Atom {symbol: 'O'})
CREATE (a_13:Atom {symbol: 'C'})
CREATE (a_14:Atom {symbol: 'O'})
CREATE (a_15:Atom {symbol: 'C'})
CREATE (a_16:Atom {symbol: 'F'})
CREATE (a_17:Atom {symbol: 'O'})
CREATE (a_18:Atom {symbol: 'O'})
CREATE (a_19:Atom {symbol: 'F'})
CREATE (a_20:Atom {symbol: 'H'})
CREATE (a_21:Atom {symbol: 'C'})
CREATE (a_22:Atom {symbol: 'O'})
CREATE (a_23:Atom {symbol: 'C'})
CREATE (a_24:Atom {symbol: 'F'})
CREATE (a_25:Atom {symbol: 'C'})


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
(c_1)-[:RELATED]->(a_10),
(c_1)-[:RELATED]->(a_11),
(c_1)-[:RELATED]->(a_12),
(c_1)-[:RELATED]->(a_13),
(c_1)-[:RELATED]->(a_14),
(c_1)-[:RELATED]->(a_15),
(c_1)-[:RELATED]->(a_16),
(c_1)-[:RELATED]->(a_17),
(c_1)-[:RELATED]->(a_18),
(c_1)-[:RELATED]->(a_19),
(c_1)-[:RELATED]->(a_20),
(c_1)-[:RELATED]->(a_21),
(c_1)-[:RELATED]->(a_22),
(c_1)-[:RELATED]->(a_23),
(c_1)-[:RELATED]->(a_24),
(c_1)-[:RELATED]->(a_25)


CREATE
(a_1)-[:BOND_WITH]->(a_6),
(a_8)-[:BOND_WITH]->(a_7),
(a_3)-[:BOND_WITH]->(a_14),
(a_6)-[:BOND_WITH]->(a_3),
(a_1)-[:BOND_WITH]->(a_2),
(a_2)-[:BOND_WITH]->(a_4),
(a_10)-[:BOND_WITH]->(a_9),
(a_4)-[:BOND_WITH]->(a_9),
(a_4)-[:BOND_WITH]->(a_5),
(a_5)-[:BOND_WITH]->(a_8),
(a_10)-[:BOND_WITH]->(a_5),
(a_9)-[:BOND_WITH]->(a_15),
(a_3)-[:BOND_WITH]->(a_11),
(a_6)-[:BOND_WITH]->(a_12),
(a_11)-[:BOND_WITH]->(a_12),
(a_6)-[:BOND_WITH]->(a_13),
(a_13)-[:BOND_WITH]->(a_14),
(a_3)-[:BOND_WITH]->(a_16),
(a_6)-[:BOND_WITH]->(a_20),
(a_11)-[:BOND_WITH]->(a_20),
(a_7)-[:BOND_WITH]->(a_19),
(a_17)-[:BOND_WITH]->(a_4),
(a_1)-[:BOND_WITH]->(a_18),

(a_21)-[:BOND_WITH]->(a_9),
(a_21)-[:BOND_WITH]->(a_4),
(a_21)-[:BOND_WITH]->(a_10),
(a_22)-[:BOND_WITH]->(a_5),
(a_23)-[:BOND_WITH]->(a_2),
(a_23)-[:BOND_WITH]->(a_24),
(a_25)-[:BOND_WITH]->(a_16)

;
