from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from PostgreSQL!'")
    message = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return f"""
    <html>
        <head>
            <title>Docker Lab</title>
            <style>
                body {{
                    margin: 0;
                    height: 100vh;
                    background-color: #121212;
                    color: white;

                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;

                    font-family: Arial, sans-serif;
                }}

                h1 {{
                    font-size: 48px;
                }}

                .humble-frog {{
                    font-size: 140px;
                }}

                .database {{
                    font-size: 24px;
                    margin-top: 20px;
                }}
            </style>
        </head>

        <body>
            <h1>Flask running in Docker</h1>

            <div class="humble-frog">
                🐸
            </div>

            <div class="database">
                {message}
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)