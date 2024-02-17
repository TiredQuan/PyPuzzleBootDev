# The maze should be making cells of 50x50, and the cell mutiplication should end if the pixel on the screen hits the invisible border of 50px padding (self-made value)
# We could achieve this by making an if statement constantly checking whether or not the increment is smaller than 800x600, AND it should be smaller than (800 - 50) x (600 - 50)

from graphic import Line, Point

class Cell():
	# Cell uses both Lines and Points to make a square, simply by drawing lines using
	# using the designated xy cords, takes in 2 xy cords, and draw each side using
	# those cords
	def __init__(self, x1, y1, x2, y2, win):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.left_wall = Line(Point( x1, y1 ),Point( x1, y2 ))
		self.top_wall = Line(Point( x1, y1 ),Point( x2, y1 ))
		self.right_wall = Line(Point( x2, y1 ),Point( x2, y2 ))
		self.bottom_wall = Line(Point( x1, y2 ),Point( x2, y2 ))
		self._win = win
	def draw(self):
		if self.left_wall:
			self._win.draw_line(self.left_wall)
		if self.top_wall:
			self._win.draw_line(self.top_wall)
		if self.right_wall:
			self._win.draw_line(self.right_wall)
		if self.bottom_wall:
			self._win.draw_line(self.bottom_wall)
	def draw_move (self,to_cell, undo=False):
		fill_color = "red"
		if undo:
			fill_color = "gray"
		# Draw move should take in 2 cells, and then see if there ISN'T an overlap
		# If there isn't, then draw a line inbetween them
		mid_x = (self.x1 + self.x2)/2
		mid_y = (self.y1 + self.y2)/2
		mid_cell_x = (to_cell.x1 + to_cell.x2)/2
		mid_cell_y = (to_cell.y1 + to_cell.y2)/2
		move_line = Line(Point(mid_x, mid_y),Point(mid_cell_x, mid_cell_y))
		self._win.draw_line(move_line,fill_color)

class Maze:
	def __init__(
		self,
		x1,y1,
		num_rows,num_cols,
		cell_size_x,cell_size_y,
		win
	):
		self.x1 = x1
		self.y1 = y1
		self.num_rows = num_rows
		self.num_cols = num_cols
		self.cell_size_x = cell_size_x
		self.cell_size_y = cell_size_y
		self._win = win
		self._cells = []
		# this method should probably itterate using the number of rows and columns that we could create the numbers of rows and columns based on the number put out, and the size of the cells are indicated in the [cell_size_x/y]
	def _create_cells(self):
		x = 50
		y = 50
		for row in self.num_rows:
			y += 50
			for col in self.num_cols:
				x += 50
		# for iterable lambda func
		def draw_cell(cell):
			cell.draw()
