import requests
import json
from collections import namedtuple
question_set = namedtuple('question_set',
                          ['question', 'options', 'answer'])
option_to_num = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3}

def get_questions(num: int) -> list[question_set]:
    question_list = []
    response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers = {
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        },
        data = json.dumps({
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [
                {
                    "role": "user",
                    "content": f"Give me {str(num)} more questions about pediatrics with 4 possible answers each with the correct answer shown, in format ###**question** **options** **answer letter**###, nothing before or after."
                }
            ],

        })
    )
    #choices -> [0] -> message -> content
    ai_output = response.json()['choices'][0]['message']['content']
    questions = ai_output.split('\n')
    assert len(questions) == num
    questions = [question.strip().strip('###').strip('**') for question in questions]
    questions = [question.split('** **') for question in questions]
    for i in range(len(questions)):
        parts = questions[i]
        question_list.append(question_set(question = parts[0],
                                          options = parts[1],
                                          answer = parts[2][-1]))

    return question_list

