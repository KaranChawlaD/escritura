def lift():
    return "G0 Z10"

def drop():
    return "G0 Z0"

def create_command_chain(matrix, one_neighbors):

    cmds = []

    # auto home initially
    cmds.append("G28")

    for pt in one_neighbors:
        cmds.append(lift)
        cmds.append(f"G0 X{pt[0]} Y{pt[1]}")
        cmds.append(drop)

        # now go to the pt's neighbour, if it exists (while loop)
        # pop pt if it exists in one_neighbors

if __name__ == "__main__":
    pass