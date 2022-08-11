import sqlite3
class DB():
	def __init__(self):
		self.conn = sqlite3.connect("base.db")
		self.cursor = self.conn.cursor()
	def get_country(self, title):
		with self.conn:
			result = self.cursor.execute("""SELECT * FROM info WHERE title = (?)""", (title,))
			return result.fetchone()
