import datetime

timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auto Study Hub</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 40px auto; padding: 20px; background: #f4f4f9; color: #333; }}
        .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <div class="card">
        <h2>Automated Daily Revision Resource</h2>
        <p>This page updates itself autonomously via Cloud AI Worker.</p>
        <p><strong>Last Cloud Sync:</strong> {timestamp} UTC</p>
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("index.html successfully generated and updated by cloud worker.")
