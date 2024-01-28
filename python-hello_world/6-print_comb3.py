for i in range(0, 10):
    print(', '.join("{:2d} {:2d}".format(min(i, j), max(i, j)) for j in range(i + 1, 10)), end='\n')
