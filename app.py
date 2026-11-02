
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GLITCH EFFECT</title>
<style>
* { box-sizing: border-box; }

body {
    margin: 0;
    background: #050505;
    color: #00ffcc;
    font-family: monospace;
    overflow: hidden;
}

.screen {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    animation: flicker 0.12s infinite;
}

h1 {
    font-size: clamp(25px, 8vw, 55px);
    text-shadow: 3px 0 red, -3px 0 blue;
    animation: shake 0.08s infinite;
}

p {
    color: white;
    animation: colors 0.3s infinite;
}

.lines {
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: repeating-linear-gradient(
        transparent 0px,
        transparent 3px,
        rgba(255,255,255,0.12) 4px
    );
}

@keyframes shake {
    0% { transform: translate(2px, -1px); }
    25% { transform: translate(-3px, 2px); }
    50% { transform: translate(3px, 1px); }
    75% { transform: translate(-1px, -2px); }
    100% { transform: translate(0, 0); }
}

@keyframes flicker {
    0%, 100% { background: #050505; }
    50% { background: #16001d; }
}

@keyframes colors {
    0% { color: #fff; }
    33% { color: #ff00ff; }
    66% { color: #00ffff; }
    100% { color: #fff; }
}
</style>
</head>
<body>
<div class="screen">
    <h1>⚡ GLITCH ⚡</h1>
    <p>تشويش بصري قوي</p>
    <div class="lines"></div>
</div>
</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
