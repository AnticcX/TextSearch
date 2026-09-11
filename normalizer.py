import unicodedata, re


def strip_diacritics(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    cleaned_chars = [char for char in decomposed if not unicodedata.combining(char)]
    return "".join(cleaned_chars)

def case_fold(text: str) -> str:
    return text.lower()

def tokenize(text: str) -> list[str]:
    normalized = strip_diacritics(case_fold(text)) 
    tokens = re.findall(r"\b\w+\b", normalized)
    return tokens

if __name__ == "__main__":
    sample_text = "Café, résumé, and naïve are words with diacritics."
    print("Original text:", sample_text)
    print("Tokens:", tokenize(sample_text))