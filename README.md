![Schema check](https://github.com/terryncew/openline-core/actions/workflows/validate.yml/badge.svg)

**Live hub:** https://terryncew.github.io/openline-hub/

# ContentTuner

**Adaptive writing engine for audience-aware narrative tuning.**

---

## What It Does
- **Profiles:** Pre-set tone and clarity profiles (`twitter`, `academic`, `investor`, `general`).
- **Transforms:** Removes filler, expands contractions, compresses sentences, and adjusts tone.
- **Metrics:** Shows placeholder values for `κ` (stress) and `ε` (entropy), hinting at deeper signal metrics.

This is the **first proof-of-concept** built on a universal compression framework (ULT), which can tune not just text, but any signal-based system.

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/terryncew/tuner-engine-or-ContentTuner.git
cd tuner-engine-or-ContentTuner
```

### 2. Run the tuner
```bash
python content_tuner.py
```

---

## Example Output
If you run the script, you’ll see how the same text is tuned for different profiles:

```text
[TWITTER TONE | f=0.20 d=0.30 c=0.90 cmp=0.90 p=0.95]
The algorithm is echoing back a version of yourself you didn’t approve.…

[ACADEMIC TONE | f=0.90 d=0.85 c=0.70 cmp=0.40 p=0.20]
The algorithm is echoing back a version of yourself you didn’t approve.

[INVESTOR TONE | f=0.80 d=0.70 c=0.95 cmp=0.80 p=0.60]
The algorithm is echoing back a version of yourself you didn’t approve.
```

---

## License
MIT License.  
See `LICENSE` for details.


