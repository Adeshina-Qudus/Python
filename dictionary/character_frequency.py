sample = "google.com"


def character_frequency(character: str):
    dictionary = {}
    for value in character:
        dictionary.update({value: character.count(value)})
    return dictionary


def character_frequency_counter(character: str):
    dictionary = {}
    dictionary.update({value: character.count(character) for value in character})
    return dictionary


print(character_frequency_counter(sample))