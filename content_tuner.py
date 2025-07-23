"""
ContentTuner: Adaptive writing engine for audience-aware narrative tuning.
See: https://your-substack-url-here (optional)
"""

# Define tone, audience, and voice presets
TONE_PROFILES = {
  "academic": {"formality": 0.9, "density": 0.85},
  "twitter": {"formality": 0.2, "punch": 0.95},
  "investor": {"clarity": 0.95, "compression": 0.9},
  "general": {"formality": 0.5, "clarity": 0.8},
}

def tune(text, profile):
  """Adjusts content characteristics based on selected profile."""
  params = TONE_PROFILES.get(profile, TONE_PROFILES["general"])
  # placeholder logic:
  return f"[{profile.upper()} TONE]\n{text.strip()}"

# Example usage
if __name__ == "__main__":
  input_text = "The algorithm is echoing back a version of yourself you didn’t approve."
  print(tune(input_text, "twitter"))
