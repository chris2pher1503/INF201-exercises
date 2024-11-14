import meshio
from abc import ABC, abstractmethod
"""
Flow: 

1. mesh class: Read the mesh file and extract points and cells data.
2. point class: Create `Point` objects for each point in the mesh.
3. TL(cell) class: Create `Triangle` or `Line` objects for each cell, depending on its type.
4. TL(cell) class: For each cell, find neighboring cells by checking shared points.
5. TL(cell) class: Determine if a cell is a boundary cell.
6. Print information about specific cells using their indexes. 
7. Test the implementation with cells having indexes 4, 189, 222.

"""


class Point:
    #point constructor with x and y coordinates / point
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def __str__(self):
        #printing the point with x and y coordinates
        return f"Point: ({self.x}, {self.y})"
    
    
class Cell(ABC):
    #cell construktor with index, points and a list to store the neighbors
    def __init__(self, index, points):
        self.index = index
        self._points = points 
        self._neighbors = [] 
    
    @abstractmethod
    #abstract method to check if a cell is a neighbor of another cell -> triangle and line
    def is_neighbor(self, other_cell):
        pass

    @abstractmethod
    #abstract method to check if a cell is a boundary cell -> triangle and line
    def is_boundary(self):
        pass
    
    def add_neighbor(self, neighbor):
        #appending the neighbor to the list of neighbors
        self._neighbors.append(neighbor)

    def __str__(self):
        #first checking if the cell is a boundary cell or not.
        #then printing the status, cell index and the indexes of its neighbors
        neighbor_indexes = [neighbor.index for neighbor in self._neighbors]
        if self.is_boundary():
            boundary_status = 'Boundary'
        else:
            boundary_status = 'Inside'
        return f"cell {self.index}: {boundary_status} , Neighbors: {neighbor_indexes}"
    
class Triangle(Cell):
    #checking if a cell is a neighbor of another cell, abstract method implementation
    def is_neighbor(self, other_cell):
        shared_points = set(self._points) & set(other_cell._points)
        return len(shared_points) == 2

    #checking if a cell is a boundary cell, abstract method implementation
    def is_boundary(self):
        return len(self._neighbors) < 3
        
class Line(Cell):
    #checking if a cell is a neighbor of another cell, abstract method implementation
    def is_neighbor(self, other_cell):
        shared_points = set(self._points) & set(other_cell._points)
        return len(shared_points) == 1
    
    #checking if a cell is a boundary cell, abstract method implementation
    def is_boundary(self):
        return True
    
    
class Mesh:
    #mesh constructor with points and cells 
    def __init__(self, meshFile):
        self._points = []
        self._cells = []
        self.read_mesh(meshFile)
        self.find_neighbors()
        
    #reading the mesh file and storing the points and cells
    def read_mesh(self, meshFile):
        msh = meshio.read(meshFile)
        points_data = msh.points  
        cells_data = msh.cells 
        
        for coords in points_data:
            x, y = coords[0], coords[1]
            self._points.append(Point(x, y))
        
        cell_index = 0
        """ print("cell data: ", cells_data) """
        for CellBlock in cells_data:
            """ print("type_cells: ", CellBlock) """
            cell_type = CellBlock.type
            for cell_points in CellBlock.data:
                if cell_type == 'triangle':
                    cell = Triangle(cell_index, cell_points.tolist())
                elif cell_type == 'line':
                    cell = Line(cell_index, cell_points.tolist())
                else:
                    print(f"Unknown type")
                    continue
                self._cells.append(cell)
                cell_index += 1 
    
    #finding the neighbors of each cell
    def find_neighbors(self):
        for i, cell in enumerate(self._cells):
            for j, other_cell in enumerate(self._cells):
                if i != j and cell.is_neighbor(other_cell):
                    """ print(f"Cell {i} is neighbor of cell {j}") """
                    cell.add_neighbor(other_cell)
     
    #printing the cell information   
    def print_cell_info(self, indexes):
        for index in indexes:
            if 0 <= index < len(self._cells):
                print(self._cells[index])
            else:
                print(f"Cell {index} does not exist.")
        
    
file  = 'simple.msh' 
mesh = Mesh(file)
mesh.print_cell_info([4, 189, 222])