# python
def count_words(text):
    return len(text.split())

def sort_on(item):
    return item["num"]

def count_characters(text):
    counts = {}
    for ch in text.lower():
        if ch.isalpha():
            counts[ch] = counts.get(ch, 0) + 1

    result = [{"char": ch, "num": n} for ch, n in counts.items()]
    result.sort(reverse=True, key=sort_on)
    return result