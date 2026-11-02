
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
    margin: 0;
    background: black;
    overflow: hidden;
}
.glitch {
    width: 100vw;
    height: 100vh;
    background: repeating-linear-gradient(
        0deg, black 0px, black 2px,
        #333 3px, black 4px
    );
    animation: shake 0.08s infinite;
}
@keyframes shake {
    0% { transform: translate(2px,1px); }
    50% { transform: translate(-2px,-1px); }
    100% { transform: translate(1px,2px); }
}
</style>
</head>
<body>
<div class="glitch"></div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
