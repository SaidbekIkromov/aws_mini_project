from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Database connection configuration
DB_HOST = "saidbek.c1s864qewj81.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "qwerty12345"

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/timetable', methods=['GET'])
def timetable():
    level = request.args.get('level')
    if not level:
        return "Please select a level.", 400

    connection = get_connection()
    cursor = connection.cursor()

    # Fetch timetable data based on level
    cursor.execute("SELECT * FROM timetable WHERE level = %s", (level,))
    timetable_data = cursor.fetchall()

    connection.close()

    return render_template('timetable.html', timetable=timetable_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
