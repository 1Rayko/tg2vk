import sqlite3


class Database:
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    ''' Методы для работы с таблицей USERS '''

    def add_user(self,user_id,nickname,url): # Добавляет пользователя в таблицу
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`, `nickname`, `url`, `isAdmin`) VALUES (?, ? , ?, ?)",(user_id,nickname,url,0,))

    def user_exists(self,user_id): # проверяет существует ли пользователь в бд и возвращает истину или ложь
        with self.connection:
            result = self.cursor.execute("select * from `users` where `user_id` = ?",(user_id,)).fetchall()
            return bool(len(result))

    def is_admin(self,user_id): # проверяет значение поля isAdmin
        with self.connection:
            return self.cursor.execute("select `isAdmin` from `users` where `user_id` = ?",(user_id,)).fetchall()

    def set_admin(self, user_id, new_state): # изменяет поле isAdmin
        with self.connection:
            self.cursor.execute("UPDATE `users` SET `isAdmin` = ? WHERE `user_id` = ?", (new_state, user_id))
            return self.cursor.rowcount

    def get_all_user_id(self): # Возвращает все user_id из таблицы. Полезно для массовой рассылки
        with self.connection:
            return self.cursor.execute("select user_id from `users` ").fetchall()

    ''' Методы для чатов '''

    def create_chat_table(self,chat_id): # создает таблицу слов под конкретный чат
        with self.connection:
            self.cursor.execute(f"""CREATE TABLE words_{message.chat.id} (
                word text
            )""")


    def get_words(self,chat_table): # возвращает все слова из таблицы
        pass

    def add_word (self,chat_table,word): # Добавляет слово в таблицу чата
        with self.connection:
            self.cursor.execute(f"""INSERT INTO words_{message.chat.id} VALUES (
                {word}
            )""")


    def get_admin(self,chat_table): # возвращает админа конкретного чата
        pass


    ''' Методы для  '''
    def get_chats(self):
        with self.connection:
            return self.cursor.execute("SELECT chat_id from chats").fetchall()

    def add_chat(self,chat_id,title):
        with self.connection:
            return self.cursor.execute("INSERT INTO `chats` (`chat_id`, `title`) VALUES (?, ?)",(chat_id,title,))
        with self.connection:
            self.cursor.execute(f"INSERT INTO `chats` (`chat_id`, `title`) VALUES ({chat_id}, {title})")
