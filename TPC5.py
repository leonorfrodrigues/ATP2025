def criarturma():
    turma=[]
    n=int(input("Qual o tamanho da turma:"))
    while len(turma)<n:#Adiciona alunos até a turma chegar ao valor posto
        cond=True
        notas=[]
        nome=input("Insira o nome do aluno:")
        id_aluno=input("Insira o número do aluno:") 
        while cond:#enquanto for verdade que as notas não estão no intervalo
            notaTPC=float(input("Insira a nota do TPC:"))
            notaProj=float(input("Insira a nota do projeto:"))# para pedir o valor das notas tem de estar dentro do ciclo pois caso uma esteja mal não volta a pedir 
            notaTeste=float(input("Insira a nota do teste:"))
            if 0<=notaTPC<=20 and 0<=notaProj<=20 and 0<=notaTeste<=20:
                cond=False# as notas estão no intervalo pretendido
            else:
                print("Coloque a nota entre 0-20 valores")
        
        notas=[notaTPC,notaProj,notaTeste]
        aluno=(nome,id_aluno,notas)
        turma.append(aluno)
        print(f"O aluno {nome} foi inserido com sucesso")
    return turma

def inserirAluno(turma,aluno_novo):
    existe=False# o aluno a pesquisar não existe 
    while existe:
        for aluno in turma:
            if aluno_novo[1]== aluno[1]:
                existe=True
                print("O aluno que pretende inserir já existe")
    if existe==False:
        turma.append(aluno_novo)
        print(f"O aluno {aluno_novo} foi inserido com sucesso")
    return turma

def listarTurma(turma):
    if turma==[]:
        print("Não há turmas criadas")
    else:
        print(f"{turma}\n")
    return turma 

def consultarId(id_aluno,turma):
    encontrado=False
    for aluno in turma:
        if id_aluno==aluno[1]:
            print(aluno)
            encontrado=True
    if encontrado==False:
        print("O aluno não está na turma")

def guardarTurma(turma,fturma):
    file=open(fturma,"w")
    for aluno in turma:
        nome=aluno[0]
        id_aluno=aluno[1]
        notas=aluno[2]
        file.write(f"{nome};{id_aluno};{str(notas[0])}@{str(notas[1])}@{str(notas[2])}\n")
    file.close()
    return

def carregarTurma(fturma,turma):
    file=open(f"./{fturma}.txt")
    text= file.read()
    alunos_text=text.split("\n")
    for a in alunos_text:
        a=a.strip()
        if a!="":
            partes=a.split(";")
            nome=partes[0]
            id_aluno=partes[1]
            nota_str=partes[2].split("@")
            notas=[]
            for n in nota_str:
                notas.append(float(n))
            aluno=(nome,id_aluno,notas)
            turma.append(aluno)
    file.close()
    print(turma)


def menu():
    turma=[] 
    sair=False
    while sair!=True:
        print("-----------Menu do TurmaGere------------\n" 
    "(1)Criar Turma\n"
    "(2)Inserir aluno na turma\n" 
    "(3)Listar a Turma\n"
    "(4)Consultar aluno por Id\n"
    "(5)Guardar a turma num ficheiro\n" 
    "(6)Carregar turma a partir de ficheiro\n"
    "(0)Sair")
        op=int(input("Introduza a opção:"))
        
        if op==1:        
            turma=criarturma()
        elif op==2:
            nome=input("Insira o nome do aluno:")
            id_aluno=input("Insira o número do aluno:")
            notaTPC=float(input("Insira a nota do TPC:"))
            notaProj=float(input("Insira a nota do projeto:"))
            notaTeste=float(input("Insira a nota do teste:"))
            notas=[notaTPC,notaProj,notaTeste]
            aluno_novo=(nome,id_aluno,notas)
            inserirAluno(turma,aluno_novo)
        elif op==3:
            listarTurma(turma)
        elif op==4:
            id_aluno=input("Insira o número do aluno:")
            consultarId(id_aluno,turma)
        elif op==5:
            fturma=input("Qual o ficheiro que quer guardar?:")
            guardarTurma(turma,f"{fturma}.txt")
        elif op==6:
            fturma=input("Qual o ficheiro que quer carregar?:")
            carregarTurma(fturma,turma)
        elif op==0:
            sair=True
            print("Até à próxima!")
        else:
            print("Opção inválida")

menu()
