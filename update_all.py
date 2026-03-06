import os
import glob
import re

# 1. Update Philosophy Page Images -> Videos
phil_path = "philosophy.html"
if os.path.exists(phil_path):
    with open(phil_path, "r") as f:
        phil_html = f.read()
    
    # Replace linocut image with video
    phil_html = re.sub(
        r'<img src="images/philosophy_linocut\.png"[^>]+>',
        r'<video autoplay loop muted playsinline style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);"><source src="images/philosophy_anti_swipe.mp4" type="video/mp4"></video>',
        phil_html
    )
    # Replace clay image with floating man video
    phil_html = re.sub(
        r'<img src="images/philosophy_clay\.jpg"[^>]+>',
        r'<video autoplay loop muted playsinline style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);"><source src="images/philosophy_slow_food.mp4" type="video/mp4"></video>',
        phil_html
    )
    with open(phil_path, "w") as f:
        f.write(phil_html)

# 2. Update Tiers Page Nuclear Option -> Video
tiers_path = "tiers.html"
if os.path.exists(tiers_path):
    with open(tiers_path, "r") as f:
        tiers_html = f.read()
    
    tiers_html = re.sub(
        r'<img src="images/broken_pot_verdict\.jpg"[^>]+>',
        r'<video autoplay loop muted playsinline style="width: 100%; border-radius: 20px; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.1);"><source src="images/tiers_nuclear.mp4" type="video/mp4"></video>',
        tiers_html
    )
    with open(tiers_path, "w") as f:
        f.write(tiers_html)

# 3. Global Footer Update
footer_html = """    <footer class="footer fade-in-up">
        <div class="logo" style="margin-bottom: 8px;">1 in a <span style="font-family: 'Playfair Display', serif; font-weight: 700; color: #a9856f;">Billion</span></div>
        <p style="margin-bottom: 24px;">The Ultimate Psychological Mirror.</p>
        <div style="font-size: 0.9rem; color: var(--text-muted); display: flex; flex-direction: column; align-items: center; gap: 8px;">
            <p style="margin: 0;">Developed by Michael Wogenburg</p>
            <p style="margin: 0;">Guru of <a href="https://forbidden-yoga.com" target="_blank" style="color: var(--primary-accent); text-decoration: none;">forbidden-yoga.com</a></p>
            <a href="https://forbidden-yoga.com" target="_blank" style="margin-top: 12px; display: inline-block;">
                <img src="images/forbidden-yoga-logo.png" alt="Forbidden Yoga Logo" style="height: 32px; filter: grayscale(100%) contrast(1.2); opacity: 0.7; transition: all 0.3s ease;" onmouseover="this.style.filter='none'; this.style.opacity='1'" onmouseout="this.style.filter='grayscale(100%) contrast(1.2)'; this.style.opacity='0.7'">
            </a>
        </div>
    </footer>"""

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r") as f:
        content = f.read()
    
    # regex to find from <footer... to </footer>
    new_content = re.sub(r'<footer class="footer[^>]*>.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(new_content)
    print(f"Updated footer in {file}")

print("Done updating files.")
