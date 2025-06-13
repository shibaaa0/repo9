from flask import Flask, request

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 100px;
    }}
    input, button {{
      padding: 10px;
      font-size: 16px;
      margin: 5px;
    }}
  </style>
</head>
<body>
  <h2>Nhập username GitHub để xem hồ sơ</h2>
  <form method="post">
    <input type="text" name="username" required>
    <button type="submit">Xem</button>
  </form>
</body>
</html>
"""

HTML_PROFILE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      margin: 40px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}

    .profile {{
      display: flex;
      align-items: center;
      justify-content: center;
      background: #ffffff;
      padding: 20px 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      gap: 40px;
    }}

    .avatar {{
      border-radius: 50%;
      width: 150px;
      height: 150px;
      object-fit: cover;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }}

    .stats img {{
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}

    a {{
      margin-top: 20px;
      text-decoration: none;
      color: #007BFF;
    }}
  </style>
</head>
<body>
  <div class="profile">
    <img src="https://github.com/{username}.png" alt="Avatar" class="avatar">

    <div class="stats">
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&custom_title={username}" alt="Top Languages">
    </div>
  </div>

  <a href="/">Home</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            return HTML_PROFILE.format(username=username)
    return HTML_FORM

if __name__ == "__main__":
    app.run(debug=True)
