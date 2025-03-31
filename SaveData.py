import sqlite3
from Generate import question_set
class Save:
    def __init__(self):
        self._connection = sqlite3.connect('Questions.db')
        self._cursor = self._connection.cursor()
        self.create_table()

    def create_table(self):
        self._cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS trivia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                options TEXT NOT NULL,
                answer TEXT NOT NULL
                );
            ''')

    def add_question(self, q: question_set):
        question = q.question
        options = q.options
        answer = q.answer
        self._cursor.execute(
            '''
            INSERT INTO trivia (question, options, answer)
            VALUES (?, ?, ?);
                ''',
            (question, options, answer)
        )
        self._connection.commit()

    def get_question(self, index: int) -> question_set:
        self._cursor.execute(
            '''
            SELECT question, options, answer 
            FROM trivia
            WHERE id = ?
            ''',
            (index,)
        )
        q, o, a = self._cursor.fetchone()
        return question_set(question = q,
                            options = o,
                            answer = a)

    def delete_question(self, index):
        self._cursor.execute(
            '''
            DELETE
            FROM trivia
            WHERE id = ?
            ''',
            (index,)
        )
        self._connection.commit()

    def max_id(self) -> int:
        self._cursor.execute(
            '''
            SELECT MAX(id)
            FROM trivia;
            '''
        )
        return self._cursor.fetchone()[0]


