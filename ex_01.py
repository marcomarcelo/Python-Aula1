nome_produto: str = "Mesa de Escritório"
quantidade_estoque: int = 10
preco_unitario: float = 450.0
disponivel_venda: bool = True
data_validade = 2024-12-31

# Imprime uma mensagem simples
print("ola mundo!")
print(nome_produto)
print(f"meu produto é o: {nome_produto}")

# Função input
# Pede ao usuário para digitar seu nome e armazena o resultado na variável nome_usuario
#nome_utilizador = input("Digite seu nome: ")
#print("Olá,", nome_utilizador + "!")

#Função type
print(type(nome_produto))   # <class 'str'>
print(type(quantidade_estoque))  # <class 'int'>
print(type(preco_unitario))  # <class 'int'>
print(type(disponivel_venda))  # <class 'bool'>
print(type(data_validade))  # <class 'int'> ??
print(data_validade)        # 1981

# Métodos
nome_produto_maiusculo = nome_produto.upper()
print(nome_produto_maiusculo)  # Output: MESA DE ESCRITÓRIO

