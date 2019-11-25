import re
"""
        Library used to normalize csv data
                Date: 22/11/2019
                Willian Antunes
            wiliam-m-@hotmail.com
"""

#Transform genres in list of strings

def split_genres(genres):
    new_genres = []

    for i, items in enumerate(genres):
        new_genres.insert(i, items.split('},'))

    return new_genres

#transform object re in list of strings

def transform_to_list(list):
    variable = ""
    for o in list:
        if o == None:
            return None
        else:
            variable += str(o.group(1)) + "|"
    return variable[:-1]


#Using regular expression colect genres

def transform_to_str(new_genres):
    genres_str = []
    new_genres_str = []
    for i_n, items_n in enumerate(new_genres):
        for i_k in items_n:
            new_genres_str.append(re.search(r'"name": "(.*?)"', i_k))
        genres_str.append(transform_to_list(new_genres_str))
        new_genres_str.clear()
    return genres_str