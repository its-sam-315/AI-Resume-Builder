from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_resume():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    summary = request.form["summary"]
    skills = request.form["skills"]
    experience = request.form["experience"]
    education = request.form["education"]

    # Simple resume format for now
    resume_text = f"""
    Name: {name}
    Email: {email}
    Phone: {phone}

    Summary:
    {summary}

    Skills:
    {skills}

    Experience:
    {experience}

    Education:
    {education}
    """

    return f"<pre>{resume_text}</pre>"

if __name__ == "__main__":
    app.run(debug=True)
 
