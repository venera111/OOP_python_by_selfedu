"""9. Свойства property. Декоратор @property"""
# класс property создает объект-свойство для работы с приватным атрибутом экземпляра


class Person:
	def __init__(self, name, old):
		self.__name = name
		self.__old = old

	@property #getter
	def old(self): #имена методов должны совпадать
		return self.__old

	@old.setter #setter
	def old(self, old): #имена методов должны совпадать
		self.__old = old

	@old.deleter #вызывается когда удаляется свойство __old
	def old(self):
		del self.__old


p = Person('Сергей', 20)
del p.old # удаление через deleter
p.old = 5
# обращение к объекту-свойству класса
#декоратор getter позволяет получать значение
#декоратор setter устанавливает значение
# p.old = 35 #изменяем приватный атрибут экземпляра -> работает setter
print(p.__dict__) # получить значение приватного атрибута экземпляра

pass
