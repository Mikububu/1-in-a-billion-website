import os
import glob
import re

footer_html = """    <footer class="footer fade-in-up">
        <!-- Top section: App info -->
        <div style="margin-bottom: 25px;">
            <div class="logo" style="margin-bottom: 8px;">1 in a <span style="font-family: 'Playfair Display', serif; font-weight: 700; color: #a9856f;">Billion</span></div>
            <p style="margin-bottom: 0;">The Ultimate Psychological Mirror.</p>
        </div>

        <!-- Middle section: Legal links -->
        <div style="display: flex; gap: 20px; justify-content: center; margin-bottom: 40px; font-size: 0.85rem;">
            <a href="terms.html" style="color: var(--text-muted); text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='var(--primary-accent)'" onmouseout="this.style.color='var(--text-muted)'">Terms &amp; Conditions</a>
            <a href="privacy.html" style="color: var(--text-muted); text-decoration: none; transition: color 0.3s ease;" onmouseover="this.style.color='var(--primary-accent)'" onmouseout="this.style.color='var(--text-muted)'">Privacy Policy</a>
        </div>

        <!-- Bottom section: Developer info & backlink -->
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 20px; width: 100%; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 30px; padding-bottom: 20px;">
            <div style="text-align: center; line-height: 1.6; font-size: 0.9rem; color: var(--text-muted); font-family: 'Inter', sans-serif;">
                Developed by Michael Wogenburg<br>
                Guru of <a href="https://forbidden-yoga.com" target="_blank" style="color: var(--primary-accent); text-decoration: none; transition: opacity 0.3s ease;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">forbidden-yoga.com</a>
            </div>
            <a href="https://forbidden-yoga.com" target="_blank" style="display: inline-block;">
                <img src="images/forbidden-yoga-logo.png" alt="Forbidden Yoga Logo" style="height: 38px; filter: grayscale(100%) contrast(1.2); opacity: 0.6; transition: all 0.3s ease;" onmouseover="this.style.filter='none'; this.style.opacity='1'" onmouseout="this.style.filter='grayscale(100%) contrast(1.2)'; this.style.opacity='0.6'">
            </a>
        </div>
    </footer>"""

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r") as f:
        content = f.read()
    
    new_content = re.sub(r'<footer class="footer[^>]*>.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    with open(file, "w") as f:
        f.write(new_content)
    print(f"Updated footer in {file}")

print("Done updating files.")
