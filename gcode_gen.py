def lift():
    return "G0 Z10"

def drop():
    return "G0 Z0"

def create_command_chain(matrix):

    cmds = []

    # auto home initially
    cmds.append("G28")

if __name__ == "__main__":
    pass