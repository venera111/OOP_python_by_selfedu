""" 3. Инициализатор __init__ и финализатор __del__ """

# магические методы
# __init__(self) - перед созданием экземпляра
# __del__(self) - перед удалением экземпляра

class Point:
	color = 'red'
	circle = 2

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __del__(self): # вызов перед удалением экземпляра
		print('удаление экземпляра ' + str(self))

	def set_coords(self, x, y):
		self.x = x
		self.y = y

	def get_coords(self):
		return self.x, self.y

pt = Point(1, 2)
# pt.set_coords(1, 2)
print(pt.__dict__)

pt2 = Point()
print(pt2.__dict__)

# магический метод init позволит сразу создать локальные атрибуты экземпляра класса

