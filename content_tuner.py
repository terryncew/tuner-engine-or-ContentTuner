import re
from textwrap import shorten

TONE_PROFILES = {
    "academic": {"formality": 0.9, "density": 0.85, "clarity": 0.7, "compression": 0.4, "punch": 0.2},
    "twitter":  {"formality": 0.2, "density": 0.3,  "clarity": 0.9, "compression": 0.9, "punch": 0.95},
    "investor": {"formality": 0.8, "density": 0.7,  "clarity": 0.95,"compression": 0.8, "punch": 0.6},
    "general":  {"formality": 0.5, "density": 0.5,  "clarity": 0.8, "compression": 0.6, "punch": 0.5},
}

FILLER = {
    "basically","literally","actually","really","very","just","kind of","sort of",
    "in fact","in order to","in my opinion","in my view","it seems","honestly"
}

CONTRACTIONS = {
    "can't":"cannot","won't":"will not","isn't":"is not","I'm":"I am","you're":"you are",
    "they're":"they are","we're":"we are","it's":"it is","that's":"that is",
    "doesn't":"does not","don't":"do not","didn't":"did not","I'll":"I will",
}

def remove_fillers(text, strength):
    if strength < 0.4:
        return text
    # remove filler words/phrases
    def repl(m): 
        return ""
    for w in sorted(FILLER, key=len, reverse=True):
        text = re.sub(rf"\b{re.escape(w)}\b", "", text, flags=re.IGNORECASE)
    # collapse spaces
    return re.sub(r"\s{2,}", " ", text).strip()

def expand_contractions(text, strength):
    if strength < 0.7:
        return text
    for c, full in CONTRACTIONS.items():
        text = re.sub(rf"\b{re.escape(c)}\b", full, text)
        text = re.sub(rf"\b{re.escape(c.lower())}\b", full, text)
    return text

def shorten_sentences(text, compression, punch):
    # naive: if highly compressed or punchy, cut long sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    max_len = 180 - int(120 * max(compression, punch))  # 180 → 60 chars
    tuned = [shorten(s.strip(), width=max_len, placeholder="…") for s in sentences]
    return " ".join(tuned)

def densify(text, density):
    # naive densify: join short lines into fewer sentences (here we just leave as-is if density low)
    if density < 0.6:
        return text
    # merge double newlines, prefer longer paragraphs
    text = re.sub(r'\n{2,}', '\n', text)
    return text

def add_punch(text, punch):
    if punch < 0.7:
        return text
    # add hard breaks after short punchy statements and emphasize with em-dashes
    text = re.sub(r'(^|\.\s+)([A-Za-z][^\.!?]{0,60})([\.!?])', r'\1\2\3\n', text)
    return text.strip()

def tune(text: str, profile: str = "general") -> str:
    params = TONE_PROFILES.get(profile, TONE_PROFILES["general"])
    formality     = params.get("formality", 0.5)
    density       = params.get("density", 0.5)
    clarity       = params.get("clarity", 0.8)
    compression   = params.get("compression", 0.6)
    punch         = params.get("punch", 0.5)

    out = text.strip()

    # clarity: remove fillers first
    out = remove_fillers(out, clarity)

    # formality: expand contractions if formal
    out = expand_contractions(out, formality)

    # compression / punch: shorten long sentences
    out = shorten_sentences(out, compression, punch)

    # density: (placeholder) keep paragraphs tight if dense
    out = densify(out, density)

    # punch: add line breaks for emphasis
    out = add_punch(out, punch)

    header = f"[{profile.upper()} TONE | f={formality:.2f} d={density:.2f} c={clarity:.2f} cmp={compression:.2f} p={punch:.2f}]"
    return f"{header}\n{out}"

# Example
if __name__ == "__main__":
    input_text = "The algorithm is echoing back a version of yourself you didn’t approve. It’s actually kind of funny, but also really dangerous."
    print(tune(input_text, "twitter"))
    print()
    print(tune(input_text, "academic"))
