
import random 

def criarlista():
    res=[]
    n=int(input("Dimensão da lista:"))
    for elem in range(n):
        elem=random.randint(1,101)
        res.append(elem)
    return res 

def ler_lista():
    res=[]
    n=int(input("Dimensão da lista:"))
    for elem in range(n):
        elem=int(input("Introduza os valores para colocar na sua lista:"))
        res.append(elem)    
    return res 

def soma_elem(res):
    s=res[0]# A soma começa no primeiro elemento da lista 
    for elem in res[1:]:
        s=s+elem # À soma é acrescentado os elementos seguintes 
    return s

def media_elem(res):
    med=soma_elem(res)/len(res)
    return med

def maior_elem(res):
    maior=res[0]
    for elem in res:
        if maior<=elem:#verifica que se o elemento em teste for maior que o guardado anteriormente então esse irá ser armazenado 
            maior=elem
    return maior

def menor_elem(res):
    menor=res[0]
    for elem in res:
        if menor>=elem:
            menor=elem
    return menor 

def ordenada_Crescente(res):
    for i in range(len(res)-1):# i representa cada posição (0,1,2,...)
        cond="Sim"
        if res[i]>=res[i+1]:#verifica que se o seguinte na lista for menor que o anterior então não está por ordem crescente
            cond="Não"
        else:
            cond="Sim"
    return cond

def ordenada_Decrescente(res):
    for i in range(len(res)-1):
        cond="Sim"
        if res[i]<=res[i+1]:
            cond="Não"
        else:
            cond="Sim"
    return cond

def procura_elem(res):
    x=int(input("Qual valor está à procura?:"))
    for i in range(len(res)):
        if x==res[i]:# verifica se o número que procura está na lista e em que posição
            print(f"Encontrei {x} na posição {i+1}")
    return -1

def menu():
    res=[]
    sair=False
    while sair==False:
        print("Bem-vindo à app de listas aqui tem o menu de funcionalidades!")
        print("(1) Criar Lista") 
        print("(2) Ler Lista") 
        print("(3) Soma") 
        print("(4) Média") 
        print("(5) Maior") 
        print("(6) Menor") 
        print("(7) Está ordenada por ordem crescente?") 
        print("(8) Está ordenada por ordem decrescente?") 
        print("(9) Procura um elemento") 
        print("(0) Sair") 

        y=int(input("O que deseja fazer?:"))
        if y==1:
            res = criarlista()
            print(res)
        elif y==2:
            res = ler_lista()
            print(res)
        elif y==3 and res:
            print(soma_elem(res))
        elif y==4 and res:
            print(media_elem(res))
        elif y==5 and res:
            print(maior_elem(res))
        elif y==6 and res:
            print(menor_elem(res))
        elif y==7 and res:
            print(ordenada_Crescente(res))
        elif y==8 and res:
            print(ordenada_Decrescente(res))
        elif y==9 and res:
            print(procura_elem(res))
        elif y==0:
            sair=True
            print(res)
            print("Então até à próxima!")
        else:
            print("Opção inválida ou lista ainda não criada.")  

menu()                
        
