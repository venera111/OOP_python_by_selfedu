""" 4. Магический метод __new__. Пример паттерна Singleton """

# вызывется перед созданием объекта класса
# cls ссылается на текущий класс Point
# self ссылается на экземпляр класса Point
# __new__ должен возвращать адрес нового созданного объекта
# super() - ссылка на базовый класс object


class Point:
	def __new__(cls, *args, **kwargs): # базовое определение
		print('вызов __new__ для ' + str(cls))
		# запускаем процесс создания экземпляра и возвращаем адрес нового объекта
		return super().__new__(cls) #из базового класса вызываем __new__

	def __init__(self, x=0, y=0):
		print('вызов __init__ для ' + str(self))
		self.x = x
		self.y = y

pt = Point(1, 2)
print(pt)

# паттерн Singleton
# полагаем, что в программе должен существовать только один экземпляр этого класса в каждый момент ее работы.
class DataBase:
	__instance = None

	def __new__(cls, *args, **kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)

		return cls.__instance

	def __del__(self):
		DataBase.__instance = None

	def __init__(self, user, psw, port):
		self.user = user
		self.psw = psw
		self.port = port

	def connect(self):
		print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

	def close(self):
		print('закрытие соединения с БД')

	def read(self):
		return 'данные из БД'

	def write(data):
		print(f'запись в БД {data}')

db = DataBase('user', '1234', 80)
db2 = DataBase('user2', '5678', 40) # объект не создан, но перезаписаны данные
print(id(db), id(db2)) #id объектов одинаковые
db.connect()
db2.connect()

pass
