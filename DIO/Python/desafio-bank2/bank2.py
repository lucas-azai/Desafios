# Função para exibir o menu
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar Usuário
    [a] Cadastrar Conta Bancária
    [q] Sair
    => """
    return input(menu).lower()


# Função para depósito
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


# Função para saque
def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato, numero_saques


# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# Função para cadastrar usuário
def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if cpf in usuarios:
        print("Usuário já cadastrado!")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("Usuário cadastrado com sucesso!")

    return usuarios


# Função para cadastrar conta bancária
def cadastrar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
        print("Usuário não encontrado!")
        return contas

    numero_conta = len(contas) + 1
    contas[numero_conta] = {"cpf": cpf, "saldo": 0, "extrato": "", "numero_saques": 0}
    print(f"Conta {numero_conta} cadastrada com sucesso para o usuário {usuarios[cpf]['nome']}!")

    return contas


# Variáveis globais
usuarios = {}
contas = {}

saldo = 0
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

# Loop principal
while True:
    opcao = exibir_menu()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "c":
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == "a":
        contas = cadastrar_conta(contas, usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
