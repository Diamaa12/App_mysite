import random
import sqlite3
import pathlib

import faker as faker


class Users:
    dir = pathlib.Path(__file__).resolve().parent / "users_db.db"
    def __init__(self, name, username, age, message):
        self.name = name
        self.username = username
        self.age = age
        self.message = message
    def db_gestion(self, connect, disconnect):
        pass
    def enrgistrer(self):
        try:
            DB = sqlite3.connect(self.dir)
            cursor = DB.cursor()
            # requete = "CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT," \
            #            "Name text, Username text, Age INTEGER, Message text)"
            requete = "INSERT INTO user(Name, Username, Age, Message) VALUES(:Name, :Username, :Age, :Message)"
            data = {"Name":self.name, "Username":self.username, "Age":self.age, "Message":self.message}
            cursor.execute(requete, data)
            DB.commit()
            DB.close()
        except SyntaxError as e:
            print(f"L'erreur suivant {e} est survenu")
    def recup_data(self):
        DB = sqlite3.connect(self.dir)
        cursor = DB.cursor()
        requet = "SELECT * FROM user"
        data = cursor.execute(requet)
        perso = data.fetchall()

        DB.commit()
        DB.close()
        return perso
    def del_data(self, name):
        DB = sqlite3.connect(self.dir)
        cursor = DB.cursor()
        req = f"SELECT * FROM user WHERE Name == '{name}'"
        r = cursor.execute(req)
        '''IL faut essayer de resoudre le cas ou l'utilisateur n'existe pas'''
        user = len(r.fetchall())
        if user == 0 :
            print("L'utilisateur n'exite pas encore. ")
            return False
        else:
             rqst = f"DELETE FROM user WHERE Name = '{name}' "
             cursor.execute(rqst)
             print(f"{name} supprimé avec succés! ")
             DB.commit()
             DB.close()
             return True


fake = faker.Faker(locale="de_DE")
name = fake.first_name()
user_name = fake.last_name()
age = random.randrange(20, 50)
message = fake.text()
users = Users(name, user_name, age, message)

if __name__ == "__main__":
    #users.enrgistrer()
    #users.recup_data()
    n = input("Taper votre nom")
    r = users.del_data(n)
    print(r)
