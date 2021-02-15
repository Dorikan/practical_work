import re
import codecs
import pymorphy2 # $ pip install pymorphy2


class analyzer:

    def __init__(self, file=None):
        self.pattern = re.compile('[A-zА-яё]*')
        self.a = open(file, 'r').read().split(' ')
        self.first_list = []
        self.second_list = []
        self.functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
        self.x = []
        self.endDict = {}

    def start(self):
        self.make_x_list()
        self.check_words()
        self.create_dict()



    # noinspection SpellCheckingInspection
    @staticmethod
    def pos(word, morth=pymorphy2.MorphAnalyzer()):
        return morth.parse(word)[0].tag.POS

    def dict_enumerator(self, d):
        for i in dict(d):
            if d[i] == 1:
                d.pop(i)
            elif self.pos(i) in self.functors_pos:
                d.pop(i)
                
    def mem_clean(self):
        del self.x
        del self.second_list
        del self.first_list

    def make_x_list(self):
        for i in self.a:
            i = i.lower()
            i = self.pattern.findall(i)
            for v in i:
                if v != '':
                    self.x.append(v)

    def check_words(self):
        for i in self.x:
            if i in self.first_list:
                self.second_list[self.first_list.index(i)] += 1
            else:
                self.first_list.append(i)
                self.second_list.append(1)

    def console_output(self):
        for i in self.endDict:
            print('{}: {}'.format(i, self.endDict.get(i)))

    def file_output(self):
        z = ''
        for i in self.endDict:
            z = '{}\n{}: {}'.format(z, i, self.endDict.get(i))
        codecs.open('output.txt', 'w', 'utf-8').write(str(z))

    def gui_otput(self):
        z = ''
        for i in self.endDict:
            z = '{}\n{}: {}'.format(z, i, self.endDict.get(i))
        return z

    def create_dict(self):
        self.endDict = dict(zip(self.first_list, self.second_list))
        self.dict_enumerator(self.endDict)
        self.endDict = {k: v for k, v in sorted(self.endDict.items(), key=lambda item: item[1], reverse=True)}
        self.mem_clean()