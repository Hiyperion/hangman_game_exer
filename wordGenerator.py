'''
Created on domingo, 3 de abril de 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Descripcion:
    Generates a random word from the Data file

    '''
import random
class Generator():
    def __init__(self,fileName) -> None:
        self.filename = fileName
    def generate_word(self):
        words = []
        with open(self.filename,'r',encoding = 'UTF-8') as f:
            for word in f:
                words.append(word)
        ran_index = random.randint(0,len(words))
        rand_word =words[ran_index].strip()
        rand_word = rand_word.upper()
        return self.replace_tildes(rand_word)

    def replace_tildes(self,word):
        vocals = ['A', 'E', 'I', 'O', 'U']
        vocals_tild = ['Á', 'É', 'Í', 'Ó', 'Ú']
        for i in range(5):
            if vocals_tild[i] in word:
                word = word.replace(vocals_tild[i],vocals[i])
        return word