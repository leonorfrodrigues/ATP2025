#Jogo com o computador a jogar 1º
from random import randint



def game1():
    print("O computador joga primeiro")
    total=21
    while total>1:
        if total>4:
            com=randint(1,4)
        else: 
            com=randint(1,total-1)
        print(f"O computador retirou {com}")
        total=total-com 
        print(f"Restam {total}")
        
        if total==1:
            print("Perdeste!, ficaste com o último fósforo")
            break
#Jogador
        while True:
            res= int(input("Quantos fósforos queres retirar?:"))
            if 1<=res<=4 and res<=total-1:
                break
            print("Perdeste!, ficaste com o último fósforo")
            
         
        print(f"Retiraste {res}")
        total=total-res
        print(f"Restam {total}")

        if total==1:
            print("Ganhaste!, o computador ficou com o último fósforo")
            y=input("Gostarias de jogar de novo?: ")
            if y.lower()=="s":
                z=input("Gostarias de experimentar jogar em segundo?:")
                if z.lower()=="s":
                    game1()
                else:
                    game2()
            else:
                print("That's all folks!")
        
#Jogo com o computador em 2º
def game2():
    print("És o primeiro a jogar")
    total = 21
    while total>1:
        while True:
            res = int(input("Quantos fósforos queres retirar?: "))
            if 1 <= res <= 4 and res <= total - 1:
                break
            print("Inválido, introduza um valor entre 1 e 4")
            
        print(f"Retiraste {res}")
        total= total- res
        print(f"Restam {total}")

        if total == 1:
            print("Ganhaste! O computador ficou com o último fósforo.")
            return

        # computador joga de forma "inteligente"
        com = (total - 1) % 5
        if com == 0:  
            com = 1
        print(f"O computador retirou {com}")
        total =total- com
        print(f"Restam {total}")

        if total == 1:
            print("Perdeste! Ficaste com o último fósforo.")
            y=input("Gostarias de jogar de novo?: ")
            if y.lower()=="s":
                z=input("Gostarias de experimentar jogar em segundo?:")
                if z.lower()=="s":
                    game1()
                else:
                    game2()
            else:
                print("That's all folks!")
                




#Introdução
input("Bem vindo ao jogo dos fósforos inicialmente começa com 21 fósforos e vão sendo retirados 1,2,3 ou 4 fósforos vence aquele que não retirar o último fósforo")
x=input("Gostaria de ser o primeiro a jogar, responde s ou n: ")
if x=="s" or x=="S":
    game2()

else:
    game1()



