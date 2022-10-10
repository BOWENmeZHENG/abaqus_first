def write_csv(nodes, stresses, coords, elem_nodes):
    with open("nodes.csv", "w") as f:
        f.write("nodeid,x,y,z,stress\n")
        for i in range(len(nodes)):
            f.write(f"{nodes[i]},{coords[i][0]:.5},{coords[i][1]:.5},{coords[i][2]:.5},{stresses[i]:.5}\n")
    with open("elements.csv", "w") as f:
        f.write("elemid,node1,node2,node3,node4\n")
        for i in range(len(elem_nodes)):
            f.write(f"{i},{elem_nodes[i][0]},{elem_nodes[i][1]},{elem_nodes[i][2]},{elem_nodes[i][3]}\n")