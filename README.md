# ContentTuner

Adaptive writing engine for audience-aware narrative tuning.

---

## 🚀 Quick Start

1. Clone or download this repo  
2. Run:
3. Generates demo outputs with different tone profiles.

3. Plug in your own OpenAI key to generate real content.

---

## 🧠 Philosophy

This project is based on the idea that *voice tuning* will be a core primitive in AI-native tooling—especially for writers, strategists, and cultural architects.

---

## ⚙️ Status

This is a sketch-level prototype.  
Not a full product yet, but outlines how voice models could be tuned dynamically from prompt-level compression.

---

## 📚 Read More

👉 [Substack essays explaining the framework](https://substack.com/@sirterrynce)

---

## 📜 License

MIT — free to use, remix, and extend.  
For commercial use or collaboration, feel free to reach out.

---

## 🔧 Code Snapshot

```python
TONE_PROFILES = {
"academic": {"formality": 0.9, "density": 0.85},
"twitter": {"formality": 0.2, "punch": 0.95},
"investor": {"clarity": 0.95, "compression": 0.9},
"general": {"formality": 0.5, "clarity": 0.8},
}

def tune(text, profile):
params = TONE_PROFILES.get(profile, TONE_PROFILES["general"])
return f"[{profile.upper()} TONE]\n{text.strip()}"

# Example usage
if __name__ == "__main__":
input_text = "The algorithm is echoing back a version of yourself you didn’t approve."
print(tune(input_text, "twitter"))
