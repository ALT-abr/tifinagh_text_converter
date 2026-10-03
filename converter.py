alphabet = {
    "a": "ⴰ",
    "b": "ⴱ",
    "c": "ⵛ",
    "č": "ⵛ",
    "d": "ⴷ",
    "ḍ": "ⴹ",
    "e": "ⴻ",
    "f": "ⴼ",
    "g": "ⴳ",
    "ǧ": "ⴵ",
    "h": "ⵀ",
    "ḥ": "ⵃ",
    "i": "ⵉ",
    "j": "ⵊ",
    "k": "ⴽ",
    "l": "ⵍ",
    "m": "ⵎ",
    "n": "ⵏ",
    "q": "ⵇ",
    "r": "ⵔ",
    "ṛ": "ⵕ",
    "s": "ⵙ",
    "ṣ": "ⵚ",
    "t": "ⵜ",
    "ṭ": "ⵟ",
    "u": "ⵓ",
    "w": "ⵡ",
    "x": "ⵅ",
    "y": "ⵢ",
    "z": "ⵣ",
    "ẓ": "ⵥ",
    "ɛ": "ⵄ",
    "ɣ": "ⵖ"
}

groupes = {
    "ch": "ⵛ",
    "gh": "ⵖ",
    "kh": "ⵅ"
}

accents = str.maketrans({
    "à": "a",
    "á": "a",
    "â": "a",
    "ä": "a",
    "ã": "a",
    "å": "a",
    "é": "e",
    "è": "e",
    "ê": "e",
    "ë": "e",
    "í": "i",
    "ì": "i",
    "î": "i",
    "ï": "i",
    "ó": "o",
    "ò": "o",
    "ô": "o",
    "ö": "o",
    "õ": "o",
    "ú": "u",
    "ù": "u",
    "û": "u",
    "ü": "u",
})

def remove_accents(message):
    return message.translate(accents)

def convert_to_tifinagh(message):
    message = remove_accents(message.lower())

    resultat = ""
    i = 0

    while i < len(message):
        groupe = message[i:i+2]

        if groupe in groupes:
            resultat += groupes[groupe]
            i += 2

        else:
            lettre = message[i]
            resultat += alphabet.get(lettre, lettre)
            i += 1

    return resultat