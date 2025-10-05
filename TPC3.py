
import random 

def criarlista():
    res=[]
    n=int(input("Dimensão da lista:"))
    for elem in range(n):
        elem=random.randint(1,100)
        res.append(elem)
    print(res)
    return res 

def ler_lista():
    res=[]
    n=int(input("Dimensão da lista:"))
    for elem in range(n):
        elem=int(input("Introduza os valores para colocar na sua lista:"))
        res.append(elem)    
    print(res)
    return res 

def soma_elem(res):
    s=res[0]# A soma começa no primeiro elemento da lista 
    for elem in res[1:]:
        s=s+elem # À soma é acrescentado os elementos seguintes 
    print (s)
    return s

def media_elem(res):
    med=soma_elem(res)/len(res)
    return med

def maior_elem(res):
    maior=0
    for elem in res:
        if maior<=elem:#verifica que se o elemento em teste for maior que o guardado anteriormente então esse irá ser armazenado 
            maior=elem
    print(maior) 
    return maior

def menor_elem(res):
    menor=0
    for elem in res:
        if menor>=elem:
            menor=elem
    print(menor)
    return menor 

def ordenada_Crescente(res):
    for i in range(len(res)-1):# i representa cada posição (0,1,2,...)
        if res[i]>=res[i+1]:#verifica que se o seguinte na lista for menor que o anterior então não está por ordem crescente
            print("Não")
            return "Não"
    print("Sim")
    return "Sim"

def ordenada_Decrescente(res):
    for i in range(len(res)-1):
        if res[i]<=res[i+1]:
            print("Não")
            return "Não"
    print("Sim")
    return "Sim"

def procura_elem(res):
    x=int(input("Qual valor está à procura?:"))
    for i in range(len(res)):
        if x==res[i]:# verifica se o número que procura está na lista e em que posição
            print(f"Encontrei {x} na posição {i+1}")
    return -1

while True:
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
    elif y==2:
        res = ler_lista()
    elif y==3 and res:
        soma_elem(res)
        break
    elif y==4 and res:
        media_elem(res)
        break
    elif y==5 and res:
        maior_elem(res)
        break
    elif y==6 and res:
        menor_elem(res)
        break
    elif y==7 and res:
        ordenada_Crescente(res)
        break
    elif y==8 and res:
        ordenada_Decrescente(res)
        break
    elif y==9 and res:
        procura_elem(res)
        break
    elif y==0 and res:
        print(res)
        print("Então até à próxima!")
        break
    else:
        print("Opção inválida ou lista ainda não criada.")
        break
