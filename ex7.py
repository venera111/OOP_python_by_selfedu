# __setattr__ __getattribute__ __getattr__ __delattr__

class Point:
	MAX_COORD = 100
	MIN_COORD = 0

	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y

	def set_coord(self, x, y):
		if self.MIN_COORD <= x <= self.MAX_COORD:
			self.x = x
			self.y = y

	@classmethod
	def set_bound(cls, left):
		cls.MIN_COORD = left


pt = Point(1, 2)
pt.set_bound(-100) # меняем атрибут класса MIN_COORD с помощью метода класса set_bound
print(Point.__dict__)

