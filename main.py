def count_chars(text: str) -> list[dict[str, int | str]]:
    text = text.lower()
    counts: dict[str, int] = {}
    for ch in text:
        if counts.get(ch, None) == None:
            counts[ch] = 0
        counts[ch] += 1
    return [{"char": ch, "count": c} for ch, c in counts.items() if ch.isalpha()]


def print_char_counts(counts: list[dict[str, int | str]]):
    counts.sort(key=lambda i: i["count"], reverse=True)
    for c in counts:
        print(f"The '{c["char"]}' character was found {c["count"]} times")


def main():
    content: str = None
    path: str = "books/frankenstein.txt"
    
    with open(path, 'rt') as f:
        content = f.read()
    
    words = content.split()
    character_counts = count_chars(content)
    
    print(f"--- Begin report of {path} ---")
    print(f"{len(words)} words found in the document")
    print_char_counts(character_counts.copy())


main()