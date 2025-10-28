def medias(tabMeteo):
    res = []
    for data,tmin,tmax,prec in tabMeteo:
        med=(tmax-tmin)/2 # res.append((data,f"{dia[2]}-{dia[1]//2})
        res.append((data,med))
    return res

def guardaTabMeteo(t, fnome):
    file=open(fnome,"w")
    for data,tmin,tmax,prec in t:
        ano,mes,dia=data
        file.write(f"{ano}-{mes}-{dia}|{tmin}|{tmax}|{prec}\n")
    file.close()
    return

def carregaTabMeteo(fnome):
    res = []
    file=open(fnome,"r")
    for linha in file:
        linha.strip()
        campos=linha.split("|")
        data,tmin,tmax,prec=campos
        ano,mes,dia=data.split("-")
        res.append(((int(ano),int(mes),int(dia)),float(tmin),float(tmax),float(prec)))
    file.close()
    return res

def minMin(tabMeteo):
    minima=tabMeteo[0][1]
    i=0
    while i<len(tabMeteo):
        if minima>tabMeteo[i][1]:
            minima=tabMeteo[i][1]
        i=i+1
    return minima

def amplTerm(tabMeteo):
    res = []
    for dia in tabMeteo:
        ampl=dia[2]-dia[1]
        res.append((dia[0],ampl))
    return res 

def maxChuva(tabMeteo):
    max_prec=tabMeteo[0][3]
    for dia in tabMeteo:
        if dia[3]>max_prec:
            max_prec=dia[3]
            max_data=dia[0]
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    i=0
    while i< len(tabMeteo):
        if tabMeteo[i][3]>p:
            res.append((tabMeteo[i][0],tabMeteo[i][3]))
        i=i+1
    return res

def maxPeriodoCalor(tabMeteo, p):
    res=0
    seq=0
    i=0
    while i<len(tabMeteo):
        if tabMeteo[i][2]>p:
            seq=seq+1
        if tabMeteo[i][2]<=p:
            if res<seq:
                res=seq
            seq=0
        i=i+1
    if res<seq:
        res=seq
    return res

from matplotlib import pyplot as plit 

def grafTabMeteo(t):
    x = [f"{data[0]}/{data[1]}/{data[2]}" for data,tmin,tmax,prec in t]#t é a tabela meteo
    ymin = [tmin for data,tmin,tma,prec in t]
    ymax = [tmax for data,tmin,tmax,prec in t]
    precs =[prec for *_, prec in t]# escolhe os últimos valores de cada dia 

    plit.plot(x,ymin, label="Temperatura mínima(ºC)", color="blue",marker="o")
    plit.plot(x,ymax, label= "Temperatura Máxima(ºC)", color="red", marker="o")
    plit.legend() #legenda
    plit.grid() #grelha de trás 
    plit.xticks(rotation=45)
    plit.show() #mostrar o gráfico 


    plit.bar(x,precs, label="Precipitação", color="c")#para um gráfico de barras 
    plit.legend() #legenda
    plit.grid()  #grelha de trás 
    plit.xticks(rotation=45) #rotação 
    plit.show() #
    return


def menu():
    print(
    "---------Aplicação de Meteorologia---------\n"
     "(1) Escolha a tabela meteorológica\n"
     "(2) Média de Temperaturas\n"
     "(3) Guardar Tabela Meteorológica\n"
     "(4) Carregar Tabela Meteorológica\n"
     "(5) Temperatura Mínima\n"
     "(6) Amplitude Térmica\n"
     "(7) Máxima precipitação\n"
     "(8) Dias Chuvosos\n"
     "(9) Período Máximo de Calor\n"
     "(10) Gráficos de Temperatura e Pluviosidade\n"
     "(0) Sair ")
    
    
    sair=False
    tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
    tabMeteo2 = [((2022,1,20), 2, 16, 0), ((2022,1,21), 1, 13, 0.2), ((2022,1,23), 6, 19, 0.6), ((2022,1,24), 3, 18, 0.8),((2022,2,20), 6, 19, 0.2), ((2022,2,24), 3, 18, 0.2), ((2022,2,28), 3, 18, 0.2)]
    tabelas = {"tabMeteo1": tabMeteo1,"tabMeteo2": tabMeteo2}
    while sair!=True:
        op=int(input("Escolha a opção:"))
        if op==1:
            encontrado=False
            while encontrado!=True:
                tab=input("Escolha a tabela Meteorológica (tabMeteo1 ou tabMeteo2):")
                if tab in tabelas:
                    tabela=tabelas[tab]
                    encontrado=True
                else:
                    print("Coloque uma lista meteorológica da lista (tabMeteo1 ou tabMeteo2)")
            print(f"A tabela seleciona é {tabela}")
        elif op==2:
            print(f"Temperatura média:{medias(tabela)}")       
        elif op==3:
            fnome=input("Introduza o nome do ficheiro que quer guardar:")
            guardaTabMeteo(tabela,f"{fnome}.txt")
        elif op==4:
            fnome=input("Introduza o nome do ficheiro:")
            tabela=carregaTabMeteo(f"{fnome}.txt")
        elif op==5:
            print(f"Temperatura mínima:{minMin(tabela)}")
        elif op==6:
            print(f"Amplitude Térmica:{amplTerm(tabela)}")
        elif op==7:
            print(f"Máxima precipitação:{maxChuva(tabela)}")
        elif op==8:
            p=int(input("Escolha o limite de precipitação:"))
            print(f"Os dias com mais precipitação:{diasChuvosos(tabela,p)}")
        elif op==9:
            p=int(input("Escolha o limite de calor:"))
            print(f"Período máximo de calor:{maxPeriodoCalor(tabela,p)}")
        elif op==10:
            grafTabMeteo(tabela)
        elif op==0:
            sair=True
            print("Até à próxima!")
        else:
            print("Opção inválida")
        
menu()

    



