from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

file_path = "D:/Christie_D/code/internship_stuff/Script-Extraction/Script/session.json"

@app.route('/log_click', methods=['POST'])
def log_click():
    data = request.json
    print("Received data:", data)  # Log the received data

    if not data or 'timestamp' not in data or 'element' not in data or 'page' not in data:
        print("Invalid data received")  # Log invalid data
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

    # Load existing data
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = {}
    else:
        existing_data = {}

    # Ensure the page entry exists
    page_name = data['page']
    if page_name not in existing_data:
        existing_data[page_name] = []

    # Append click details to the corresponding page
    existing_data[page_name].append({
        'timestamp': data['timestamp'],
        'element': data['element'],
        'textContent': data['textContent'],
        'x': data['x'],
        'y': data['y']
    })

    # Save updated data
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
    
    print("Data saved successfully")  # Log successful save

    processed_data = {
        'status': 'success',
        'message': f"Received click on {data.get('element', 'unknown element')}",
        'received_at': data['timestamp']
    }

    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
