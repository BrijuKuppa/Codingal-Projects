from flask import Flask, render_template, request
from get_response import generate

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def main():
    input_rf = None
    input_rb = None

    if request.method == "POST":
        if 'rfi' in request.form:
            reinforcemnt_input = request.form.get("rfi")
            if reinforcemnt_input:
                input_rf = generate(reinforcemnt_input)

        elif 'rbi' and 'rbs' in request.form:
            role = request.form.get("rbs")
            topic = request.form.get("rbi")
            if role == 'teacher':
                input_rb = generate(f"Explain {topic} as if I am a student learning from a teacher.")
            elif role == "expert":
                input_rb = generate(f"Explain {topic} as if I am learning from an expert professor")



    return render_template(
        "index.html",
        reinforcement_output=input_rf,
        role_based_output=input_rb
    )

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)