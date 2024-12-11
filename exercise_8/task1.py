import meshio


msh = meshio.read("simple.msh")

points = msh.points
cells = msh.cells

cell = cells[1].data[222]
print(cell)
print(cells[1].type)


if cells[1].type == "triangle":
    print("triangle.")
else:
    print("not triangle.")

print("Coordinates:")
for i in cell:
    point_coords = points[i]
    print(f"Point index {i}: {point_coords}")
