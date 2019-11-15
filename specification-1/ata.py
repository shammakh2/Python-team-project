#Adam's Text Analysis#
import os.path
import matplotlib.pyplot as plot
import re
import csv
#import multiprocessing as mp, maybe someday I will get you working


class Analyser:
    __path = ""
    __word_count = {}
    __character_count = {}
    def __init__(self, path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] + "\\resources\\txt\\book"
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
        self.__word_count = self.__order_dictionary(self.__word_count)
        return self.__word_count

    def count_characters(self, raw = False):
        """counts character frequency"""
        self.count_words(raw)
        if self.__character_count == {}:
            for key in self.__word_count:
                for character in key:
                  self.__count_char(self.__character_count, character, self.__word_count[key])
            self.__character_count = self.__order_dictionary(self.__character_count)
        return self.__character_count

    def most_freq(self, quantity, filepath="words.csv"):
        """produces a csv file of the most frequent words"""
        self.count_words()
        if quantity > len(self.__word_count):
            raise Exception("Depth of " + str(quantity) + " is greater than the quantity of unique words")
        else:
            with open(filepath, "w+") as csvfile:
                writer = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
                counter = 0
                for key in self.__word_count:
                    if counter == quantity:
                        break
                    else:
                        writer.writerow([key, self.__word_count[key]])
                        counter += 1
            csvfile.close()

    def produce_findings(self, num_of_words=10, filepath="FINDINGS.MD"):
        self.count_characters()
        file = open(filepath, "w+", encoding="utf-8")
        file.write("### Findings\n")
        file.write("\n")
        file.write(f"The {str(num_of_words)} most frequent words are: \n")
        counter = 0
        for key in self.__word_count:
            if counter == num_of_words:
                break
            else:
                file.write(f"* {key} with {str(self.__word_count[key])}\n")
                counter += 1
        file.write("\n")
        file.write("The frequency of each character is: \n")
        for key in self.__character_count:
            file.write(f"* {key} - {str(self.__character_count[key])}\n")
        file.close()


    def __count_char(self, char_count, char, value):
        if char in char_count:
            char_count[char] += 1*value
        else:
            char_count[char] = 1*value


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

    def word_graph(self):
        """"produces a bar chart of the word frequency"""
        self.count_words()
        self.__produce_graph(self.__word_count)

    def char_graph(self):
        """produces a bar chart of the character frequency"""
        self.count_characters()
        self.__produce_graph(self.__character_count)

    def __order_dictionary(self, dictionary):
        """sorts a dictionary in descending order of the value"""
        templist = []
        for key in dictionary:
            templist.append((key, dictionary[key]))

        templist = sorted(templist, key=lambda x: x[1], reverse=True)
        return dict(templist)

    def __format_string(self, string):
        """removes non-alphanumeric characters and makes a string lowercase"""
        string = string.lower()
        string = re.sub(r"[^\w]", " ", string)
        string = string.replace("_", "")
        return string

    def __produce_graph(self, dictionary):
        """produces a graph of a dictionary"""
        plot.bar(range(len(dictionary)), dictionary.values(), align='center')
        plot.xticks(range(len(dictionary)), list(dictionary.keys()))
        plot.show()
