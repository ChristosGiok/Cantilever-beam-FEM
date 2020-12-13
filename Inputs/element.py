import numpy

class Element:
    """An actual representation of an element in FEM, it consist of two nodes at its end and it calculates stiffness matrix"""

    n1 = None #node near fixed end (in our convention left end)
    n2 = None #node far from fixed end (in our convention right end)

    l = 0
    k = numpy.zeros((4, 4)) #stifness matrix

    k1 = numpy.zeros((2, 2))
    k2 = numpy.zeros((2, 2))
    k3 = numpy.zeros((2, 2))
    k4 = numpy.zeros((2, 2))

    q = [] #nodal displacement vector
    EI = 0

    def __init__(self, n1, n2, EI):
        """Calculates stiffness (4x4 matrix) k and also creates k1, k2, k3, k4 which are 2x2 matrices 
        k1, k2, k3, k4 helps in determining global stiffness matrix K of beam
        k1 is 2x2 located at top left of k
        k2 is 2x2 located at top right of k
        k3 is 2x2 located at bottom left of k
        k4 is 2x2 loacted at bottom right of k"""

        self.n1 = n1
        self.n2 = n2
        
        l = n2.pos - n1.pos
        if l<0:
            raise Exception("Invalid node data entered")
        else:
            self.l = l
    
        k = numpy.array([[12,   6*l,  -12,   6*l],
                      [6*l, 4*l*l, -6*l, 2*l*l],
                      [-12, -6*l,   12,   -6*l],
                      [6*l, 2*l*l, -6*l, 4*l*l]])
        k = k/(l**3)
        k = k * EI
        self.k = k
        self.k1 = k[0:2, 0:2]
        self.k2 = k[0:2, 2:4]
        self.k3 = k[2:4, 0:2]
        self.k4 = k[2:4, 2:4]

        self.q = [n1.v, n1.th, n2.v, n2.th]
        self.EI = EI

        self.shear_force()
        self.bending_moment()

    s_f = 0
    def shear_force(self):
        EI = self.EI
        l = self.l

        q = numpy.array(self.q)
        B = numpy.array([12/l**3, 6/l**2, -12/l**3, 6/l**2])
        B = EI * B
        self.s_f = numpy.matmul(B,q)
        return self.s_f

    b_m = 0
    def bending_moment(self):
        EI = self.EI
        l = self.l

        q = numpy.array(self.q)
        B = numpy.array([-6/l**2, -4/l, 6/l**2, -2/l])
        B = EI * B
        self.b_m = numpy.matmul(B,q)
        return self.b_m