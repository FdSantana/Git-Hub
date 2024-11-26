import json
import os
import getpass

user = getpass.getuser()
path_dict = f"C:\\Users\\{user}\\OneDrive\\Files - Programming\\Estudos\\Python\\RocketSeat\\Introdução ao Python\\Aprendendo na pratica\\projeto\\"
cmd_limpeza = lambda: os.system("cls")


def atualizar_registros(tarefas: list, id_tarefa: dict):

    """
    salva as tarefas para não perder o histórico
    salva o último id gerado p evitar erros
    """

    global cmd_limpeza

    print("salvando histórico de tarefas...")
    with open(path_dict + "\\data\\tarefas_v2.json", "w") as fp:
        json.dump(tarefas, fp)
        fp.close()

    with open(path_dict + "\\data\\ultimo_id.json", "w") as fp:
        json.dump(id_tarefa, fp)
        fp.close()

    print("histórico salvo...")
    cmd_limpeza()


def adicionar_tarefa(
    tarefas: list = "recebe a lista de todas as tarefas",
    id_tarefa: dict = "recebe o último registro de id",
):

    """
    nome_nova_tarefa: Recebemos o nome da nova tarefa a ser criada
    id_nova_tarefa, id_tarefa['id']: pega o ultimo_id_tarefa gerado e soma + 1
    loga após ele salva o histórico com a tarefa nova gerada
    """

    nome_nova_tarefa = input("Informe o nome da nova tarefa: ")
    id_nova_tarefa = id_tarefa["id"] = id_tarefa["id"] + 1

    tarefas.append(
        {"id": id_nova_tarefa, "tarefa": nome_nova_tarefa, "status": "em aberto"}
    )

    atualizar_registros(tarefas, id_tarefa)

    return print(f"tarefa registrada no id: {id_nova_tarefa}")


def atualizar_tarefas(tarefas: list):

    """
    Recebe o id da tarefa procurada
    """
    id_tarefa_procurada = int(input("informe o id da tarefa que será atualizada: "))
    novo_nome = str(input("informe o novo nome da tarefa: "))

    for i, item in enumerate(tarefas):
        if item["id"] == id_tarefa_procurada:
            tarefa_localizada = True
            break

    try:
        if tarefa_localizada:
            tarefas[i]["tarefa"] = novo_nome

            with open(path_dict + "\\data\\tarefas_v2.json", "w") as fp:
                json.dump(tarefas, fp)
                fp.close()

            return print(f"tarefa id {id_tarefa_procurada} atualizada!")
    except Exception as e:
        if "is not defined" in e:
            return print("o id_tarefa informado está inválido")


def completar_tarefa(tarefas: list):
    """
    localizamos o id da tarefa
    solicitamos o status atual da tarefa e atualizamos o status
    """

    id_tarefa_procurada = int(input("informe o id da tarefa que será atualizada: "))

    for i, item in enumerate(tarefas):
        if item["id"] == id_tarefa_procurada:
            tarefa_localizada = True
            break

    try:
        if tarefa_localizada:

            status = {
                0: "em aberto",
                1: "em tratativa",
                2: "finalizado",
                3: "travado (dependencias externas)",
            }

            while True:

                print(f"temos os seguintes status disponíveis:")
                print(f"{json.dumps(status)}")
                print(
                    "lembre-se, coloque apenas o número na frente (sem aspas) do respectivo status"
                )

                try:
                    id_status = int(input("informe o id do status: "))
                    break
                except Exception as e:
                    print(
                        "ops, parece que você digitou um id de status inválido, vamos tentar de novo..."
                    )
                    print("lembre-se, digite apenas o número do status (sem aspas)")

            tarefas[i]["status"] = status[id_status]

            with open(path_dict + "\\data\\tarefas_v2.json", "w") as fp:
                json.dump(tarefas, fp)
                fp.close()

            return print(f"tarefa id {id_tarefa_procurada} teve seu status atualizado!")
    except:
        return print("o id_tarefa informado está inválido")


def deletar_tarefa(tarefas: list):
    """
    Vamos remover todas as tarefas que estão com o status de finalizado
    """

    lista_tarefas_finalizadas = []

    for i, item in enumerate(tarefas):
        if item["status"] == "finalizado":
            lista_tarefas_finalizadas.append(i)

    lista_tarefas_finalizadas.sort(reverse=True)

    try:
        with open(path_dict + "\\data\\tarefas_removidas.json", "r") as fp:
            tarefas_removidas = json.load(fp)
            fp.close()
    except Exception as e:
        if "Expecting value: line 1 column 1" in str(e):
            tarefas_removidas = list([])

    for i in lista_tarefas_finalizadas:
        tarefas_removidas.append(tarefas[i])
        del tarefas[i]

        with open(path_dict + "\\data\\tarefas_v2.json", "w") as fp:
            json.dump(tarefas, fp)
            fp.close()

        with open(path_dict + "\\data\\tarefas_removidas.json", "w") as fp:
            json.dump(tarefas, fp)
            fp.close()

    return print("tarefas finalizadas foram excluídas")


def mostrar_tarefas(tarefas: list):
    return print(json.dumps(tarefas, indent=2))
