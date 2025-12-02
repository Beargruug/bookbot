def get_count_words(text):
    return len(text.split())


def get_count_chars(text):
    result = {}
    lower_text = text.lower()
    splitted = lower_text.split()

    for c in splitted:
        for i in c:
            result[i] = lower_text.count(i)

    return result


def sort_list(dir):
    li = list(dir.items())
    sorted_list = list(li)
    result = [{"name": name, "num": num} for name, num in sorted_list]
    result.sort(reverse=True, key=sort_on)
    return result


def sort_on(items):
    return items["num"]
