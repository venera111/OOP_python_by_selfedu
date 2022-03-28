"""6. Режимы доступа public, private, protected. Сеттеры и геттеры"""

# @private из библиотеки позволяет запретить вызов функции вне класса
# вместо декоратора можно использовать __check_value(cls, x) нижнее подчеркивание
# одиночное подчеркивание позволяет обратиться извне, но так не рекомендуется
# к приватному методу можно обратиться черз название класса _Point__check_value()
# но так тоже не рекомендуется делать

from accessify import private, protected

class Point:
	def __init__(self, x=0, y=0):
		self.__x = self.__y = 0
		if self.check_value(x) and self.check_value(y):
			self.__x = x
			self.__y = y

	@private #защита от доступа извне
	@classmethod # будет вызываться для проверки и мб использовать атрибуты класса в будущем
	def check_value(cls, x):
		return type(x) in (int, float)

	def set_coords(self, x, y):
		if self.check_value(x) and self.check_value(y):
			self.__x = x
			self.__y = y
		else:
			raise ValueError('координаты должны быть числами')

	def get_coords(self):
		return self.__x, self.__y

pt = Point(1, 2)
pt.set_coords(10, 20)
print(pt.get_coords())
print(dir(pt))
