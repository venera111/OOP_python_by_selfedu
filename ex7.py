"""7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__"""

# атрибуты класса не копируются в экземпляры, но через жкз мы можем обращаться к атрибутам
# тк пространство имет экземпляра додержит ссылку на внешнее пространство класса
# если атрибута в экз нет, то поиск будет в классе


class Point:
	MIN_COORD = 0
	MAX_COORD = 100

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def set_coords(self, x, y):
		if self.MIN_COORD <= x <= self.MAX_COORD:
			self.x = x
			self.y = y

	@classmethod #пусть будет методом класса, работает только с атрибутами класса
	def set_bound(cls, left): # задаем ссылку на класс, а не self, чтобы поменять атрибут класса, а не создать локальный атрибут
		cls.MIN_COORD = left

	# срабатывает когда обращение к атрибуту через экземпляр
	# по умолч возвращает None
	# позволяет защитить атрибут экземпляра
	def __getattribute__(self, item):
		if item == 'x':
			raise ValueError('доступ запрещен')
		else:
			return object.__getattribute__(self, item)

	# срабатывает всегда когда идет присвоение атрибуту какого-либо значения
	# запретить создавать локальный атрибут
	def __setattr__(self, key, value):
		if key == 'z':
			raise AttributeError('недопустимое значение')
		else:
			object.__setattr__(self, key, value)
			# self.x = value # будет рекурсия метода __setattr__
			# self.__dict__[key] = value #так можно делать

	# когда идет обращение к несуществующему атрибуту экземпляра класса или атриб класса
	# мы не хотим чтобы появлялась ошибка и переопределяем на False или др значение
	def __getattr__(self, item):
		return False

	# когда удаляется атрибут экземпляра
	def __delattr__(self, item):
		print('__delattr__: ' + item)
		object.__delattr__(self, item) #если не сделать, не удалится атрибут

# 4 раза обратились к атрибуту и изменили значение -> __setattr__
pt1 = Point(1, 2)
pt2 = Point(10, 20)
# pt1.x = 5 # возникнет ошибка
# print(pt1.yy)
del pt1.x #
print(pt1.__dict__)
# print(pt1.MIN_COORD) # обратимся к атрибуту класса через экземпляр
# pt1.set_bound(-100) # изменяем атрибут класса
# print(pt1.__dict__) # не создался локальный атрибут
# print(Point.__dict__)
# print(Point.MAX_COORD)
# a = pt1.x
# print(a)
# b = pt1.y
