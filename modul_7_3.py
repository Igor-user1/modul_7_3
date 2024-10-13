class WordsFinder:
    file_names = []
    all_words = {}

    def __init__(self, *args):
        self.file_names.append(*args)

    def get_all_words(self):
        words = []
        for j in range(len(self.file_names)):
            with open(self.file_names[j]) as file:
                for line in file:
                    line = str(line).lower()
                    for i in range(len(line)):
                        if line[i:i+1] in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                            line = str(line[:i]) + str(line[i+1:])
                    words_line = line.split()
                    for k in words_line:
                        words.append(k)
            self.all_words[self.file_names[j]] = words
        return self.all_words

    def find(self, word):
        new_dict = {}
        word = str(word).lower()
        self.get_all_words()
        for key in self.all_words:
            if word in self.all_words[key]:
                list_1 = list(self.all_words[key])
                for i in list_1:
                    if i == word:
                        new_dict[key] = int(list(list_1).index(i)) + 1
        return new_dict

    def count(self, word):
        new_dict_2 = {}
        d = 0
        word = str(word).lower()
        self.get_all_words()
        for key in self.all_words:
            if word in list(self.all_words[key]):
                for i in range(len(list(self.all_words[key]))):
                    if list(self.all_words[key])[i] == word:
                        d += 1
            new_dict_2[key] = d
        return new_dict_2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
