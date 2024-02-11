import socket
from uuid import getnode as get_mac
from flask import Flask,jsonify

# Get device details
def get_device_details():
	hostname = socket.gethostname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	MAC_address = get_mac()
	MAC_address = (':'.join(("%012X" % MAC_address)[i:i+2] for i in range(0, 12, 2)) ).replace(":", "-")
	return hostname,ip,MAC_address
	
app = Flask(__name__)

# Returns device hostname,IP and MAC address
@app.route("/details")
def details():
    hostname,ip,mac = get_device_details()
    return jsonify(
        HOSTNAME=hostname,
        MAC_ID=mac,
        IP=ip
    )

@app.route("/")
@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
	