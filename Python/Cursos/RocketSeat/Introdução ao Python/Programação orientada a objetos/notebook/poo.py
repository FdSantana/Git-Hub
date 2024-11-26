import json
import os
import sqlite3
import datetime

with open('../temp/variaveis.json', 'r', encoding='utf-8') as f:
    jsonFile = json.load(f)
    f.close()


class Pessoa:
    def __init__(
        self,
        nome: str,
        idade: int,
        altura: float,
        peso: float,
        telefone: str,
        email: str,
        cep: str,
    ) -> None:

        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.telefone = telefone
        self.email = email
        self.cep = cep


    def carga_registro_id(self):
        with open("../temp/id_registro.json", "r") as fp:
            id_db = json.load(fp)
            self.id_db = id_db['id']
            fp.close()


    def escrita_registro_id(self):
        jsonId = {"id": (self.id_db + 1)}
        with open("../temp/id_registro.json", "w") as fp:
            json.dump(jsonId, fp)
            fp.close()


    def conexao_db(self):
        try:
            self.conexao()
        except:
            self.conexao = sqlite3.connect('../db/dbo.pessoas.db')
            self.cnxn = self.conexao.cursor()


    def valida_tabela_existente_db(self):

        try:
            self.cnxn.execute('SELECT * FROM pessoas')

        except Exception as e:
            if 'no such table: pessoas' in str(e):

                query = """
                CREATE TABLE pessoas (id VARCHAR PRIMARY KEY, nome VARCHAR, idade INT, altura FLOAT, peso FLOAT, telefone VARCHAR, email VARCHAR, cep VARCHAR) 
                        """

                self.cnxn.execute(query)
                self.conexao.commit()
            else:
                data_execucao = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
                with open(f"../logs/log_erro_{data_execucao.replace(':', '')}.txt", 'a') as f:
                    f.write(f'erro no db: {str(e)} - data: {data_execucao} \n')


    def registro_db(self):
        print(f'registrando {self.nome}, id: {self.id_db} no banco')
        query = f"""
        INSERT INTO pessoas VALUES('{self.id_db}', '{self.nome}', {self.idade}, {self.altura}, {self.peso}, '{self.telefone}', '{self.email}', '{self.cep}')
        """
        self.escrita_registro_id()
        self.cnxn.execute(query)
        self.conexao.commit()


    def execucao(self):
        self.carga_registro_id()
        self.conexao_db()
        self.valida_tabela_existente_db()
        self.registro_db()


if __name__ == "__main__":

    for item in jsonFile["pessoas"]:
        try:
            registro_db = Pessoa(
                item["nome"],
                item["idade"],
                item["altura"],
                item["peso"],
                item["telefone"],
                item["email"],
                item["cep"],
            )
            registro_db.execucao()
        except Exception as e:
            data_execucao = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            with open(f"../logs/log_geral_{data_execucao.replace(':', '')}.txt", "a") as f:
                f.write(f"erro : {e} - data : {data_execucao} \n")
