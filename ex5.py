""" 5. Методы класса (classmethod) и статические методы (staticmethod) """

# @classmethod позволяет работать только с атрибутами класса и не позволяет
# изменять локальные атрибуты экземпляра
# мы можем проверять входящее значение в __init__
#  у таких методов первый аргумент - ссылка на класс
# такой метод можно вызывать напрямую из класса Vector.validate(5)


# @staticmethod независимая функция внутри класса,
# которая не имеет доступа ни к атрибутам класса,
# ни к атрибутам экземпляра, а работает только с собственными входными значениями
# можно использовать как дополнительную функцию
# можно вызвать через название класса
class Vector:
	MIN_COORD = 0
	MAX_COORD = 100

	@classmethod
	def validate(cls, arg):
		return cls.MIN_COORD <= arg <= cls.MAX_COORD

	@staticmethod
	def norm2(x, y):
		return x*x + y*y

	def __init__(self, x, y):
		self.x = self.y = 0
		if self.validate(x) and self.validate(y):
			self.x = x
			self.y = y

		print(self.norm2(self.x, self.y))

	def get_coords(self):
		return self.x, self.y

v = Vector(10, 20)
print(v.get_coords())
print(Vector.norm2(2,2))
