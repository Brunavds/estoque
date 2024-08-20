#Apresenta todos os produtos cadastrados no sistema.

import MySQLdb

def create_connection():
    try:
        connection = MySQLdb.connect(
            host = 'localhost',
            database = 'estoque1',
            user ='root',
            password = ''
        )
        print("******** Produtos cadastrados *********")
    except MySQLdb.Error as e:
        print("Erro ao conectar com a base: {e}")
        connection = None
    return connection
    

def select_produto(connection):
    select_query = '''
    SELECT id_entrada, produto_id, nome_produto, ctg_produto, qtd_produto,
    vlr_venda, data_entrada FROM entrada_produtos;
    '''

    try: 
        cursor = connection.cursor()
        cursor.execute(select_query)
        resultados = cursor.fetchall()
        for row in resultados:
            print(row)
        cursor.close()
    except MySQLdb.Error as e:
        print(f"Erro o executar a consulta: {e}")


connection = create_connection()

if connection:
    select_produto(connection)
    connection.close()
    print("Fim da Listagem.")