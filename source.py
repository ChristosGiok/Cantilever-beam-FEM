        el.append(Element(nodes[i-1], nodes[i], EI))
    return el

def global_stiffness(e_list):
    """Calcultes and returns the Global stiffness matrix of beam by taking a list of elements as an arguments"""
    n = len(e_list)
    dim = 2 * (n + 1)
    K = numpy.zeros((dim, dim))

    def place_2by2_at(i, element): #digonal index
        K[i:i+2, i:i+2] = numpy.add(K[i:i+2, i:i+2], element.k1)
        K[i:i+2, i+2:i+4] = numpy.add(K[i:i+2, i+2:i+4], element.k2)
        K[i+2:i+4, i:i+2] = numpy.add(K[i+2:i+4, i:i+2], element.k3)
        K[i+2:i+4, i+2:i+4] = numpy.add(K[i+2:i+4, i+2:i+4], element.k4)

    ii = 0
    for iii in range(0,n):
        place_2by2_at(ii, e_list[iii])
        ii += 2
    return K

def deflection_on_nodes(nodes, elements):
    """Calculates and returns defelection vector v = [v1, th1, v2, th2, .....vn, thn].
    It also modifies all the nodes by assigning calculated v and th of each node 
    This function is designed for cantiliver beams only by considering boundary condition of 
    zero defection at fixed end, it then calculates the deflection using equation f = ku => u = f/k.
    In future this method can be modified for other mboundary conditions for generalized solution for beams"""
    frc = []
    for ii in range(1, len(nodes)):
        frc.append(nodes[ii].f)
        frc.append(nodes[ii].m)

    frc = numpy.array(frc)
    frc = numpy.transpose(frc)

    K = global_stiffness(elements)
    K_inv = numpy.linalg.inv(K[2:,2:])

    defs = numpy.matmul(K_inv, frc)

    jj = 0
    for ii in range(1, len(nodes)):
        nodes[ii].v = defs[jj]
        jj += 1
        nodes[ii].th = defs[jj]
        jj += 1
        
    return defs

inc = 0.001 * s #Beam will be divided into 1000 parts
node_pos = numpy.arange(0.0, s+inc, inc) # location of nodes based on increment size
'''--------------------------Deflection For P and W-----------------------'''

'''Creating list of nodes form node_pos'''
nodes = []
for position in node_pos:
    node = Node(position)
    nodes.append(node)

'''Changing f and m values of node or nodes on which p is applied'''
for ii in range(0, len(nodes)):
    if nodes[ii].pos == xp:
        nodes[ii].f = p
        break
    elif nodes[ii].pos > xp:
        dx = nodes[ii].pos - xp
        nodes[ii].f = p * ((inc-dx)/dx)
        nodes[ii].m = p * dx

        nodes[ii-1].f = p - nodes[ii].f
        nodes[ii-1].m = p * (inc - dx)
        break

'''Changing f and m values of nodes if w is applied'''    
if(w != 0):
    for ii in range(0, len(nodes)):
        nodes[ii].f = nodes[ii].f + w * inc/2
        nodes[ii].m = nodes[ii].m + w * inc * inc /2

        nodes[ii-1].f = nodes[ii-1].f + w * inc/2
        nodes[ii-1].m = nodes[ii-1].m + w * inc * inc /2

'''creating elements form node list'''
elements = elem(nodes)

'''Deflections is the deflection vector in the form [v1, th1, v2, th2 ---- vn, thn] and may not be used directly for ploting
instead one can use the node list generated earlier to get the vs and ths separately.
Remember that the ftn "deflection_on_nodes" also populates all the vs and ths to the nodes of node list'''
deflections = deflection_on_nodes(nodes, elements)


'''------------------------sfd and bmd ordinates------------'''
elements = elem(nodes)
sfs = []
bms = []

for element in elements:
    sfs.append(element.s_f)
    bms.append(element.b_m)
sfs.append(0)
bms.append(0)

'''Ploting deflection curves, subplots of displacements and slopes'''
deflection_plot_figure = plt.figure(1, figsize=(6.4, 10))
plot_v = deflection_plot_figure.add_subplot(211)
plot_v.set_title('Displacment Curve')

plot_th = deflection_plot_figure.add_subplot(212)
plot_th.set_title('Slope Curve')

plot_v.plot([node.pos for node in nodes], [node.v for node in nodes])
plot_th.plot([node.pos for node in nodes], [node.th for node in nodes])

sfd_bmd = plt.figure(2, figsize=(6.4, 10))
plot_sfd = sfd_bmd.add_subplot(211)
plot_sfd.set_title('SFD')

plot_bmd = sfd_bmd.add_subplot(212)
plot_bmd.set_title('BMD')

plot_sfd.plot([node.pos for node in nodes], [sf for sf in sfs])
plot_bmd.plot([node.pos for node in nodes], [bm for bm in bms])

plt.show()
'''Solved example'''
#10,200,3,50,200000000000,0.02,0.06
