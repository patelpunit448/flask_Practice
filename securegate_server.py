import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for active scans
scans = {}

@app.route("/api/v1/pipeline/start", methods=["POST"])
def pipeline_start():
    scan_id = str(uuid.uuid4())
    scans[scan_id] = {
        "deployment_decision": "APPROVED",
        "security_score": 100,
        "sonar_quality_gate": "OK",
        "finding_counts": {},
        "tool_status": "SUCCESS",
        "findings": [],
    }
    print(f"[*] Started pipeline scan ID: {scan_id}")
    return jsonify({"scan_id": scan_id}), 200

@app.route("/api/v1/scans/<scan_id>/<tool>", methods=["POST"])
def upload_report(scan_id, tool):
    print(f"[*] Received report for tool: {tool} on scan ID: {scan_id}")
    return jsonify({"status": "received"}), 200

@app.route("/api/v1/scans/<scan_id>", methods=["GET"])
def get_scan(scan_id):
    scan_data = scans.get(
        scan_id,
        {
            "deployment_decision": "APPROVED",
            "security_score": 100,
            "sonar_quality_gate": "OK",
            "finding_counts": {},
            "tool_status": "SUCCESS",
            "findings": [],
        },
    )
    return jsonify(scan_data), 200

@app.route("/api/v1/pipeline/complete", methods=["POST"])
def pipeline_complete():
    print("[*] Pipeline completed successfully!")
    return jsonify({"status": "completed"}), 200

# if __name__ == "__main__":
# #     app.run(port=8080)
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5050)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

