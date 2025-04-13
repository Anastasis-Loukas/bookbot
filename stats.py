def count_words(book):
    words = book.split()
    return len(words)

def count_characters(book):
    count = dict()
    for c in book:
        if(c.lower() in count):
            count[c.lower()]+=1
        else:
            count[c.lower()] = 1
    return count

def sort_on(dict_item):
    return dict_item["count"]  # Return the count value for sorting

def sorted_dicts(dictionary):
    list_dict = []
    for char in dictionary:
        list_dict.append({"char": char, "count": dictionary[char]})
    list_dict.sort(reverse=True , key=sort_on)
    return list_dict
    

