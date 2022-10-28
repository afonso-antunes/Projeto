
import random

creditos = float(input("Quantos créditos quer depositar? \n Créditos: "))
simbolos = ["&", "$", "Y", "%", "€", "£", "§"]
probabilidade = [50/156, 40,156, 30/156, 20/156, 10/156, 5/156, 1/156]
creditos_apostados = float(input("Quantos creditos deseja apostar? \n Aposta: "))

class SlotMachine:
    def __init__(self, creditos, creditos_apostados):
        self.creditos = creditos
        self.creditos_apostados = creditos_apostados

    def gira_e_roda(self):
        self.slot1, self.slot2, self.slot3 = random.choices(simbolos, probabilidade), random.choices(simbolos, probabilidade), random.choices(simbolos, probabilidade), 
        return self.slot1, self.slot2, self.slot3


    def auxiliar(self, num):
        self.creditos = self.creditos - self.creditos_apostados + num * self.creditos_apostados
        return self.creditos

    def ganhos(self):                                                   #5, 10, 20, 70, 200, 1000, 100000
        if self.slot1 == self.slot2 == self.slot3 == "&":                        
            return self.auxiliar(self, 5)
        elif self.slot1 == self.slot2 == self.slot3 == "$":
            return self.auxiliar(self, 10)
        elif self.slot1 == self.slot2 == self.slot3 == "Y":
            return self.auxiliar(self, 20)
        elif self.slot1 == self.slot2 == self.slot3 == "%":
            return self.auxiliar(self, 70)
        elif self.slot1 == self.slot2 == self.slot3 == "€":
            return self.auxiliar(self, 200)
        elif self.slot1 == self.slot2 == self.slot3 == "£":
            return self.auxiliar(self, 1000)            
        elif self.slot1 == self.slot2 == self.slot3 == "§":
            return self.auxiliar(self, 100000)
           

    def questoes(self):
        while self.creditos > 0:
            self.continuar = input("Deseja continuar a jogar? ")
            if self.continuar == "sim" or self.continuar == "Sim": self.creditos_apostados = float(input("Quantos créditos deseja apostar desta vez? \n Créditos: "))
            else: 
                print("Ganhou", self.creditos, "creditos! Parabéns")
                exit()
        
        if self.creditos <= 0:
            print("Infelizmente já não tem créditos suficientes para continuar o jogo...\nOs seus créditos:", self.creditos)
            exit()
    
    
    def GameIsOn(self):
        while self.creditos > 0:
            res = self.questoes()
            print(self.gira_e_roda())
            print("Ficou com", self.ganhos(), "créditos")


# GameIsOn()