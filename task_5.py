def tower_of_hanoi(n, source, dest, aux):
    if n == 0:
        return
    tower_of_hanoi(n - 1, source, aux, dest)
    print("Move disk", n, "from", source, "to", dest)
    tower_of_hanoi(n - 1, aux, dest, source)
    
