dicionario = {
    'O principe': True ,
    'Turma da Monica': True ,
    'Admiravel Mundo Novo': True ,
    'Biografia de Steve Jobs': True
} 

# Exibir os livros 
def exibir_livros(): 
    print("LIVROS DISPONIVEIS") 
    for i , ( livro , disponivel) in enumerate(dicionario.items() , start= 1 ): 
        if disponivel:
            status = 'disponivel'
        else:
            status = 'indisponivel' 
            
        print(f"{i} - {livro} ({status})") 
        
def empresta(livro_emprestado):
    if livro_emprestado in dicionario:
        if dicionario[livro_emprestado]:  # Corrigido para acessar o livro corretamente
            dicionario[livro_emprestado] = False  # Marca como indisponível
            print(f"Você emprestou o livro '{livro_emprestado}'")
        else:
            print(f"O livro '{livro_emprestado}' já está indisponível.")
    else:
        print(f"Esse livro não está disponível: '{livro_emprestado}'") 
        
while True:
    exibir_livros() 
    escolha = int(input("Escolha um número (1-4) :")) 
    livro_emprestado = list(dicionario.keys())[escolha] # LISTE -> DICIONARIO.KEYS()[ESCOLHA]
    empresta(livro_emprestado) 
    
    opcao = input("Deseja continuar [S/N]: ") 
    if opcao == 'S' or opcao == 's':
        exibir_livros() 
        escolha = int(input("Escolha um número: ")) 
    elif opcao == 'N' or opcao == 'n': 
        print("SAIR DO SISTEMA") 
        break

#EXPLICANDO O CÓDIGO 
 # for i , ( livro , disponivel) in enumerate(dicionario.items() , start= 1 ): 
        # status = 'disponivel' if disponivel else 'indisponivel'  
        # print(f"{i} - {livro} ({status})")   
        
# livro = chave 
# disponvel = valor 
# enumerate = ENUMERAR ITENS (LISTAGEM - 1 , 2, 3 ,4 )  - COMEÇA (START = 1) 
# status = PODE DECLARAR VARIAVEL ATRAVES DE CHAVES  

#  livro_emprestado = list(dicionario.keys())[escolha] # 

# list() = traforma ou converte as chave em listas 
# keys() = metodo que mostra as chaves do dicionario 
# value() = metodo que mostra os valores do dicionario
              