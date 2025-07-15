import csv

arquivo = "arquivocsv"

clientes = []
def cadastrar_clientes():
    nome = input('Nome:\n')
    cpf = input('Cpf:\n')
    email = input('Email:\n')
    telefone = input('Telefone:\n')
    cliente = {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone}
    clientes.append(cliente)



def buscar_clientes_cadastrados():
    cpf = input('Digite o cpf do cliente:')
    for cliente in clientes:
         if cliente['cpf'] == cpf:
            print(f"\nCliente encontrado!\nNome: {cliente['nome']}\nEmail: {cliente['email']}\nTelefone: {cliente['telefone']}\n")
            encontrado = True
            break
    if not encontrado:
        print('Cliente não encontrado.\n')

            
print ('===Menu===')

while True:
    escolha = input('\n 1. cadastrar cliente\n 2. buscar cliente\n 3. sair\nEscolha (1/2/3):\n')
    try:
        if escolha == '3':
            print ('Obrigado pela visita!')
            break
        elif escolha == '1':
            cadastrar_clientes()
            desejo = input('Deseja continuar?(s/n): ')
            if desejo == 's': continue
            elif desejo == 'n': 
                print ('Operação concluída!')
                break
        elif escolha == '2':
            buscar_clientes_cadastrados()
            desejo = input('Deseja continuar?(s/n): ')
            if desejo == 's': continue
            elif desejo == 'n': 
                print ('Operação concluída!')
                break
        else:
            print ('Escolha uma operação existente ou adicione números válidos!')
    except ValueError:
        print ('Entrada inválida tente novamente!')
        