class Node:
    """Represents asingle node in FEM, and has all the attributes required for an FEM node"""

    pos = 0 #Position of node from fixed end
    f = 0 #Applied force on the node
    m = 0 #Applied moment on the node
    v = 0 #vertical deflection
    th = 0 #Rotation

    def __init__(self, pos:float):
        self.pos = pos
        