# механизм инкапсуляции public, private, protected. Сеттеры и геттеры

from traceback import print_tb


class Point:
	def __init__(self, x=0, y=0) -> None:
		self.__x = self.__y = 0
		if self.__check_value(x) and self.__check_value(y):
			self.__x = x # защищенный локальный атрибут
			self.__y = y

	@classmethod
	def __check_value(cls, x):
		return type(x) in (int, float)

	def set_coord(self, x, y):
		if self.__check_value(x) and self.__check_value(y):
			self.__x = x
			self.__y = y
		else:
			raise ValueError("координаты должны быть числами")

	def get_coord(self):
		return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 5)
# print(pt.__x, pt.__y)
print(pt.get_coord())
# print(dir(pt))
print(pt._Point__x, pt._Point__y) # не рекомендуется так делать
