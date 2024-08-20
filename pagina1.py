#Cadastra produtos no sistema.

import MySQLdb

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
        print(f"Erro ao conectar com a base: {e}")
        connection = None
    return connection 

def insert_produto(connection, produto):
    insert_query = '''
    INSERT INTO produto (nome_produto, ctg_produto, desc_produto, qtd_produto, vlr_compra,
    vlr_venda)
    VALUES (%s, %s, %s, %s, %s, %s ); 
    '''

    cursor = connection.cursor()
    try:
        cursor.execute(insert_query, (
            produto.nome,
            produto.categoria,
            produto.descricao,
            produto.qtd,
            produto.valor_compra,
            produto.valor_venda

        ))
        connection.commit()

        pergunta = input("Deseja inserir mais produtos? (Sim|Não):  ").strip().lower()
        if pergunta != 'Sim':
            print("Produto cadastrado com sucesso.")
            return False #Para parar o loop pois o break não pode se usado nessa estrutura
           
  
    except MySQLdb.Error as e:
        print(f"Erro ao cadastrar produto: {e}")
    finally:
        cursor.close()


class Estoque:
    # Contrala a operação de adcionar produtos ao banco
    def __init__(self, connection):
        self.connection = connection

    def adicionar_produto(self, produto):
        insert_produto(self.connection, produto)


class Produto: 
    #Produtos que serão incluidos
    def __init__(self, nome_produto, ctg_produto, desc_produto, qtd_produto, vlr_compra,
    vlr_venda): 
        self.nome = nome_produto
        self.categoria = ctg_produto 
        self.descricao = desc_produto
        self.qtd= qtd_produto
        self. valor_compra= vlr_compra
        self. valor_venda= vlr_venda


def cadastrar_produto(): #Coletar as informações
    print("****** Sistema de cadastro BY *****")
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    descricao = input ("Descrição: ")
    qtd = int(input("Quantidade do produto: "))
    valor_compra = float(input("Valor de compra: "))
    valor_venda = float(input("Valor de venda: "))

    return Produto(nome, categoria, descricao, qtd, valor_compra, valor_venda)

connection = create_connection()

if connection: 
    estoque = Estoque(connection)

    while True: 
        produto = cadastrar_produto()
        continuar = estoque.adicionar_produto(produto)
        if continuar is False:
            break

    
    connection.close()
    print("Produto cadastrado com sucesso!")

