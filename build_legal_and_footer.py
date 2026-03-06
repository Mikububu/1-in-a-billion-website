import os
import glob
import re

# 1. Parse and Adapt Legal Pages
def adapt_legal_page(file_path, title):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r") as f:
        html = f.read()

    # Extract just the post-content
    match = re.search(r'<div class="post-content">(.*?)</div>\s*<a href="/" class="back-link"', html, re.DOTALL)
    if not match:
        return
    
    content = match.group(1)

    # Text replacements to bring it from Forbidden Yoga -> 1 in a Billion
    content = content.replace("Forbidden Yoga", "1 in a Billion")
    content = content.replace("spiritual art performance project", "psychological dating application")
    content = content.replace("sessions, workshops, or events", "mobile application and services")
    content = content.replace("sessions, consultations, and events", "the application")
    content = content.replace("sessions or events", "the application")
    content = content.replace("participating in 1 in a Billion sessions", "using the 1 in a Billion application")
    content = content.replace("attend the scheduled session", "use the application appropriately")
    content = content.replace("artistic, educational, and personal development experiences", "a psychological matching service")
    content = content.replace("artistic and educational context", "technological context")
    content = content.replace("artistic and educational initiative", "technological initiative")

    # Build the 1 in a Billion wrapper
    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 1 in a Billion</title>
    <!-- Core Brand Styles -->
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
    <style>
        .legal-container {{
            max-width: 800px;
            margin: 120px auto 60px;
            padding: 0 20px;
        }}
        .legal-container h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            color: var(--primary-accent);
            margin-bottom: 2rem;
            text-align: center;
        }}
        .legal-content h2 {{
            font-family: 'Playfair Display', serif;
            color: var(--text-light);
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }}
        .legal-content h3 {{
            font-family: 'Inter', sans-serif;
            color: var(--primary-accent);
            font-size: 1.1rem;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }}
        .legal-content p, .legal-content li {{
            font-family: 'Inter', sans-serif;
            color: var(--text-muted);
            line-height: 1.7;
            margin-bottom: 1rem;
        }}
        .legal-content ul {{
            margin-bottom: 1.5rem;
            padding-left: 20px;
        }}
        .legal-content strong {{
            color: var(--text-light);
        }}
    </style>
</head>
<body>
    <!-- Global Navigation -->
    <nav class="global-nav">
        <a href="index.html" class="nav-logo">1 in a <span style="font-family: 'Playfair Display', serif; font-weight: 700; color: #a9856f;">Billion</span></a>
        <div class="nav-links">
            <a href="philosophy.html" class="nav-link">Philosophy</a>
            <a href="deep-matching.html" class="nav-link">The Engine</a>
            <a href="the-sound.html" class="nav-link">Sonic Signatures</a>
            <a href="deep-readings.html" class="nav-link">The Archive</a>
            <a href="tiers.html" class="nav-link">Access</a>
            <a href="about.html" class="nav-link">The Architects</a>
        </div>
    </nav>

    <div class="legal-container fade-in-up">
        <h1>{title}</h1>
        <div class="legal-content">
            {content}
        </div>
    </div>

    <!-- FOOTER PLACEHOLDER -->
</body>
</html>
"""
    with open(file_path, "w") as f:
        f.write(new_html)

adapt_legal_page("terms.html", "Terms & Conditions")
adapt_legal_page("privacy.html", "Privacy Policy")

# 2. Fix the Talking Head Video in Philosophy
phil_path = "philosophy.html"
if os.path.exists(phil_path):
    with open(phil_path, "r") as f:
        phil_html = f.read()
    
    # Revert the first video (anti_swipe.mp4) back to the static linocut image
    phil_html = re.sub(
        r'<video autoplay loop muted playsinline style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba\(0,0,0,0\.1\); border: 1px solid rgba\(0,0,0,0\.05\);"><source src="images/philosophy_anti_swipe\.mp4" type="video/mp4"></video>',
        r'<img src="images/philosophy_linocut.png" alt="Slow food for the nervous system linocut portrait" style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);">',
        phil_html
    )
    with open(phil_path, "w") as f:
        f.write(phil_html)

# 3. Apply the New Balanced Footer Globally
footer_html = """    <footer class="footer fade-in-up">
        <!-- Top section: App info -->
        <div style="margin-bottom: 25px;">
            <div class="logo" style="margin-bottom: 8px;">1 in a <span style="font-family: 'Playfair Display', serif; font-weight: 700; color: #a9856f;">Billion</span></div>
            <p style="margin-bottom: 0;">The Ultimate Psychological Mirror.</p>
        </div>

        <!-- Middle section: Legal links -->
        <div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 30px; font-size: 0.85rem;">
            <a href="terms.html" style="color: var(--text-muted); text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='var(--primary-accent)'" onmouseout="this.style.color='var(--text-muted)'">Terms & Conditions</a>
            <a href="privacy.html" style="color: var(--text-muted); text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='var(--primary-accent)'" onmouseout="this.style.color='var(--text-muted)'">Privacy Policy</a>
        </div>

        <!-- Bottom section: Developer info & backlink -->
        <div style="font-size: 0.85rem; color: var(--text-muted); display: flex; flex-direction: column; align-items: center; gap: 8px; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 20px; max-width: 300px; margin: 0 auto;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 15px; width: 100%;">
                <div style="text-align: right; line-height: 1.4;">
                    <p style="margin: 0; opacity: 0.8;">Developed by Michael Wogenburg</p>
                    <p style="margin: 0; opacity: 0.8;">Guru of <a href="https://forbidden-yoga.com" target="_blank" style="color: var(--primary-accent); text-decoration: none;">forbidden-yoga.com</a></p>
                </div>
                <div style="width: 1px; height: 30px; background-color: rgba(255,255,255,0.1);"></div>
                <a href="https://forbidden-yoga.com" target="_blank" style="display: flex; align-items: center; justify-content: center;">
                    <img src="images/forbidden-yoga-logo.png" alt="Forbidden Yoga Logo" style="height: 28px; filter: grayscale(100%) contrast(1.2); opacity: 0.5; transition: all 0.3s ease;" onmouseover="this.style.filter='none'; this.style.opacity='1'" onmouseout="this.style.filter='grayscale(100%) contrast(1.2)'; this.style.opacity='0.5'">
                </a>
            </div>
        </div>
    </footer>"""

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r") as f:
        content = f.read()
    
    # Check if this file has a placeholder footer from the new legal generation
    if "<!-- FOOTER PLACEHOLDER -->" in content:
        new_content = content.replace("<!-- FOOTER PLACEHOLDER -->", footer_html)
    else:
        # regex to find from <footer... to </footer>
        new_content = re.sub(r'<footer class="footer[^>]*>.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(new_content)
    print(f"Updated footer in {file}")

print("Done updating files.")
