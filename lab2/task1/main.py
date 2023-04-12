import os
import re
import regexp




def number_of_sentences(text: str):
    count = len(re.findall(regexp.SENTENCE_PATTERN, text))

    quote_splitting = text.split("\"")
    for i in range(0, len(quote_splitting)):
        if i % 2 == 0 and i != 0:
            count += len(re.findall("^ [A-Z]", quote_splitting[i]))

            if i == len(quote_splitting) - 1 and quote_splitting[i] == "":
                count += 1
        elif i % 2 == 1:
            count -= len(re.findall(regexp.SENTENCE_PATTERN, quote_splitting[i]))

    count -= sum(initials.count(".") for initials in re.findall(regexp.INITIALS, text))

    for abbr in regexp.ONE_WORD_ABBREVIATIONS:
        count -= len(re.findall(abbr + "(?:,+| [a-z])", text))

    for abbr in regexp.NOT_END_ONE_WORD_ABBREVIATIONS:
        count -= len(re.findall(abbr, text))

    for abbr in regexp.TWO_WORDS_ABBREVIATIONS:
        count -= len(re.findall(abbr + "(?:,+| [a-z])", text)) * 2
        count -= len(re.findall(abbr + " [A-Z]", text))
        count -= len(re.findall(abbr + "$", text))

    return count



file = open(os.path.join(os.path.dirname(__file__), "data.txt"), "r")
text = file.readline()

print(number_of_sentences(text))