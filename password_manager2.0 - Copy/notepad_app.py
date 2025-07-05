from flask import Flask, render_template, request, redirect, url_for, flash
from cryptography.fernet import Fernet
import os
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# ------------- ENCRYPTION KEY -------------
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    return open("key.key", "rb").read()

key = load_key()
fernet = Fernet(key)

# ------------- LOGIN PAGE -------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "khushi563":
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid password!", "danger")
    return render_template("login.html")

# ------------- DASHBOARD -------------
@app.route("/dashboard")
def dashboard():
    if not os.path.exists("notes.json"):
        with open("notes.json", "w") as f:
            json.dump({}, f)

    with open("notes.json", "r") as f:
        data = json.load(f)

    decrypted_notes = {}
    for title, content in data.items():
        decrypted_notes[title] = fernet.decrypt(content.encode()).decode()

    return render_template("dashboard.html", notes=decrypted_notes)

# ------------- ADD NEW NOTE -------------
@app.route("/add", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        encrypted_content = fernet.encrypt(content.encode()).decode()

        with open("notes.json", "r") as f:
            data = json.load(f)

        data[title] = encrypted_content

        with open("notes.json", "w") as f:
            json.dump(data, f, indent=4)

        return redirect(url_for("dashboard"))

    return render_template("add_note.html")

# ------------- EDIT NOTE -------------
@app.route("/edit/<title>", methods=["GET", "POST"])
def edit_note(title):
    with open("notes.json", "r") as f:
        data = json.load(f)

    if request.method == "POST":
        updated_content = request.form["content"]
        encrypted_content = fernet.encrypt(updated_content.encode()).decode()
        data[title] = encrypted_content

        with open("notes.json", "w") as f:
            json.dump(data, f, indent=4)

        return redirect(url_for("dashboard"))

    decrypted_content = fernet.decrypt(data[title].encode()).decode()
    return render_template("edit_note.html", title=title, content=decrypted_content)

# ------------- DELETE NOTE -------------
@app.route("/delete/<title>")
def delete_note(title):
    with open("notes.json", "r") as f:
        data = json.load(f)

    if title in data:
        del data[title]

    with open("notes.json", "w") as f:
        json.dump(data, f, indent=4)

    return redirect(url_for("dashboard"))

# ------------- RUN APP -------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
