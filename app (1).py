from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI is running"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data["question"]

    return jsonify({"answer": question})

if __name__ == "__main__":
    app.run()