from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="templates")

# Global variable to store status (True = Red, False = White)
status_data = {"status": False}


# 📌 ROUTE 1: Frontpage (HTML)
@app.route("/")
def index():
    return render_template("index.html", status=status_data["status"])


# ROUTE 2: API endpoint to update status
@app.route("/update", methods=["POST"])
def update_status():
    global status_data
    data = request.get_json()
    if "status" in data:
        status_data["status"] = data["status"]
        print(f"Status updated: {data["status"]}")
        return jsonify({"message": "Status updated"}), 200
    return jsonify({"error": "Invalid data"}), 400


# ROUTE 3: API endpoint to fetch status
@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(status_data)


# Start Flask server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
