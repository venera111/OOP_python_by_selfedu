# __new__ и паттерн Singleton

class DataBase:
	__instance = None # ссылка на экземпляр класса

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls) # присвоим ссылку на экземпляр класса
		return cls.__instance

	def __init__(self, user, psw, port) -> None:
		self.user = user
		self.psw = psw
		self.port = port

	def __del__(self):
		DataBase.__instance = None

	def connect(self):
		print(f"connect with DB: {self.user}, {self.psw}, {self.port}")

	def close(self):
		print("close connection of DB")

	def read(self):
		print("data from DB")

	def write(self, data):
		print(f"write on DB {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40) # не был создан, ссылается на db
# print(id(db), id(db2))
db.connect()
db2.connect()
