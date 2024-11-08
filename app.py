from flask import Flask, request
from chatbot.chat import get_response
import os

app = Flask(__name__)

@app.route('/api/response', methods=['POST'])
def response():
  body = request.get_json()
  prompt = body['prompt']
  return get_response(prompt)


if __name__ == "__main__":
  os.system('clear')
  app.run(debug=True)
