def cadastrar_pedido():
    novo_pedido = {
        'id_pedido': 0,
        'nome_cliente': 0,
        'endereco': 0,
        'prioridade': 0,
        'descricao_pedido': 0,
        'status_pedido': 0,
        'id_entregador': 0
    }
    for key in novo_pedido:
        if key == 'id_pedido':
            pass
        else: 
            dado = input(f"Insira o dado do {key}\n")
            novo_pedido[key] = dado


cadastrar_pedido()