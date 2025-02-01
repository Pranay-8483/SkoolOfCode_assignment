from flask import Flask, request, jsonify
import openai

app = Flask(_name_)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    tutor_character = data.get('character', 'Robot')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a friendly {tutor_character} who teaches Python to kids."},
            {"role": "user", "content": user_input}
        ]
    )
    return jsonify({"response": response['choices'][0]['message']['content']})

if _name_ == '_main_':
    app.run(debug=True)
