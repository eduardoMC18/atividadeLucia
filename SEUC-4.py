from rich import print

def menu_leituras():
    numLeituras = int(input("Quantidade de leituras que serão realizadas no seu turno: "))
    somaLeituras = 0
    zonaVermelha = 0
    menorLeitura = 999999
    leiturasVerdes = 0
    leiturasRealizadas = 0 

    while leiturasRealizadas < numLeituras:
        leituraAtual = int(input("Leitura(UPCs): "))

        if leituraAtual > 150:
            leituraAtual *= 1.08
        else:
            leituraAtual *= 0.96
        print(leituraAtual)
        somaLeituras += leituraAtual

        if leituraAtual < menorLeitura:
            menorLeitura = leituraAtual


        if leituraAtual >= 250:
            print("[red]ZONA VERMELHA[/red]")
            zonaVermelha += 1
        else:
            if 120 <= leituraAtual <= 180:
                
                leiturasVerdes += 1
            else:

                if leituraAtual < 250 or leituraAtual < 120:
                    print('[yellow]ZONA AMARELA[/yellow]')

            zonaVermelha = 0


        if zonaVermelha >= 2:
            print("[red]TRAVAMENTO[/red]")
            leiturasRealizadas +=1
            break
        leiturasRealizadas+=1


    porcentagemVerde = (leiturasVerdes/numLeituras) * 100
    relatorio = f"""
        [green]RELATÓRIO[/green]
            Media das pressões: [blue]{somaLeituras/leiturasRealizadas:.2f} [/blue]
            Menor Leitura: [blue]{menorLeitura:.2f} [/blue]
            Porcentagem de leituras verdes: [green]{porcentagemVerde:.2f}% [/green]
    """
    if zonaVermelha >= 2:
        porcentagemRealizada = (leiturasRealizadas/numLeituras) * 100
        relatorio += f"        Porcentagem de leituras realizadas: {porcentagemRealizada:.2f}%"
        print(relatorio)
    else:
        print(relatorio)




def login():
    usuarios = [['Eduardo Martins', 1234, 0], ['Gustavo De Oliveira', 4321, 0], ['Enzo Carletinhos', 5678, 0]]
    nome = input("Digite o nome do usuario: ")
    senha = int(input("Informe a senha: "))

    for usuario in usuarios:
        if nome == usuario[0]:
            if senha == usuario[1]:
                print("Login realizado com sucesso\n")
                menu_leituras()
    print("Usuário ou senha incorretos")

login()