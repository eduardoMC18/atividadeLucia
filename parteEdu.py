def cadastrar_pedido():
    novo_pedido = {
        'id_pedido': 0,
        'nome_cliente': 0,
        'endereco': 0,
        'prioridade': 0,
        'descricao_pedido': 0,
        'status_pedido': 'Pendente',
        'id_entregador': 0
    }
    for key in novo_pedido:
        if key == 'id_pedido':
            pass
        else: 
            dado = input(f"Insira o dado do {key}\n")
            novo_pedido[key] = dado

def buscar_pedidos():
    repeat = 0
    print("Digite o ID do pedido:\n")
    while repeat == 0:
        buscar = int(input(""))
        if buscar != novo_pedido['id_pedido']:
            print("Erro, o ID não existe, digite outro ID:\n")
        else:
            print(novo_pedido)
            repeat = 1
    
buscar_pedidos()

cadastrar_pedido()
