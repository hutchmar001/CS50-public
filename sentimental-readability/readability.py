# TODO
import cs50

def count_letters_and_words(text):
    global letters
    global words
    global sentences
    letters = 0
    words = 1
    sentences = 0

    for i in range(0, len(text)):
        if text[i] == ' ':
            words += 1
        elif text[i] == '.' or text[i] == '!' or text[i] == '?':
            sentences += 1
        elif text[i] != '\'' and text[i] != '\"':
            letters += 1

def main():
    text = input("Text: ")
    count_letters_and_words(text)
    l = letters / words * 100
    s = sentences / words * 100
    index = int(round(0.058 * l - 0.296 * s - 15.8))
    if index < 1:
        print("Before Grade 1")
    elif index > 15:
        print("Grade 16+")
    else:
        print("Grade", index)
    return 0

main()


