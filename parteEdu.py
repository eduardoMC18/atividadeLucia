import random
import string

pedido = {
        'id_pedido': 0,
        'nome_cliente': 0,
        'endereco': 0,
        'prioridade': 0,
        'descricao_pedido': 0,
        'status_pedido': 'Pendente',
        'id_entregador': 0
    }
entregador = {
    'id_entregador': 0,
    'nome': 0,
    'veiculo': 0,
    'id_pedido': [],
    'disponibilidade': 0
}
pedidos = []
entregadores = []

def cadastrar_pedido():
    novo_pedido = pedido
    for key in novo_pedido:
        if key == 'id_pedido':
            novo_pedido['id_pedido'] = criar_id()
        else: 
            dado = input(f"Insira o dado do(a) {key}\n")
            novo_pedido[key] = dado
    pedidos.append(novo_pedido)
    print(novo_pedido)

def cadastrar_entregador():
    novo_entregador = entregador
    for key in novo_entregador:
        if key == 'id_pedido':
            novo_entregador['id_pedido'] = criar_id()
        else: 
            dado = input(f"Insira o dado do(a) {key}\n")
            novo_entregador[key] = dado
    entregadores.append(novo_entregador)
    print(novo_entregador)

def atualizar_pedido():
    pedido = buscar_pedidos()
    a = int(input("oque voce deseja alterar?"))
    if a == 1:
        novo_status = input("Digite o status: ")
        pedido['status_pedido'] = novo_status
        print(pedido)
    else:
        if a == 2:
            pedido['status_pedido'] = 'Cancelado'
            print(pedido)
        else:
            if a == 3:
                id_entregador = int(input('Digite o id do entregador: '))
                pedido['id_entregador'] = id_entregador
                print(pedido)
            else: 
                if a == 4:
                    pedido['id_entregador'] = None
                    print(pedido)


def buscar_pedidos():
    repeat = 0
    print("Digite o ID do pedido:\n")
    for i in pedidos:
        busca = int(input(''))
        if i['id_pedido'] == busca:
            return i
        
def consultas():
    a = 0
    while a != 4:
        a = int(input(''))
        match a:
            case 1:
                for i in pedidos:
                    if i['status_pedido'] == 'Pendente':
                        print(i)
            case 2:
                for i in pedidos:
                    if i['status_pedido'] == 'Entregue':
                        print(i)
            case 3:
                buscar_pedidos()
            case 4:
                for i in entregadores:
                    if i['disponibilidade'] == 'Disponivel':
                        print(i)
            # case 5:
            #     for i in entregadores:
            #         for w in i['id_pedido']:



def criar_id():
    letra = random.choice(string.ascii_letters)
    numeros = random.randint(0, 9999)
    id = letra + str(numeros)
    return id

a = 0
while a != 4:
    print("""
          --------------
          MENU PRINCIPAL
          --------------""")
    a = int(input('1-Cadastrar pedidos\n2-Consultas\n3-Atualizar pedidos\n'))
    match a:
        case 1:
            cadastrar_pedido()
        case 2:
            buscar_pedidos()
        case 3:
            atualizar_pedido()

