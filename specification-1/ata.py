#Adam's Text Analysis#
import os.path
import matplotlib.pyplot as plot
import re
import matplotlib
#import multiprocessing as mp, maybe someday I will get you working


class Analyser:
    __path = ""
    __word_count = {}
    def __init__(self, path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\resources\\txt\\test"
                                                                                             ".txt"):
        """checks the file passed actually exists"""
        if os.path.isfile(path) and path.endswith(".txt"):
            self.__path = path
        else:
            raise Exception(path + " is not a valid .txt file, ensure the location and file type are correct")

    def count_words(self, raw = False):
        """counts how many times a word appears in the file"""
        if self.__word_count == {}:
            with open(self.__path, encoding="utf8") as file:
                for line in file:
                 self.__count_line(self.__word_count, line, raw)
            file.close()
        return self.__word_count

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

    def produce_graph(self):
        self.count_words()
        plot.bar(range(len(self.__word_count)), self.__word_count.values(), align='center')
        plot.xticks(range(len(self.__word_count)), list(self.__word_count.keys()))
        plot.show()

    def __format_string(self, string):
        """removes non-alphanumeric characters and makes a string lowercase"""
        string = string.lower()
        string = re.sub(r"[^\w]", " ", string)
        string = string.replace("_", "")
        return string

myanalyser = Analyser()
myanalyser.produce_graph()
