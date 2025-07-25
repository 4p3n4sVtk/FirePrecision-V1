import os
from datetime import datetime

class LocationTracker:
    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        
    def log(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("logs/captures.txt", "a") as f:
            f.write(
                f"[{timestamp}]\n"
                f"SERVIÇO: {data['service']}\n"
                f"IP: {data['ip']}\n"
                f"GPS: {data['lat']}, {data['lon']}\n"
                f"USER-AGENT: {data['user_agent']}\n"
                f"-----------------------------------\n"
            )
        with open("logs/ips.txt", "a") as f:
            f.write(f"{data['ip']} | {timestamp}\n")