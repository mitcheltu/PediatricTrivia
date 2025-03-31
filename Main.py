from Generate import get_questions
from SaveData import Save
import random

if __name__ == '__main__':
    db = Save()
    index = random.randint(1, db.max_id())

    print('[A]dd Questions,\n[S]tart Trivia\n...')
    user = input().upper()
    while True:
        if user == 'A':
            print('How many questions?: ')
            num_questions = int(input())
            print('Generating...')
            question_list = get_questions(num_questions)
            print('Adding questions to databse...')
            for question in question_list:
                db.add_question(question)
            print('Succesfully added.')
            print('...\n[A]dd Questions\n[S]tart Trivia')
            user = input().upper()

        elif user == 'S' or user == 'C':
            try:
                q = db.get_question(index)
                print(q.question)
                print(q.options)
                print('Choice (A,B,C,D): ')
                user = input().upper()
                if user == q.answer:
                    print('Correct!')
                else:
                    print(f'Incorrect. The correct answer was {q.answer}')

                print('...\n[A]dd Questions\n[C]ontinue\n[D]elete Question')
                user = input().upper()
                if user == 'D':
                    db.delete_question(index)
                    print('Question Deleted.')
                    print('...\n[A]dd Questions\n[C]ontinue')
                    user = input().upper()
                index = random.randint(1, db.max_id())
            except TypeError:
                if 1 <= index <= db.max_id():
                    index = random.randint(1, db.max_id())
                    user = 'C'
                else:
                    print('Questions Must Be Added to Continue.')
                    user = 'A'



