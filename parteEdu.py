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
    novo_pedido = pedido.copy()
    for key in novo_pedido:
        if key == 'id_pedido':
            novo_pedido['id_pedido'] = criar_id()
        else: 
            dado = input(f"Insira o dado do(a) {key}\n")
            novo_pedido[key] = dado
    pedidos.append(novo_pedido)
    print(novo_pedido)

def cadastrar_entregador():
    novo_entregador = entregador.copy()
    novo_entregador['id_pedido'] = []
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
    a = int(input("Oque voce deseja alterar?\n\n1-Alterar Status\n2-Cancelar Pedido\n3-Associar Entregador\n4-Remover Associação de Entregador"))
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
        busca = (input('Informe o ID do Pedido: '))
        if i['id_pedido'] == busca:
            return i
        
def consultas():
    a = 0
    while a != 4:
        a = int(input('1-Pendentes\n2-Entregue\n3-Buscar Pedido\n4-Disponivel\n5-Voltar ao Menu\n\nEscolha uma opção: '))
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
            case 5:
                return
            # case 5:
            #     for i in entregadores:
            #         for w in i['id_pedido']:
     menu_principal()

def  relatorios():
    print(f"Total de pedidos cadastrados: {len(pedidos)}")
    
    status_contagem = {'Pendente': 0, 'Em Rota': 0, 'Entregue': 0, 'Cancelado': 0}
    altas = 0
    for i in pedidos:
        status_contagem[i['status_pedido']] += 1
        if i['prioridade'] == 'Alta':
            altas += 1
            
    print("\nQuantidade de pedidos por status:")
    for status, qtd in status_contagem.items():
        print(f"  - {status}: {qtd}")
        
    print(f"\nPedidos com alta prioridade total: {altas}")
    
    maior_volume = -1
    nome_destaque = "Nenhum"
    for ent in entregadores:
        if len(ent['id_pedido']) > maior_volume:
            maior_volume = len(ent['id_pedido'])
            nome_destaque = ent['nome']
            
    print(f"Entregador com mais entregas ativas/alocadas: {nome_destaque} ({maior_volume} rotas)")

def criar_id():
    letra = random.choice(string.ascii_letters)
    numeros = random.randint(0, 9999)
    id = letra + str(numeros)
    return id
def menu_principal():
        a = 0
        while a != 7:
            print("""
                  --------------
                  MENU PRINCIPAL
                  --------------""")
            a = int(input('1-Cadastrar Pedidos\n2-Cadastrar Entregador\n3-Atualizar Pedidos\n4-Consultas\n5-Relatórios\n6-Fechar Sistema\n\nEscolha uma opção: '))
            match a:
                case 1:
                    cadastrar_pedido()
                case 2:
                    cadastrar_entregador()
                case 3:
                    atualizar_pedido()
                case 4:
                    consultas() 
                case 5:
                    relatorios()
                case 6:
                    break
        

menu_principal()
