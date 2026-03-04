from tifinagh_dict import latin_to_tifinagh, tifinagh_to_latin

def to_tifinagh(text):
    resultat = []
    
    for letter in text:
        letter = remove_accents(letter)
        if letter in latin_to_tifinagh:
            resultat.append(latin_to_tifinagh[letter])
        elif letter in tifinagh_to_latin:
            resultat.append(tifinagh_to_latin[letter])
        else:
            resultat.append(letter)
    
    return "".join(resultat)

def remove_accents(letter):
    if letter not in ("é","è","ê","ë","à","â","î","ï","ô","ù","û","ü","ç"):
        return letter
    elif letter in ("é", "è", "ê", "ë"):
        return "e"
    elif letter in ("à", "â"):
        return "a"
    elif letter in ("î", "ï"):
        return "i"
    elif letter in ("ô"):
        return "o"
    elif letter in ("ù", "û", "ü"):
        return "u"
    elif letter == "ç":
        return "c"
    else:
        return letter