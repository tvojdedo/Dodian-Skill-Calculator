<link rel="stylesheet" href="/static/css/style.css">

<div class="container">
  <h1>{{ skill.name }}</h1>

  <form method="post">
    <label>Current Level</label>
    <input type="number" name="current_level">

    <label>Current XP</label>
    <input type="number" name="current_xp">

    <label>Target Level</label>
    <input type="number" name="target_level">

    <label>Target XP</label>
    <input type="number" name="target_xp">

    <button>Calculate</button>
  </form>

  {% if result %}
    <div class="result">
      <p>Current level: <strong>{{ result.current_level }}</strong></p>
      <p>Current XP: <strong>{{ result.current_xp }}</strong></p>
      <p>Target level: <strong>{{ result.target_level }}</strong></p>
      <p>Target XP: <strong>{{ result.target_xp }}</strong></p>
      <p>XP needed: <strong>{{ result.xp_needed }}</strong></p>
    </div>
  {% endif %}

  <div class="footer">
    <a href="/">← Back to skills</a>
  </div>
</div>