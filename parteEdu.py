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
        elif key == 'status_pedido':
            dado = input(f"Insira o dado do(a) {key}: ")
            if dado not in ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']:
                validacao = False
                while not validacao:
                    dado = input('Por favor, escolha entre "Pendente", "Em Rota", "Entregue" ou "Cancelado"\n')
                    if dado not in ['Pendente', 'Em Rota', 'Entregue', 'Cancelado']:
                        validacao = False
                    else:
                        novo_pedido[key] = dado
                        validacao = True
            else:
                novo_pedido[key] = dado
        elif key == 'prioridade':
            dado = input(f"Insira o dado do(a) {key}: ")
            if dado not in ['Alta', 'Normal']:
                validacao = False
                while not validacao:
                    dado = input('Por favor, escolha entre "Alta" ou "Normal"\n')
                    if dado not in ['Alta', 'Normal']:
                        validacao = False
                    else:
                        novo_pedido[key] = dado
                        validacao = True
            else:
                novo_pedido[key] = dado

        else:
            dado = input(f"Insira o dado do(a) {key}: ")
            if novo_pedido[key] == 'nome_cliente' or 'endereco' or 'descricao_pedido' or 'status_pedido':
                novo_pedido[key] = dado
            else:
                dado = int(dado)
                novo_pedido[key] = dado
    pedidos.append(novo_pedido)
    print("ID: ",novo_pedido['id_pedido'])

def cadastrar_entregador():
    novo_entregador = entregador.copy()
    novo_entregador['id_pedido'] = []
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
                        pedidos = entregadores_pedidos()
                        novo_entregador['id_pedido'] = pedidos
                    else:       
                        if key == 'disponibilidade':
                            disp = disponibilidade(pedidos)
                            novo_entregador['disponibilidade'] = disp
    entregadores.append(novo_entregador)
    print(novo_entregador)

def atualizar_pedido(pedido):
    print(pedido)
    if pedido:
        a = int(input("Oque voce deseja alterar?\n\n1-Alterar Status\n2-Cancelar Pedido\n3-Associar Entregador\n4-Remover Associação de Entregador"))
        if a == 1:
            novo_status = input("Digite o status: ")
            pedido['status_pedido'] = novo_status
            print("ID: ",pedido['id_pedido'],'\nStatus: ',pedido['status_pedido'])
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
    pedido = None
    busca = input("Digite o ID do pedido:\n")
    for i in pedidos:
        print(i)
        if i['id_pedido'] == busca:
            pedido = i
            return pedido
    if not pedido:
        print('Pedido não encontrado')
        return False
        
        
def consultas():
    a = 0
    while a != 6:
        a = int(input('1-Pendentes\n2-Entregue\n3-Buscar Pedido\n4-Entregadores disponiveis\n5-Entregas realizadas por entregador\n6-Voltar ao menu\n\nEscolha uma opção: '))
        match a:
            case 1:
                pedido = None
                for i in pedidos:
                    if i['status_pedido'] == 'Pendente':
                        print(i)
                    pedido = i
                if not pedido:
                    print('Nenhum pedido pendente')
            case 2:
                pedido = None
                for i in pedidos:
                    if i['status_pedido'] == 'Entregue':
                        print(i)
                    pedido = i
                if not pedido:
                    print('Nenhum pedido a ser entregue')
            case 3:
                buscar_pedidos()
            case 4:
                entregador = None
                for i in entregadores:
                    if i['disponibilidade'] <= 10:
                        print(i)
                    entregador = i
                if not entregador:
                    print("Nenhum entregador disponivel")
            case 5:
                 for i in entregadores:
                    numero_pedido = 0
                    for w in i['id_pedido']:
                        print(w)
                        numero_pedido += 1
                        print('Id do pedido entregue:', w)
                    print('Total de pedidos entregues:', numero_pedido)
                         
    menu_principal()


def  relatorios():
    print(f"\nTotal de pedidos cadastrados: {len(pedidos)}")
    
    status_contagem = {'Pendente': 0, 'Em Rota': 0, 'Entregue': 0, 'Cancelado': 0}
    altas = 0
    for i in pedidos:
        status_contagem[i['status_pedido']] += 1
        print(i['prioridade'])
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

"Aqui acontece o cadastro de entregadores ---- APAGAR COMENTÁRIO DEPOIS"
def cadastrar_ID():
    numeros = random.randint(1000, 9999)
    id = str(numeros)
    print(f"o id {id} foi gerado")
    return id

def buscar_entregadores():
    print("Digite o ID do pedido:\n")
    for i in entregadores:
        busca = (input('Informe o ID do Pedido: '))
        if i['id_entregador'] == busca:
            return i

def cadastrar_veiculo():
    veiculos =  ["van", "moto", "carro"]
    veiculo = input("o veículo é van, moto, ou carro?").strip().lower()
    if veiculo in veiculos:
            return veiculo
            
    while veiculo not in veiculos:
        print("O veículo é van, moto, ou carro?")
        veiculo = input("escolha uma das três opções").strip().lower()
        if veiculo in veiculos:
            return veiculo
        
def cadastrar_nome():
    nome_entregador = input("nome completo:")
    print(f'''o entregador {nome_entregador} foi cadastrado ''')    
    return nome_entregador 

def entregadores_pedidos():
    pedidos = []
    num = int(input('Quantos pedidos esse entregador tem? '))
    for i in range(num):
        pedido = input(f'Digite o {i+1}º id: ')
        pedidos.append(pedido)
    return pedidos  
   
def disponibilidade(pedidos):
        tamanho = len(pedidos)
        if tamanho >= 9:
            return 'indisponível'
        elif tamanho <= 9:
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
                    pedido = buscar_pedidos()
                    atualizar_pedido(pedido)
                case 4:
                    consultas() 
                case 5:
                    relatorios()
                case 6:
                    break
        

menu_principal()
