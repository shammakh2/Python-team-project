#Adam's Text Analysis#
import os.path
import re
#import multiprocessing as mp, maybe someday I will get you working


class Analyser:
    __path = ""

    def __init__(self, path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\resources\\txt\\book"
                                                                                             ".txt"):
        """checks the file passed actually exists"""
        if os.path.isfile(path) and path.endswith(".txt"):
            self.__path = path
        else:
            raise Exception(path + " is not a valid .txt file, ensure the location and file type are correct")

    def count_words(self, raw = False):
        """counts how many times a word appears in the file"""
        word_count = {}
        with open(self.__path, encoding="utf8") as file:
            for line in file:
                self.__count_line(word_count, line, raw)
        file.close()
        return word_count

    def __count_line(self, word_count, line, raw = False):
        """counts how many times a word appears in a string"""
        if raw == False:
            line = self.__format_string(line)
        for word in line.split(" "):
            if word != "":
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    def __format_string(self, string):
        """removes non-alphanumeric characters and makes a string lowercase"""
        string = string.lower()
        string = re.sub(r"[^\w]", " ", string)
        string = string.replace("_", "")
        return string

