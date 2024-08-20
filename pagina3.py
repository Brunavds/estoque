# Salvar os registros de vendas para futuros balanços. 

## Ainda falta correções no código!

import MySQLdb
from datetime import datetime

def create_connection():
    try:
        connection = MySQLdb.connect(
            host = 'localhost',
            database = 'estoque1',
            user = 'root',
            password = ''
        )
        print("Base conectada!")
    except MySQLdb.Error as e:
        print("Erro ao conectar com o banco: {e}")
        connection = None
    return connection

def insert_vendas(connection, vendas):
    insert_query = ''' 
    INSERT INTO vendas (produto_id, data_venda, qtd_venda, vlr_unitario, total_venda)
    VALUES (%s, %s, %s, %s, %s) 
    '''

    cursor = connection.cursor()
    try:
        cursor.execute(insert_query, vendas)
        connection.commit()
        print("Vendas registradas!")
    except MySQLdb.Error as e:
        print(f"Erro ao inserir dados!: {e}")
    finally:
        cursor.close()


class Saida:
    def __init__(self,connection):
        self.connection = connection

    def adicionar_vendas(self, vendas):
        insert_vendas(self.connection, vendas)


class Vendas:
    def __init__(self, produto_id, data_venda, qtd_venda, vlr_unitario, total_venda):
        self.codigo = produto_id
        self.data_venda = data_venda
        self.qtd_venda = qtd_venda
        self.valor_unitario = vlr_unitario
        self.valor_total = total_venda



def registro_vendas():
    print("******* Registro de vendas ******** ")
    codigo = int(input("Código do produto: "))
    data_venda = datetime.now()
    qtd_venda = int(input("Quantidade de intem: "))
    valor_unitario = float(input("Valor unidade: R$ "))
    valor_total = qtd_venda * valor_unitario

    return(codigo, data_venda, qtd_venda, valor_unitario, valor_total)

def main():
    connection = create_connection()

    if connection:
        vendas = registro_vendas()

        insert_vendas(connection, vendas)

        connection.close()

if __name__ =="__main__":
    main()
