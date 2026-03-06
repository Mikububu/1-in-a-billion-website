import glob
import re

html_files = glob.glob("*.html")
for file in html_files:
    with open(file, "r") as f:
        content = f.read()
    
    # Remove the Access link
    new_content = re.sub(r'<a href="tiers\.html" class="nav-link.*?">Access</a>', '', content)
    
    with open(file, "w") as f:
        f.write(new_content)
    print(f"Updated {file}")
