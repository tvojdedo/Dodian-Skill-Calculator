from flask import Flask, render_template, request
from skills import SKILLS
import logic  # Toto teraz bude fungovať, lebo máš logic.py
import os

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
        try:
            # Získame dáta z formulára a prevedieme na int, ak existujú
            data = {
                "current_level": request.form.get("current_level"),
                "current_xp": request.form.get("current_xp"),
                "target_level": request.form.get("target_level"),
                "target_xp": request.form.get("target_xp"),
            }
            clean = {k: int(v) for k, v in data.items() if v and v.strip()}
            
            # Voláme funkciu calculate zo súboru logic.py
            result = logic.calculate(**clean)
        except Exception as e:
            result = {"error": str(e)}

    return render_template("skill.html", skill=SKILLS[skill], result=result)

if __name__ == "__main__":
    # Na Renderi musíme počúvať na porte, ktorý nám pridelia
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)