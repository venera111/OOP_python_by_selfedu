# Декораторы classmethod staticmethod

class Vector:
	MIN_COORD = 0
	MAX_COORD = 100

	@classmethod
	def validate(cls, arg):
		return cls.MIN_COORD <= arg <= cls.MAX_COORD

	def __init__(self, x, y) -> None:
		self.x = self.y = 0
		if self.validate(x) and self.validate(y):
			self.x = x
			self.y = y
		print(self.norm2(x, y))

	def get_coord(self):
		return self.x, self.y

	@staticmethod
	def norm2(x, y):
		return x*x + y*y

v = Vector(10, 20)
# res = Vector.get_coord(v)
# print(res)

print(Vector.norm2(5, 6))
