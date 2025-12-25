from flask import Flask, render_template, request
from skills import SKILLS
import logic

app = Flask(__name__)

@app.route("/")
def index():
    # Tu musíme poslať 'skills' (množné číslo), lebo index.html to tak vyžaduje
    return render_template("index.html", skills=SKILLS)
@app.route("/skill/<skill_name>", methods=["GET", "POST"])
def skill_detail(skill_name):
    # Skontrolujeme, či skill existuje v našom zozname
    if skill_name not in SKILLS:
        return "Skill not found", 404
        
    skill_data = SKILLS[skill_name]
    result = None

    if request.method == "POST":
        try:
            current_xp = int(request.form.get("current_xp", 0))
            target_level = int(request.form.get("target_level", 1))
            # Výpočet cez tvoju logic.py
            xp_needed = logic.calculate_xp_needed(current_xp, target_level)
            result = {"xp_needed": xp_needed}
        except ValueError:
            result = {"error": "Zadaj platné čísla!"}

    # Tu posielame 'skill' (dáta o jednom skille) a 'skill_key' (názov skillu)
    return render_template("skill.html", skill=skill_data, skill_key=skill_name, result=result)

if __name__ == "__main__":
    app.run(debug=True)
