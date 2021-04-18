def countingValleys(steps, path):
    ground_level = 0
    mountains = 0
    valleys = 0
    for _ in path:
        if _ == "U" and ground_level == 0:
            mountains += 1
            ground_level += 1
        elif _ == "D" and ground_level == 0:
            valleys+=1
            ground_level -= 1
        elif _ == "U":
            ground_level += 1
        elif _ == "D":
            ground_level -= 1
    return valleys
