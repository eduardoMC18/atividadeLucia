import random
import string

pedido = {
        'id_pedido': 0,
        'nome_cliente': 0,
        'endereco': 0,
        'prioridade': 0,
        'descricao_pedido': 0,
        'status_pedido': 'Pendente',
        'id_entregador': []
    }
entregador = {
    'id_entregador': 0,
    'nome': 0,
    'veiculo': 0,
    'id_pedido': [],
    'disponibilidade': 'disponível'
}
pedidos = []
entregadores = []

def cadastrar_pedido():
    novo_pedido = pedido.copy()
    novo_pedido['id_entregador'] = []
    for key in novo_pedido:
        if key == 'id_pedido':
            novo_pedido['id_pedido'] = criar_id()
        elif key == 'status_pedido':
            print("'Pendente', 'Em Rota', 'Entregue', 'Cancelado'")
            dado = input(f"Qual o status do pedido? ").strip().title()
            if dado not in ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']:
                validacao = False
                while not validacao:
                    dado = input('Por favor, escolha entre "Pendente", "Em Rota", "Entregue" ou "Cancelado"\n').strip().title()
                    if dado not in ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']:
                        validacao = False
                    else:
                        novo_pedido['status_pedido'] = dado
                        validacao = True
            else:
                novo_pedido[key] = dado
        elif key == 'prioridade':
            print("A prioridade deve ser Alta ou Normal!")
            dado = input(f"Insira o dado do(a) {key}: ").strip().title()
            if dado not in ['Alta', 'Normal']:
                validacao = False
                while not validacao:
                    dado = input('Por favor, escolha entre "Alta" ou "Normal"\n').strip().title()
                    if dado not in ['Alta', 'Normal']:
                        validacao = False
                    else:
                        novo_pedido['prioridade'] = dado
                        validacao = True
            else:
                novo_pedido[key] = dado
        elif key == 'descricao_pedido':
            dado = input(f"Qual é o produto a ser entregue? ")
            novo_pedido['descricao_pedido'] = dado
        elif key == 'endereco':
            dado = input("Qual o endereço? ")
            novo_pedido['endereco'] = dado
        elif key == 'nome_cliente':
            dado = input("Qual o nome do cliente? ")
            novo_pedido['nome_cliente'] = dado
        elif key == 'id_entregador':
            if entregadores == []:
                print("Nenhum entregador foi cadastrado ainda")
            else:
                disponiveis = []
                for i in entregadores:
                    if i['disponibilidade'] == 'disponível':
                        disponiveis.append(i)
                if disponiveis == []:
                    print("Todos os entregadores estão indisponíveis.")
                else:
                    for i in disponiveis:
                        print('ID do entregador:', i['id_entregador'])
                    ids_validos = []
                    for i in disponiveis:
                        ids_validos.append(i['id_entregador'])
                    dado = input("Digite o ID do entregador: ")
                    while dado not in ids_validos:
                        print("ID inválido, tente novamente.")
                        dado = input("Digite o ID do entregador: ")
                    novo_pedido['id_entregador'] = dado
                    for i in entregadores:
                        if i['id_entregador'] == dado:
                            i['id_pedido'].append(novo_pedido['id_pedido'])
                            i['disponibilidade'] = disponibilidade(i['id_pedido'])
                            break
            

    pedidos.append(novo_pedido)
    print(f'ID do pedido criado: {novo_pedido["id_pedido"]}')
    print(novo_pedido)

def cadastrar_entregador():
    novo_entregador = entregador.copy()
    novo_entregador['id_pedido'] = []
    lista_p = []

    for key in novo_entregador:
        if key == 'id_entregador':
            id = cadastrar_ID()
            novo_entregador['id_entregador'] = id
        else:
            if key == 'nome':
                nome_ent = cadastrar_nome()
                novo_entregador['nome'] = nome_ent
            else:
                if key == 'veiculo':
                    veiculo = cadastrar_veiculo()
                    novo_entregador['veiculo'] = veiculo

                else:
                    if key == 'id_pedido':
                        lista_p = entregadores_pedidos(novo_entregador['id_entregador'])
                        novo_entregador['id_pedido'] = lista_p
                    else:       
                        if key == 'disponibilidade':
                            disp = disponibilidade(lista_p)
                            novo_entregador['disponibilidade'] = disp
    entregadores.append(novo_entregador)
    print(novo_entregador)

def atualizar_pedido():
    pedido = buscar_pedidos()
    if pedido is None:
        print("Não há nenhum pedido, voltando ao menu principal...")
        return 
    print("1 para alterar status")
    print("2 para cancelar pedido")
    print("3 para associar entregador")
    print("4 para remover associação de entregador")
    a = int(input("Digite 1,2,3 ou 4: "))
    
    match a:
        case 1:
            novo_status = input("Digite o status: ")
            pedido['status_pedido'] = novo_status
            print(pedido)
        case 2:
            pedido['status_pedido'] = 'Cancelado'
            print(pedido)
        case 3:
            id_entregador = int(input('Digite o id do entregador: '))
            pedido['id_entregador'] = id_entregador
            print(pedido)
        case 4:
            pedido['id_entregador'] = None
            print(pedido)

def buscar_pedidos():
    ped = None 
    if pedidos == []:
        print("nenhumn pedido foi cadastrado")
        return  
    busca = input('Informe o ID do Pedido: ')
    for i in pedidos:
        if i['id_pedido'] == busca:
            ped = i
            print(ped)
            break
    if not ped:
        print("\nPedido não encontrado\n")
        return None
    return ped
        
def consultas():
    a = 0
    print('1- Pendentes')
    print('2- Entregue')
    print('3- Buscar Pedido')
    print('4- Buscar entregadores disponíveis')
    print('5- Todas as entregas por entregador ')
    print('6- Voltar ao Menu')
    while a != 6:
        a = int(input("digite de 1 a 6: "))
        match a:
            case 1:
                alta = []
                normal = []
                cont = 0
                for i in pedidos:
                    cont += 1
                    if i['status_pedido'] == 'Pendente':
                        if i['prioridade'] == 'Alta':
                            alta.append(f'{cont}º {i}')
                        else:
                            normal.append(f'{cont}º {i}')
                for i in alta + normal:
                    print(i)                    
    
            case 2:
                for i in pedidos:
                    if i['status_pedido'] == 'Entregue':
                        print(i)
            case 3:
                buscar_pedidos()
            case 4:
                pedido = None

                for i in entregadores:
                    if i['disponibilidade'] == 'disponível':
                        print(i)
                    pedido = i
                if pedido == None:
                    print("Não há entregadores disponíveis")
            case 5:
                 for i in entregadores:
                    numero_pedido = 0
                    for w in i['id_pedido']:
                        numero_pedido += 1
                        print('Id do pedido entregue:', w)
                    print('Total de pedidos entregues:', numero_pedido)
            case 6:
                pass

                         
    menu_principal()


def relatorios():
    print(f"\nTotal de pedidos cadastrados: {len(pedidos)}")
    
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
    numeros = random.randint(1000, 9999)
    id = letra + str(numeros)
    repetiu = True
    while repetiu == True:
        repetiu = False
        for p in pedidos:
            if id == p['id_pedido']:
                letra = random.choice(string.ascii_letters)
                numeros = random.randint(1000, 9999)
                id = letra + str(numeros)
                repetiu = True
    print(f"o id {id} foi gerado")
    return id


def buscar_entregadores():
    print("Digite o ID do pedido:\n")
    for i in entregadores:
        busca = (input('Informe o ID do Pedido: '))
        if i['id_entregador'] == busca:
            return i
        
"Aqui acontece o cadastro de entregadores ---- APAGAR COMENTÁRIO DEPOIS"
def cadastrar_ID ():
    numeros = random.randint(1000, 9999)
    id = str(numeros)
    repetiu = True
    while repetiu == True:
        repetiu = False
        for entregador in entregadores:
            if id == entregador["id_entregador"]:
                numeros = random.randint(1000, 9999)
                id = str(numeros)
                repetiu = True
    print(f"o id {id} foi gerado")
    return id


def cadastrar_veiculo():
    veiculos =  ["van", "moto", "carro"]
    veiculo = input("o veículo é van, moto, ou carro? ").strip().lower()
    if veiculo in veiculos:
            return veiculo

    while veiculo not in veiculos:
        print("O veículo é van, moto, ou carro?")
        veiculo = input("escolha uma das três opções ").strip().lower()
        if veiculo in veiculos:
            return veiculo

def cadastrar_nome():
    nome_entregador = input("nome completo: ").title()
    print(f'''o entregador {nome_entregador} foi cadastrado ''')    
    return nome_entregador 

def entregadores_pedidos(id_ent):
    orders = []
    pedidos_livres = []
    for i in pedidos:
        if i['id_entregador'] == []:
            pedidos_livres.append(i)
    
    if pedidos_livres == []:
        print("Não há pedidos disponíveis.")
        return []
    
    for i in pedidos_livres:
        print('ID do pedido:', i['id_pedido'])
    
    num = int(input('Quantos pedidos deseja associar a esse entregador? '))
    while num > 10 or num > len(pedidos_livres):
        if num > 10:
            print('Máximo de 10 pedidos por entregador')
            num = int(input('Quantos pedidos deseja associar a esse entregador? '))
        else:
            print(f'Máximo de {len(pedidos_livres)} pedidos disponíveis')
            num = int(input('Quantos pedidos deseja associar a esse entregador? '))
    i = 0
    while i < num:
        pedido = input(f'Digite o {i+1}º id: ')
        for k in pedidos_livres:
            if k['id_pedido'] == pedido:
                orders.append(pedido)
                k['id_entregador'] = id_ent
                break
        else:
            print('ID não existe ou já tem entregador')
            continue
        i += 1
    return orders

def disponibilidade(ped):
    tamanho = len(ped)
    if tamanho >= 9:
        return 'indisponível'
    return 'disponível'
               

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
