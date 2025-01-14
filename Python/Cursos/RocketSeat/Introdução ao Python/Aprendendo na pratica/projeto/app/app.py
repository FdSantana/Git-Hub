import json
from modules import (adicionar_tarefa,
                     mostrar_tarefas,
                     atualizar_tarefas,
                     completar_tarefa,
                     deletar_tarefa)
import getpass
user = getpass.getuser()


with open("../data/ultimo_id.json", "r") as fp:
    id_tarefa = json.load(fp)
    fp.close()


try:
    with open("../data/tarefas_v2.json", "r") as fp:
        tarefas = json.load(fp)
        fp.close()
except Exception as e:
    if "Expecting value: line 1 column 1" in str(e):
        tarefas = list([])


acoes_index = {
    1: adicionar_tarefa,
    2: mostrar_tarefas,
    3: atualizar_tarefas,
    4: completar_tarefa,
    5: deletar_tarefa,
}


while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tafera")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    try:
        escolha = int(input("Digite a sua escolha: "))
    except:
        print('hmmm... essa escolha eu não conheço, digite novamente:')
        print("\nMenu do Gerenciador de Lista de tarefas:")
        print("1. Adicionar tafera")
        print("2. Ver tarefas")
        print("3. Atualizar tarefa")
        print("4. Completar tarefa")
        print("5. Deletar tarefas completadas")
        print("6. Sair")

    if escolha == 6:
        break
    elif escolha == 1:
        funcao_exec = acoes_index[escolha]
        funcao_exec(tarefas, id_tarefa)
    else:
        funcao_exec = acoes_index[escolha]
        funcao_exec(tarefas)
