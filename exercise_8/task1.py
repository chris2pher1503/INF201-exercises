import meshio


msh = meshio.read("simple.msh")

points = msh.points
cells = msh.cells

cell = cells[1].data[222]
print(cell)
print(cells[1].type)