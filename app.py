"""
app.py  --  Command Injection Demo  (Assignment 3, Variant: In-band)
Calls compiled C++ binaries: ./ping_vuln  and  ./ping_safe
"""
import os, subprocess
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder=".")

BASE = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_from_directory(BASE, "index.html")

@app.route("/ping/vuln", methods=["POST"])
def ping_vuln():
    host = request.json.get("host", "")
    binary = os.path.join(BASE, "ping_vuln")
    try:
        res = subprocess.run(
            [binary, host],       # calls the VULNERABLE C++ binary
            capture_output=True, text=True, timeout=10
        )
        return jsonify(output=res.stdout + res.stderr,
                       blocked=False,
                       ok=res.returncode == 0)
    except subprocess.TimeoutExpired:
        return jsonify(output="[timeout]", blocked=False, ok=False)

@app.route("/ping/safe", methods=["POST"])
def ping_safe():
    host = request.json.get("host", "")
    binary = os.path.join(BASE, "ping_safe")
    try:
        res = subprocess.run(
            [binary, host],       # calls the SECURE C++ binary
            capture_output=True, text=True, timeout=10
        )
        blocked = res.returncode != 0 and "BLOCKED" in (res.stdout + res.stderr)
        return jsonify(output=res.stdout + res.stderr,
                       blocked=blocked,
                       ok=res.returncode == 0)
    except subprocess.TimeoutExpired:
        return jsonify(output="[timeout]", blocked=False, ok=False)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
