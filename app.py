from flask import Flask, render_template, request, jsonify
from scanner.engine import ScannerEngine
from scanner.sqli import SQLiScanner
from scanner.xss import XSSScanner
from scanner.headers import HeaderScanner
from scanner.subdomain import SubdomainScanner
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    url = data.get("url", "").strip()
    run_subdomains = data.get("subdomains", False)

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url

    try:
        engine = ScannerEngine(url)
        findings = []
        discovered_subdomains = []

        # Security headers
        findings += HeaderScanner(engine).scan(url)

        # SQLi
        findings += SQLiScanner(engine).scan(url)

        # XSS
        findings += XSSScanner(engine).scan(url)

        # Subdomain enumeration (optional)
        if run_subdomains:
            _, discovered_subdomains = SubdomainScanner(engine).scan(url)

        total = len(findings)

        return jsonify({
            "url": url,
            "total": total,
            "findings": findings,
            "subdomains": discovered_subdomains,
        })

    except requests.exceptions.ConnectTimeout:
        return jsonify({"error": "Connection timed out. The target site may be down or blocking requests."}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Could not connect to the target. Check the URL and your internet connection."}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
