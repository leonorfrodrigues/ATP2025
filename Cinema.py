
def existeSala(cinema,filme):
  cond=False
  for sala in cinema:
    if filme==sala[2]:
      cond=True
  return cond

def listar(cinema):
  if cinema==[]:
      print("Não há filmes em exibição")
  else:
    for sala in cinema:
        print(f"Na sala está a ser exibido o filme {sala[2]}")
    
  
def disponivel(cinema,filme,lugar):
  cond=True
  for sala in cinema:
    if filme==sala[2]:
      if lugar in sala[1] and 1<=lugar<=sala[0]:
        cond=False
  return cond

def vendebilhete(cinema,filme,lugar):
  for sala in cinema:
    encontrado=False
    while encontrado==True:
      if filme==sala[2]:
        encontrado=True
        if 1<=lugar<=sala[0]:
          if lugar not in sala[1]:
            sala[1].append(lugar)
            print(f"Bilhete vendido para o filme {filme} no lugar {lugar}")
          else:
            print("O lugar está indisponível")
        else:
          print("Lugar Inválido")
          encontrado=False    
    if encontrado==False:
      print("O filme não está em exibição")
  return cinema

def listardisponibilidades(cinema):
  for sala in cinema:
    disp=sala[0]-len(sala[1])
    if disp==0:
      print(f"A sala {sala} não tem lugares disponíveis")
    else:
      print(f"A sala tem {disp} lugares disponíveis")

def inserirSala(cinema,sala):
  if not existeSala(cinema,sala[2]):
    cinema.append(sala)
  else:
    print("Essa sala já existe")
  return cinema

def desmarcar(cinema,filme,lugar):
  for sala in cinema:
      if filme==sala[2]:
        if lugar in sala[1]:
          sala[1].remove(lugar)
  return cinema

def removeSala(cinema,sala):
  for sala in cinema:
    if sala[1]==[] or len(sala[1])==sala[0]:
      cinema.remove(sala)
  return cinema

def menu():
  print(""" 
    (1) Reset
    (2) Filmes em exibição 
    (3) Adicionar Sala
    (4) Comprar bilhete
    (5) Desmarcar 
    (6) Lista de disponibilidades
    (7) O lugar está disponível?
    (8) Remover Sala
    (0) Sair
    """)
  
  
  sair=False
  cinema=[]
  while sair==False:
    opcao=int(input("Introduza a opção:"))
    if opcao==1:
      cinema=[]
    elif opcao==2:
      listar(cinema)
    elif opcao==3:
      vendidos=[]
      filme=input("Introduza o filme:")
      nlugares=int(input("Introduza a capacidade da sala:"))
      sala=[nlugares,vendidos,filme]
      cinema=inserirSala(cinema,sala)
    elif opcao==4:
      filme=input("Introduza o filme:")
      lugar=int(input("Introduza um lugar:"))
      cinema=vendebilhete(cinema,filme,lugar)
    elif opcao==5:
      filme=input("Introduza o filme:")
      lugar=int(input("Introduza um lugar:"))
      cinema=desmarcar(cinema,filme,lugar)
    elif opcao==6:
      listardisponibilidades(cinema)
    elif opcao==7:
      filme=input("Introduza o filme:")
      lugar=int(input("Introduza o lugar:"))
      print(disponivel(cinema,filme,lugar))
    elif opcao==8:
      sala=input("Introduza a sala que pretende remover:")
      cinema=removeSala(cinema,sala)
    elif opcao==0:
      sair=True
      print("May the force be with you, até à próxima!")
    else:
      print("Opção inválida, tente novamente")

