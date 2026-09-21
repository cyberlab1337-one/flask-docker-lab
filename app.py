from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Docker Lab</title>
            <style>
                body {
                    margin: 0;
                    height: 100vh;
                    background-color: #121212;
                    color: #ffffff;

                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;

                    font-family: Arial, sans-serif;
                }

                h1 {
                    font-size: 48px;
                    margin-bottom: 20px;
                }

                .whale {
                    font-size: 140px;
                }
            </style>
        </head>

        <body>
            <h1>Hello from Flask in Docker!</h1>
            <div class="whale">🐳</div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
