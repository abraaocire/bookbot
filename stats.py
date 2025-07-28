def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    unique_characters = {}
    text = text.lower()
    for char in text:
        if char not in unique_characters:
            unique_characters[char] = 0
    for t in text:
        if t in unique_characters:
            unique_characters[t] += 1

    return unique_characters


def sort_on(chare):
    list = []
    for key, value in chare.items():
        dict = {}
        dict["char"] = key
        dict ["num"] = value
        list.append(dict)

    list.sort(key=lambda x: x["num"], reverse=True)
    return list

