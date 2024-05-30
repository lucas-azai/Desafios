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
def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return conta


# Função para saque
def sacar(conta, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    elif excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1

    return conta


# Função para exibir o extrato
def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    if conta["extrato"]:
        print(conta["extrato"])
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
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

    usuarios[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "contas": []}
    print("Usuário cadastrado com sucesso!")

    return usuarios


# Função para cadastrar conta bancária
def cadastrar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
        print("Usuário não encontrado!")
        return contas

    numero_conta = len(contas) + 1
    conta = {"numero": numero_conta, "saldo": 0, "extrato": "", "numero_saques": 0}
    contas[numero_conta] = conta
    usuarios[cpf]["contas"].append(conta)
    print(f"Conta {numero_conta} cadastrada com sucesso para o usuário {usuarios[cpf]['nome']}!")

    return contas


# Função para selecionar uma conta
def selecionar_conta(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    if cpf not in usuarios:
        print("Usuário não encontrado!")
        return None, None

    print("Contas do usuário:")
    for conta in usuarios[cpf]["contas"]:
        print(f"Conta {conta['numero']}: Saldo R$ {conta['saldo']:.2f}")

    numero_conta = int(input("Informe o número da conta: "))
    for conta in usuarios[cpf]["contas"]:
        if conta["numero"] == numero_conta:
            return cpf, conta

    print("Conta não encontrada!")
    return None, None


# Variáveis globais
usuarios = {}
contas = {}

limite = 1500
LIMITE_SAQUES = 10

# Loop principal
while True:
    opcao = exibir_menu()

    if opcao == "d":
        cpf, conta = selecionar_conta(usuarios)
        if conta:
            conta = depositar(conta)

    elif opcao == "s":
        cpf, conta = selecionar_conta(usuarios)
        if conta:
            conta = sacar(conta, limite, LIMITE_SAQUES)

    elif opcao == "e":
        cpf, conta = selecionar_conta(usuarios)
        if conta:
            exibir_extrato(conta)

    elif opcao == "c":
        usuarios = cadastrar_usuario(usuarios)

    elif opcao == "a":
        contas = cadastrar_conta(contas, usuarios)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
