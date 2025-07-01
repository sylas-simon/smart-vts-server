from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Global data to store vehicle info
latest_data = {
    "current_speed": 0,
    "speed_limit": 0,
    "is_overspeed": False,
    "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
}

@app.route('/update', methods=['POST'])
def update_vehicle_data():
    data = request.get_json()
    if not data or "speed" not in data or "speed_limit" not in data:
        return jsonify({"error": "Missing speed or speed_limit"}), 400

    try:
        speed = float(data["speed"])
        limit = float(data["speed_limit"])
    except ValueError:
        return jsonify({"error": "Invalid data format"}), 400

    latest_data["current_speed"] = speed
    latest_data["speed_limit"] = limit
    latest_data["is_overspeed"] = speed > limit
    latest_data["timestamp"] = time.strftime('%Y-%m-%d %H:%M:%S')

    return jsonify({"message": "Data updated"}), 200

@app.route('/api/vehicle-data')
def api_vehicle_data():
    return jsonify({
        "vehicle_id": "TZ 322 ABC",
        "location": "Kijitonyama",
        "vts_status": "Active",
        "driving_performance": "Good" if not latest_data['is_overspeed'] else "Overspeeding",
        "driver_name": "Simon sosola Sylas",
        "driver_license": "D123456789",
        "speed_limit": latest_data['speed_limit'],
        "current_speed": latest_data['current_speed'],
        "is_overspeed": latest_data['is_overspeed'],
        "last_updated": latest_data['timestamp'],
        "registration_number": "Asds-sd23-ds",
        "vehicle_type": "Truck",
        "contact_number": "+255629110284",
        "road_name": "Bagamoyo Road",
        "coordinates": "-6.7714281, 39.2399597"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
