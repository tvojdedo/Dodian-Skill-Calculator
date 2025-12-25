from flask import Flask, render_template, request
from skills import SKILLS
import logic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", skills=SKILLS)


@app.route("/skill/<skill>", methods=["GET", "POST"])
def skill_detail(skill):
    if skill not in SKILLS or not SKILLS[skill]["enabled"]:
        return "Skill not available", 404

    result = None

    if request.method == "POST":
        data = {
            "current_level": request.form.get("current_level"),
            "current_xp": request.form.get("current_xp"),
            "target_level": request.form.get("target_level"),
            "target_xp": request.form.get("target_xp"),
        }

        clean = {k: int(v) for k, v in data.items() if v}
        result = logic.calculate(**clean)

    return render_template(
        "skill.html",
        skill=SKILLS[skill],
        skill_key=skill,
        result=result
    )


app.run(debug=True)
