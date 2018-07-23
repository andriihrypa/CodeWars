class Grid():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = ""
		for i in range(self.height):
			for j in range(self.width):
				self.grid += "0"
			self.grid += "\n"
		self.grid = self.grid[0:-1]

	def plot_point(self, x, y):
		grid_list = self.grid.split("\n")
		grid_list[y-1] = grid_list[y-1][:x-1] + "X" + grid_list[y-1][x:]
		self.grid = "\n".join(grid_list)
		return self.grid

	def __repr__(self):
		pass


grid = Grid(9, 9)
# print(grid.grid)
print(grid.plot_point(5, 5))
