#Adam's Text Analysis#
import os.path
import re
#import multiprocessing as mp, maybe someday I will get you working


class Analyser:
    __path = ""

    def __init__(self, path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\resources\\txt\\book"
                                                                                             ".txt"):
        if os.path.isfile(path) and path.endswith(".txt"):
            self.__path = path
        else:
            raise Exception(path + " is not a valid .txt file, ensure the location and file type are correct")

        print(self.__count_words())

    def __count_words(self):
        word_count = {}
        with open(self.__path, encoding="utf8") as file:
            for line in file:
                self.__count_line(word_count, line)

        file.close()
        return word_count

    def __count_line(self, word_count, line):
        for word in self.__format_string(line).split(" "):
            if word != "":
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    def __format_string(self, string):
        string = string.lower()
        string = re.sub(r"[^\w]", " ", string)
        string = string.replace("_", "")
        return string

myanalyser = Analyser()

