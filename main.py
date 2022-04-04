'''
Created on domingo, 3 de abril de 2022
@author: Fabricio Cordova

https://github.com/Hiyperion

Descripcion:
    Main program for run Hangman game

'''
from wordGenerator import Generator
import os
TITULO = """
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                    BY HIYPERION
"""
class MainProgram():
    def __init__(self) -> None:
        self.cont=0
        self.run()
    
    # @staticmethod
    def run(self):
        # print(TITULO)
        generator = Generator("data.txt")
        palabra = generator.generate_word()
        cont_err = 0
        
        self.solution = [el for el in '_'*len(palabra)]
        solve = False
        entradas = []
        while not solve:
            os.system("clear")
            print(TITULO)
            perdido = self.draw_hagman(cont_err)
            if perdido:
                print("PARTIDA PERDIDA, the word was: "+palabra)
                break
            # print(palabra)
            print(''.join([el+' ' for el in self.solution]))
            user_letter = input("Ingrese una letra: ")
            user_letter=user_letter.upper()
            if user_letter == palabra:
                print("Correct, the word was: "+ palabra)
                break
            if user_letter in palabra and user_letter not in entradas:
                self.replace_user_letter(palabra,user_letter)
            elif user_letter not in palabra:
                cont_err+=1
            entradas.append(user_letter)
            if self.cont ==len(palabra):
                print("Correct, the word was: "+ palabra)
                solve= True
            
    def replace_user_letter(self,palabra,user_letter):
        word_list = [let for let in palabra.strip('\n')]
        times_letter = word_list.count(user_letter)
        for i in range(times_letter):
            index = word_list.index(user_letter)
            word_list[index]='_'
            self.solution[index]=user_letter
            self.cont+=1
    def draw_hagman(self,cont_err):
        inicio ="""
**********************

         _______
        |       |
        |       |
        |
        |
        |
        |
    ____|__________

**********************
    """
        first_error ="""
**********************

         _______
        |       |
        |       |
        |       O
        |
        |
        |
    ____|__________

**********************
    """
        second_error ="""
**********************

         _______
        |       |
        |       |
        |       O
        |      /|
        |
        |
    ____|__________

**********************
    """
        third_error ="""
**********************

         _______
        |       |
        |       |
        |       O
        |      /|\\
        |
        |
    ____|__________

**********************
    """
        fourth_error ="""
**********************

         _______
        |       |
        |       |
        |       O
        |      /|\\
        |      /
        |
    ____|__________

**********************
    """
        fin ="""
**********************

         _______
        |       |
        |       |
        |       O
        |      /|\\
        |      / \\
        |
    ____|__________

**********************
    """
        errors = [inicio,first_error, second_error,third_error,fourth_error,fin]
        if cont_err <5:
            print(errors[cont_err])
        else:
            print(errors[cont_err])
            return True
if __name__ == "__main__":
    MainProgram()
