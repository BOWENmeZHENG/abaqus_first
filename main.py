import read
import utils
import output

nodes, stresses = read.read_stresses("python_run/stress.rpt")
coords, elem_nodes = read.read_coords_elem_nodes("python_run/coord.inp")

nodes_sorted, stresses_sorted = utils.sort_nodes(nodes, stresses)

exterior_nodes = read.read_exterior("python_run/exterior.csv")

output.write_csv(nodes_sorted, stresses_sorted, coords, elem_nodes, exterior_nodes)

#