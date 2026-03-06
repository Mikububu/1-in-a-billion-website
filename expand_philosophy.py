import re
import os

phil_file = "/Users/michaelperinwogenburg/Desktop/big-challenge/1-in-a-billion-v2/website/philosophy.html"

# Read current content
with open(phil_file, "r") as f:
    html = f.read()

# The new massive content block to inject before the embedded audio section
massive_expansion = """
        <!-- The 5 Metaphysical Pillars -->
        <section class="fade-in-up" style="max-width: 1000px; margin: 0 auto 80px; text-align: left;">
            <div style="background: rgba(255, 255, 255, 0.5); padding: 40px; border-radius: 24px; border: 1px solid var(--border-color); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                
                <h2 class="section-title" style="font-size: 2.5rem; margin-bottom: 24px; text-align: center;">The 5 Pillars of Destiny</h2>
                <p class="section-text" style="margin-bottom: 40px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                    <em>1 in a Billion</em> operates on the absolute cutting edge of deterministic psychology. It does not ask you what your favorite movie is or whether you prefer dogs over cats. It calculates your fundamental energetic blueprint by synthesizing five of the most potent metaphysical systems in human history. 
                </p>

                <!-- Pillar 1: Vedic Jyotish -->
                <div style="display: flex; gap: 40px; flex-wrap: wrap; align-items: flex-start; margin-bottom: 40px;">
                    <div style="flex: 1; min-width: 280px; text-align: center;">
                        <img src="images/the_mirror.jpg" alt="Vedic Compatibility Wheel" style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);">
                    </div>
                    <div style="flex: 1; min-width: 280px;">
                        <h3 class="section-title" style="font-size: 1.8rem; margin-bottom: 16px; color: var(--primary-accent);">01. Vedic Jyotish & The Ashtakoota System</h3>
                        <p class="section-text" style="margin-bottom: 16px;">
                            The foundational matching logic of the app is driven by Vedic Astrology, specifically the deeply mathematical <em>Ashtakoota Milan</em>. This is not the generalized horoscope found in magazines; it is a meticulous, lunar-based calculation analyzing 36 specific points of energetic friction or harmony between two souls.
                        </p>
                        <p class="section-text" style="color: var(--text-muted); font-size: 0.95rem;">
                            The engine analyzes Nadi (nervous system compatibility), Bhakoot (emotional foundation), and Gana (temperamental alignment) to ensure that connections shown to you have the baseline structural integrity to survive the friction of a real human relationship.
                        </p>
                    </div>
                </div>

                <div style="height: 1px; background: var(--border-color); margin: 40px 0;"></div>

                <!-- Pillar 2: The Kabbalistic Tree of Life -->
                <div style="display: flex; gap: 40px; flex-wrap: wrap; align-items: flex-start; flex-direction: row-reverse; margin-bottom: 40px;">
                    <div style="flex: 1; min-width: 280px; text-align: center;">
                        <img src="images/the_architect.jpg" alt="Kabbalah Tree of Life" style="width: 100%; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);">
                    </div>
                    <div style="flex: 1; min-width: 280px;">
                        <h3 class="section-title" style="font-size: 1.8rem; margin-bottom: 16px; color: var(--primary-accent);">02. The Kabbalistic Tree of Life</h3>
                        <p class="section-text" style="margin-bottom: 16px;">
                            While Vedic astrology maps the environmental and karmic trajectory, Kabbalah maps the internal architecture of the soul. By calculating how the Sephirot (spheres of consciousness) interact between two charts, the engine reveals the exact nodes where power struggles, spiritual illumination, or profound creative synergy will occur.
                        </p>
                        <p class="section-text" style="color: var(--text-muted); font-size: 0.95rem;">
                            It answers the question: <em>How does your light alter their shadow, and how does their gravity affect your trajectory?</em>
                        </p>
                    </div>
                </div>

                <div style="height: 1px; background: var(--border-color); margin: 40px 0;"></div>

                <!-- Pillar 3 & 4: Human Design & Gene Keys -->
                <div style="margin-bottom: 40px;">
                    <h3 class="section-title" style="font-size: 1.8rem; margin-bottom: 16px; text-align: center; color: var(--primary-accent);">03 & 04. Human Design & The Gene Keys</h3>
                    <p class="section-text" style="margin-bottom: 16px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                        To understand the mechanics of the aura and cellular resonance, we integrate Human Design and the Gene Keys. Human Design shows the mechanical flow of energy—are you a Generator who needs to respond, or a Projector waiting for an invitation? How do your defined and undefined centers interact mechanically with a potential match?
                    </p>
                    <p class="section-text" style="margin-bottom: 16px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto; color: var(--text-muted); font-size: 0.95rem;">
                        The Gene Keys take this further, mapping the specific fears (Shadows), talents (Gifts), and ultimate spiritual potentials (Siddhis) locked inside your DNA. The engine calculates how a partner will trigger your shadows or elevate you into your genius.
                    </p>
                </div>

                <div style="height: 1px; background: var(--border-color); margin: 40px 0;"></div>

                <!-- Pillar 5: Western Tropical Synthesis -->
                <div style="margin-bottom: 40px;">
                    <h3 class="section-title" style="font-size: 1.8rem; margin-bottom: 16px; text-align: center; color: var(--primary-accent);">05. Western Tropical Psychological Synthesis</h3>
                    <p class="section-text" style="margin-bottom: 16px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                        Finally, Western Tropical Astrology provides the psychological narrative arc. It is the language of modern archetypes, showing how ego, identity, and personal ambition play out in the material world. It translates the deep soul architecture of Kabbalah and Vedic mechanics into the immediately recognizable language of modern psychology.
                    </p>
                </div>

                <p class="section-text" style="font-style: italic; color: var(--primary-accent); border-left: 4px solid var(--primary-accent); padding-left: 16px; margin-top: 40px;">
                    When combined, these five pillars generate an exhaustive, multi-dimensional rendering of human capability and connection. It is not guessing. It is structural diagnosis.
                </p>

            </div>
        </section>

        <!-- The 16 Readings Architecture -->
        <section class="fade-in-up" style="max-width: 1000px; margin: 0 auto 80px; text-align: left;">
            <div style="background: rgba(255, 255, 255, 0.5); padding: 40px; border-radius: 24px; border: 1px solid var(--border-color); box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <h2 class="section-title" style="font-size: 2.5rem; margin-bottom: 24px; text-align: center;">The Anatomy of a Match:<br>The 16 Readings</h2>
                <p class="section-text" style="margin-bottom: 40px; text-align: center; max-width: 800px; margin-left: auto; margin-right: auto;">
                    When you access the deep infrastructure of a connection, the engine produces over 50,000 words mapped across your psyches, delivered as a suite of intimate audiobooks. This is "The Nuclear Option."
                </p>

                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                    
                    <div style="padding: 24px; background: rgba(0,0,0,0.03); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">
                        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--text-light); margin-bottom: 12px;">1. The Core Imprint</h4>
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">A ruthless breakdown of individual ego structures. How you both operate in isolation before the collision of the relationship.</p>
                    </div>

                    <div style="padding: 24px; background: rgba(0,0,0,0.03); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">
                        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--text-light); margin-bottom: 12px;">2. The Nervous System</h4>
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">Vedic Nadi analysis determining if your energetic frequencies soothe or aggravate each other on a cellular level.</p>
                    </div>

                    <div style="padding: 24px; background: rgba(0,0,0,0.03); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">
                        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--text-light); margin-bottom: 12px;">3. The Trigger Profile</h4>
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">Mapping exactly where arguments will originate. Synthesizing Gene Key shadows and Human Design undefined centers.</p>
                    </div>

                    <div style="padding: 24px; background: rgba(0,0,0,0.03); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">
                        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--text-light); margin-bottom: 12px;">4. The Sexual Synastry</h4>
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">Uncompromising analysis of desire, physical compatibility, and the transmutation of sexual energy based on tantric markers.</p>
                    </div>

                    <div style="padding: 24px; background: rgba(0,0,0,0.03); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">
                        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--text-light); margin-bottom: 12px;">5. The Kabbalistic Friction</h4>
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">Where your souls compete for spiritual dominance or where they naturally align into a powerful creative hierarchy.</p>
                    </div>

                    <div style="padding: 24px; background: rgba(0,0,0,0.03); border-radius: 16px; border: 1px solid rgba(0,0,0,0.05);">
                        <h4 style="font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--text-light); margin-bottom: 12px;">6. The Final Verdict</h4>
                        <p style="font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--text-muted); line-height: 1.6;">The ultimate synthesis. Does this relationship have the structural integrity to survive time, or is it a brief karmic lesson?</p>
                    </div>

                </div>
            </div>
        </section>
"""

# Find the NotebookLM Embedded Audio Output section and inject before it
split_marker = "<!-- NotebookLM Embedded Audio Output -->"
if split_marker in html:
    parts = html.split(split_marker)
    final_html = parts[0] + massive_expansion + split_marker + parts[1]
    
    with open(phil_file, "w") as f:
        f.write(final_html)
    print("Massive expansion injected successfully.")
else:
    print("Could not find injection point.")
