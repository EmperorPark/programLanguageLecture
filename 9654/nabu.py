# BACKJOON Online Judge #9654

data = []
data.append(('SHIP NAME', 'CLASS', 'DEPLOYMENT', 'IN SERVICE'))
data.append(('N2 Bomber', 'Heavy Fighter', 'Limited', '21'))
data.append(('J-Type 327', 'Light Combat', 'Unlimited', '1'))
data.append(('NX Cruiser', 'Medium Fighter', 'Limited', '18'))
data.append(('N1 Starfighter', 'Medium Fighter', 'Unlimited', '25'))
data.append(('Royal Cruiser', 'Light Combat', 'Limited', '4'))
for line in data:
    print('{:15s}{:15s}{:11s}{:10s}'.format(line[0], line[1], line[2], line[3]))