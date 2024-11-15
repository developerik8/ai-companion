# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('health_companion.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS health_metrics
                 (id INTEGER PRIMARY KEY, step_count INTEGER, heart_rate INTEGER, calories INTEGER)''')
    conn.commit()
    conn.close()

# Home route, renders the index.html page
@app.route('/')
def home():
    return render_template('index.html')

# API route to fetch health metrics
@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    conn = sqlite3.connect('health_companion.db')
    c = conn.cursor()
    c.execute('SELECT * FROM health_metrics ORDER BY id DESC LIMIT 1')
    metrics = c.fetchone()
    conn.close()
    return jsonify({
        'steps': metrics[1],
        'heart_rate': metrics[2],
        'calories': metrics[3]
    })

# API route to save health metrics
@app.route('/api/metrics', methods=['POST'])
def save_metrics():
    data = request.get_json()
    steps = data['steps']
    heart_rate = data['heart_rate']
    calories = data['calories']
    
    conn = sqlite3.connect('health_companion.db')
    c = conn.cursor()
    c.execute('INSERT INTO health_metrics (step_count, heart_rate, calories) VALUES (?, ?, ?)', 
              (steps, heart_rate, calories))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Metrics saved successfully'}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
