##
# Chips & Circuits
# Team Paprikachips
# Alle lists met de nodes op de grids en de netlists.
##

# Grids staan als (y, x) omdat de nested list ze dan omdraait naar (x, y)
# FIX: Zet de grids als (x, y) en draai ze om in de addGate functie
grid1 = [(1, 1, 1), (2, 1, 6), (3, 1, 10), (4, 1, 15), (5, 2, 3), (6, 2, 12), (7, 2, 14), (8, 3, 12), (9, 4, 8),
(10, 5, 1), (11, 5, 4), (12, 5, 11), (13, 5, 16), (14, 6, 13), (15, 6, 16), (16, 8, 2), (17, 8, 6), (18, 8, 9),
(19, 8, 11), (20, 8, 15), (21, 9, 1), (22, 10, 2), (23, 10, 9), (24, 11, 1), (25, 11, 12)]

grid2 = [(1, 1, 1), (2, 1, 6), (3, 1, 10), (4, 1, 15), (5, 2, 3), (6, 2, 12), (7, 2, 14), (8, 3, 1), (9, 3, 6),
(10, 3, 12), (11, 3, 15), (12, 4, 2), (13, 4, 8), (14, 5, 1), (15, 5, 4), (16, 5, 10), (17, 5, 11), (18, 5, 16),
(19, 6, 2), (20, 6, 7), (21, 6, 10), (22, 6, 12), (23, 6, 15), (24, 7, 6), (25, 7, 13), (26, 7, 16), (27, 8, 6),
(28, 8, 7), (29, 8, 9), (30, 8, 11), (31, 8, 15), (32, 9, 1), (33, 9, 6), (34, 10, 9), (35, 11, 12), (36, 12, 2),
(37, 12, 4), (38, 12, 7), (39, 12, 10), (40, 12, 15), (41, 13, 9), (42, 13, 13), (43, 14, 4), (44, 14, 6), (45, 15, 1),
(46, 15, 6), (47, 15, 8), (48, 15, 11), (49, 15, 13), (50, 15, 16)]

# Lists met de nodes die met elkaar verbonden moeten worden.
# Chip 1
netlist_1 = [(23, 4), (5, 7), (1, 0), (15, 21), (3, 5), (7, 13), (3, 23), (23, 8), (22, 13), (15, 17),
(20, 10), (15, 8), (13, 18), (19, 2), (22, 11), (10, 4), (11, 24), (3, 15), (2, 20), (3, 4), (20, 19),
(16, 9), (19, 5), (3, 0), (15, 5), (6, 14), (7, 9), (9, 13), (22, 16), (10, 7)]

netlist_2 = [(12, 20), (23, 20), (6, 9), (15, 10), (12, 13), (8, 18), (1, 22), (10, 20), (4, 3),
(10, 5), (17, 11), (1, 21), (22, 8), (22, 10), (19, 8), (13, 19), (10, 4), (9, 23), (22, 18),
(16, 21), (4, 0), (18, 21), (5, 17), (8, 23), (18, 13), (13, 11), (11, 7), (14, 7), (14, 6),
(14, 1), (24, 12), (11, 15), (2, 5), (11, 12), (0, 15), (14, 5), (15, 4), (19, 9), (3, 0), (15, 13)]

netlist_3 = [(0, 13), (0, 14), (0, 22), (8, 7), (2, 6), (3, 19), (3, 9), (4, 8), (4, 9), (5, 14),
(6, 4), (4, 1), (7, 23), (10, 0), (10, 1), (8, 1), (7, 5), (12, 14), (13, 2), (8, 10), (11, 0),
(11, 17), (11, 3), (8, 9), (12, 24), (13, 4), (13, 19), (15, 21), (10, 3), (18, 10), (24, 23),
(16, 7), (17, 15), (17, 21), (17, 9), (18, 20), (18, 2), (12, 9), (1, 13), (19, 21), (20, 6),
(1, 15), (2, 16), (20, 16), (22, 11), (22, 18), (2, 3), (5, 12), (24, 15), (24, 16)]

# Chip 2
netlist_4 = [(42, 3), (3, 48), (14, 6), (36, 2), (14, 4), (10, 32), (47, 22), (41, 1), (21, 6),
(39, 18), (22, 49), (35, 14), (5, 31), (48, 24), (12, 14), (8, 42), (28, 43), (20, 40), (26, 24),
(46, 35), (0, 12), (46, 12), (35, 26), (21, 7), (43, 15), (0, 21), (35, 19), (31, 11), (43, 30),
(12, 1), (4, 30), (49, 13), (4, 29), (8, 28), (32, 29), (34, 45), (14, 39), (17, 25), (28, 27),
(31, 25), (37, 16), (2, 3), (3, 31), (4, 23), (5, 44), (33, 30), (36, 4), (29, 9), (46, 0), (39, 15)]

netlist_5 = [(34, 21), (48, 47), (38, 16), (0, 16), (28, 40), (24, 8), (36, 37), (26, 8), (8, 27),
(39, 48), (44, 34), (22, 30), (43, 44), (47, 5), (19, 30), (31, 41), (0, 10), (12, 32), (3, 33),
(45, 18), (0, 21), (23, 43), (44, 42), (18, 11), (24, 23), (41, 13), (26, 1), (16, 1), (20, 29),
(31, 4), (7, 28), (28, 45), (0, 12), (44, 29), (34, 5), (2, 17), (9, 5), (30, 9), (36, 29),
(18, 27), (32, 11), (40, 10), (4, 40), (35, 6), (17, 3), (10, 19), (25, 24), (20, 47), (12, 25),
(4, 15), (19, 33), (33, 36), (1, 3), (13, 49), (25, 49), (15, 42), (33, 4), (27, 22), (4, 8), (12, 24)]

netlist_6 = [(16, 10), (25, 17), (1, 11), (32, 2), (1, 20), (12, 36), (34, 19), (11, 10), (11, 45),
(21, 42), (36, 20), (15, 22), (3, 21), (48, 2), (32, 25), (38, 49), (24, 29), (14, 16), (0, 3),
(30, 7), (3, 10), (16, 8), (46, 0), (26, 41), (34, 2), (1, 13), (25, 6), (49, 28), (27, 47),
(3, 14), (40, 47), (14, 43), (14, 46), (27, 38), (14, 34), (26, 39), (47, 44), (46, 29), (12, 9),
(49, 12), (38, 7), (30, 32), (30, 40), (13, 45), (5, 41), (29, 37), (45, 38), (44, 34), (44, 28),
(22, 44), (43, 31), (48, 34), (6, 33), (33, 7), (1, 37), (5, 17), (37, 2), (39, 38), (27, 36),
(18, 42), (17, 35), (12, 5), (37, 40), (5, 39), (37, 43), (8, 4), (39, 3), (33, 31), (21, 33), (0, 39)]