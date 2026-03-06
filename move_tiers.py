import os
import re

# 1. Update styles.css with the tier card styles
styles_file = "styles.css"
css_to_add = """
/* Tiers specific styles moved to global */
.tier-card {
    background: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 32px;
    padding: 60px 40px;
    text-align: center;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
}

.tier-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

.tier-title {
    font-family: var(--font-serif);
    font-size: 2.5rem;
    font-weight: 700;
    color: #111;
    margin-bottom: 16px;
}

.tier-price {
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--brand-red);
    margin-bottom: 32px;
}

.tier-features {
    list-style: none;
    text-align: left;
    margin-bottom: 40px;
    flex-grow: 1;
}

.tier-features li {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 16px;
    position: relative;
    padding-left: 32px;
    line-height: 1.5;
}

.tier-features li::before {
    content: '✦';
    position: absolute;
    left: 0;
    color: var(--brand-red);
    font-size: 1.2rem;
    line-height: 1.5;
}

.nuclear-badge {
    position: absolute;
    top: 24px;
    right: -32px;
    background: #111;
    color: #fff;
    padding: 8px 40px;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    transform: rotate(45deg);
}
"""
with open(styles_file, "r") as f:
    styles_content = f.read()
if ".tier-card" not in styles_content:
    with open(styles_file, "a") as f:
        f.write(css_to_add)

# 2. Inject into index.html
index_file = "index.html"
with open(index_file, "r") as f:
    index_html = f.read()

tier_section_html = """
        <!-- Pricing Tiers Grid -->
        <section class="fade-in-up delay-1" style="max-width: 1000px; margin: 0 auto 80px; padding: 0 20px;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2 class="section-title" style="font-size: 2.5rem;">Access & Architecture</h2>
                <p class="section-text" style="color: var(--text-muted);">Prove the engine works for free. Only pay when you are ready to listen.</p>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px;">
                <!-- Free Tier -->
                <div class="tier-card">
                    <div>
                        <h2 class="tier-title">The Overlay</h2>
                        <div class="tier-price">Free Forever</div>
                        <p class="section-text" style="margin-bottom: 32px;">Every time you match with a soul in the
                            gallery, you receive a foundational reading characterizing the immediate dynamic.</p>
                        <ul class="tier-features">
                            <li>Anonymous "Soul Gallery" matching.</li>
                            <li>High-level compatibility score via Ashtakoota.</li>
                            <li>A short summary of the intersection of your charts.</li>
                            <li>Access to the private Messenger interface.</li>
                        </ul>
                    </div>
                </div>

                <!-- Paid Tier -->
                <div class="tier-card" style="border-color: var(--brand-red);">
                    <div class="nuclear-badge">Uncut</div>
                    <div>
                        <h2 class="tier-title">The Readings</h2>
                        <div class="tier-price">Unlock The Archive</div>
                        <p class="section-text" style="margin-bottom: 32px;">When you discover a connection that demands
                            to be understood, unleash the military-grade psychological engine.</p>
                        <ul class="tier-features">
                            <li><strong>16 In-Depth PDFs</strong>: Over 50,000 words mapped across your individual
                                psyches and synastry.</li>
                            <li><strong>40-Minute Audiobooks</strong>: High-immersion spoken-word narrations of the
                                synastry.</li>
                            <li><strong>5 Metaphysical Systems</strong>: Western Astrology, Vedic Jyotish, Human Design,
                                Gene Keys, and Kabbalah.</li>
                            <li><strong>The Nuclear Option</strong>: Access the complete, uncompromising truth of the
                                relationship simultaneously.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
"""

# Insert right after the Hero section closing tag
if "<!-- Pricing Tiers Grid -->" not in index_html:
    index_html = index_html.replace('</header>\n\n    <!-- Split Sections for Features -->\n    <main class="content-sections">', '</header>\n\n    <main class="content-sections">\n' + tier_section_html)
    with open(index_file, "w") as f:
        f.write(index_html)

# 3. In Philosophy page, double check the Anti-swiping image
# I'll update it to an alternative if needed, but since we replaced it with philosophy_linocut.png,
# maybe the user wants a different image entirely. The user said "this image doesnt fit". 
print("Moved Tiers to index.html successfully.")
