"""
ContentTuner – 70-line demo of compression/emergence tuning
MIT Licence • github.com/terryncew/tuner-engine-or-ContentTuner
"""

from textwrap import shorten

# ------- presets (feel free to extend) ---------------------------------------
TONE_PROFILES = {
    "academic": {"formality": 0.9, "density": 0.85},
    "twitter":  {"formality": 0.2, "punch": 0.95},
    "investor": {"clarity": 0.95, "compression": 0.9},
    "general":  {"formality": 0.5, "clarity": 0.8},
}

# ------- tiny kernel ---------------------------------------------------------
def tune(text: str, profile: str = "general") -> str:
    """
    • looks up sliders for the chosen profile
    • does a visible toy transform (shorten, smart quotes, etc.)
    • returns κ (stress) & ε (entropy) placeholders so you see the hook
    """
    p = TONE_PROFILES.get(profile, TONE_PROFILES["general"])

    # demo: add "punch" by compressing to 70 chars
    if p.get("punch", 0) > 0.9:
        text = shorten(text, width=70, placeholder="…")

    # demo: add "density" by switching to smart quotes
    if p.get("density", 0) > 0.8:
        text = text.replace("'", "’")

    # fake κ / ε so interface is visible
    kappa    = round(1 - p.get("clarity", 0.8), 3)
    epsilon  = round(1 - p.get("compression", 0.5), 3)
    header   = f"[{profile.upper()} κ={kappa} ε={epsilon}]"
    return f"{header}\n{text.strip()}"

# ------- minimal CLI ---------------------------------------------------------
if __name__ == "__main__":
    sample = "The algorithm is echoing back a version of yourself you didn’t approve."
    for prof in ("twitter", "academic", "investor"):
        print(tune(sample, prof), "\n")
