import sqlite3
class Datos:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name="database.db"
    def crear(self):
        conn=sqlite3.connect(self.name)
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            password VARCHAR(50)
        )""")
    def consultar(self,consulta,parametros=()):
        conn=sqlite3.connect(self.name)
        cursor=conn.cursor()
        result=cursor.execute(consulta,parametros)
        conn.commit()
        return result