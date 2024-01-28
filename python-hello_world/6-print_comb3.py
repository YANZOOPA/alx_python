for i in range(0, 10):
    print(', '.join(f"{min(i, j): 2d}{max(i, j): 2d}" for j in range(i + 1, 10)), end='\n')
