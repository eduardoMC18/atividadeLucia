# from rich import print

def menu_leituras():
    numLeituras = int(input("Quantidade de leituras que serão realizadas no seu turno: "))
    somaLeituras = 0
    zonaVermelha = 0
    menorLeitura = 999999
    leiturasVerdes = 0
    leiturasRealizadas = 0 

    while leiturasRealizadas < numLeituras:
        leituraAtual = int(input("Leitura(UPCs): "))
        somaLeituras += leituraAtual

        if leituraAtual < menorLeitura and leituraAtual > 120:
            menorLeitura = leituraAtual


        if leituraAtual >= 250:
            print("[yellow]ZONA VERMELHA[/yellow]")
            zonaVermelha += 1
        else:
            if 120 <= leituraAtual <= 180:
                
                leiturasVerdes += 1
            else:
                if leituraAtual < 120:
                    print("Dado menor que 120, não lido")
                    leiturasRealizadas -= 1
                    somaLeituras -= leituraAtual


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
            Menor Leitura: [blue]{menorLeitura} [/blue]
            Porcentagem de leituras verdes: [green]{porcentagemVerde:.2f}% [/green]
    """
    if zonaVermelha >= 2:
        porcentagemRealizada = (leiturasRealizadas/numLeituras) * 100
        relatorio += f"        Porcentagem de leituras realizadas: {porcentagemRealizada:.2f}%"
        print(relatorio)




def login():
    u1 = ['Eduardo Martins', 1234, 0]
    u2 = ['Gustavo De Oliveira', 4321, 0]
    u3 = ['Enzo Carletinhos', 5678, 0]
    nome = input("Digite o nome do usuario: ")
    senha = int(input("Informe a senha: "))
    if (nome == u1[0] or nome == u2[0] or nome == u3[0]) and (senha == u1[1] or senha == u2[1] or senha == u3[1]):
        print("Entrando...")
        menu_leituras()
    else:
        print("Erro no login")
login()