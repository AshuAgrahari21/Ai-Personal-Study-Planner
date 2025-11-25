from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import math

app = Flask(__name__)
CORS(app)

# Load sample data
with open('sample_data.json', 'r') as f:
    SAMPLE = json.load(f)

# Simple scheduler function
def generate_plan(user):
    tasks = []
    for subj in user['subjects']:
        for ch in subj['chapters']:
            tasks.append({
                'subject': subj['name'],
                'title': ch['title'],
                'est_hours': ch.get('est_hours', 1),
                'difficulty': ch.get('difficulty', 2)
            })

    # Priority = difficulty × hours
    for t in tasks:
        t['priority'] = t['difficulty'] * t['est_hours']

    # Highest priority first
    tasks.sort(key=lambda x: x['priority'], reverse=True)

    daily_hours = user.get('daily_hours', 4)
    plan = []
    day = 1
    remain = daily_hours
    plan.append({'day': day, 'slots': []})

    for t in tasks:
        hours = t['est_hours']
        while hours > 0:
            if hours <= remain:
                plan[-1]['slots'].append({**t, 'hours': hours})
                remain -= hours
                hours = 0
            else:
                plan[-1]['slots'].append({**t, 'hours': remain})
                hours -= remain
                day += 1
                remain = daily_hours
                plan.append({'day': day, 'slots': []})

    return plan

@app.route('/api/generate', methods=['POST'])
def api_generate():
    user = request.json
    plan = generate_plan(user)
    return jsonify({'plan': plan})

@app.route('/api/sample', methods=['GET'])
def api_sample():
    return jsonify(SAMPLE)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
