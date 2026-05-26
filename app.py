from flask import Flask, render_template, request
import random

app = Flask(__name__)

questions = [
    {
        "question": "What is Python?",
        "answer": "python is a programming language"
    },
    {
        "question": "Explain OOPs concepts.",
        "answer": "class object inheritance polymorphism"
    },
    {
        "question": "What is Artificial Intelligence?",
        "answer": "ai is simulation of human intelligence"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/interview')
def interview():
    q = random.choice(questions)
    return render_template('interview.html', question=q['question'])

@app.route('/submit', methods=['POST'])
def submit():
    user_answer = request.form['answer'].lower()
    question = request.form['question']

    score = 0
    feedback = ""

    for q in questions:
        if q['question'] == question:
            correct_answer = q['answer']

            keywords = correct_answer.split()
            matched = 0

            for word in keywords:
                if word in user_answer:
                    matched += 1

            score = int((matched / len(keywords)) * 100)

            if score > 80:
                feedback = "Excellent Answer"
            elif score > 50:
                feedback = "Good Answer"
            else:
                feedback = "Need Improvement"

    return render_template('result.html',
                           score=score,
                           feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)