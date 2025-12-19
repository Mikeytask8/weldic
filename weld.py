hausa_dict = {"hello": "Sannu", "goodbye": "Sai an jima"}
yoruba_dict = {"hello": "E kú", "goodbye": "O dàbọ"}
swahili_dict = {"hello": "Jambo", "goodbye": "Kwa heri"}
zulu_dict = {"hello": "Sawubona", "goodbye": "Hamba kahle"}

languages = {
    "1": {"name": "Igbo", "dict": igbo_dict},
    "2": {"name": "Hausa", "dict": hausa_dict},
    "3": {"name": "Yoruba", "dict": yoruba_dict},
    "4": {"name": "Swahili", "dict": swahili_dict},
    "5": {"name": "Zulu", "dict": zulu_dict},
}

def translate_word(language, word):
    if language in languages:
        lang_dict = languages[language]["dict"]
        return lang_dict.get(word, "Word not found")
    return "Language not found"

def main():
    print("Choose a language:")
    for key, value in languages.items():
        print(f"{key}. {value['name']}")

    language = input("Enter language number: ")
    word = input("Enter English word: ").lower()

    print(translate_word(language, word))

if __name__ == "__main__":
    main()