import datetime
import random

# A rotating list of high-utility study themes to keep content fresh on every sync
topics = [
    {"subject": "Mathematics", "topic": "Quadratic Equations & Polynomials", "tip": "Always check the discriminant $b^2 - 4ac$ first to determine the nature of roots."},
    {"subject": "Science", "topic": "Light Reflection & Refraction", "tip": "Remember the mirror formula: $\\frac{1}{f} = \\frac{1}{v} + \\frac{1}{u}$."},
    {"subject": "Social Science", "topic": "Nationalism in India", "tip": "Key milestones: Non-Cooperation (1920), Civil Disobedience (1930), Quit India (1942)."}
]

current_topic = random.choice(topics)
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Quick Revision Hub - {current_topic['subject']}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 650px; margin: 30px auto; padding: 20px; background: #f8f9fa; color: #212529; }}
        .card {{ background: #ffffff; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 5px solid #0066cc; }}
        .badge {{ background: #e7f1ff; color: #0066cc; padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; }}
        .footer {{ margin-top: 20px; font-size: 12px; color: #6c757d; text-align: center; }}
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">{current_topic['subject']}</span>
        <h2>{current_topic['topic']}</h2>
        <p><strong>Smart Revision Tip:</strong> {current_topic['tip']}</p>
        <hr style="border:0; border-top:1px solid #eee; margin:20px 0;">
        <p style="font-size: 14px;"><em>This revision card was autonomously generated and optimized via cloud sync.</em></p>
    </div>
    <div class="footer">
        Last Cloud Sync: {timestamp} UTC | Autonomous AI Worker
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html_content)

print("Automated study card generated and committed successfully.")
