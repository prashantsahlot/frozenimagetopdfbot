from flask import Flask
import time

start_time = time.time()
app = Flask(__name__)

@app.route("/")
def home():
    uptime = round(time.time() - start_time)
    return {
        "status": "FrozenConverter is online ❄️",
        "uptime_sec": uptime,
        "ping_ms": round((time.time() - start_time) * 1000) % 300  # Simulated ping
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
