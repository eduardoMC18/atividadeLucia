def menu_leituras(): 
    num_de_leituras = int(input("\nDigite o num de leituras:"))
    i = 0
    zona_vermelha=0
    consecutivas_vermelha=0
    zona_verde=0
    zona_amarela=0
    pressão_ajustada=0
    soma_ajustadas = 0
    menor = 0
    maior = 0

    while i < num_de_leituras:
        pressão = float(input("\nDigite a pressão:")) 
        if pressão < 120:
            pressão_ajustada = pressão 
        elif pressão <= 150 and pressão>=120:
            pressão_ajustada = pressão*0.96
                
        else:
            pressão_ajustada = pressão*1.08
        if i == 0:
            menor=pressão_ajustada
            maior=pressão_ajustada
        else:
            if pressão_ajustada < menor:
                menor = pressão_ajustada
            if pressão_ajustada > maior:
                maior = pressão_ajustada
            
        i+=1
        print(f"\nLEITURA {i}/{num_de_leituras}")
        
        if pressão<120:
            print(f"A pressão de {pressão:.2f} UPCs continuará sendo {pressão_ajustada:.2f} UPCs")
        else:
            print(f"A pressão de {pressão:.2f} UPCs foi ajustada para {pressão_ajustada:.2f} UPCs")

        if 180>=pressão_ajustada>=120:
            zona_verde+=1
            consecutivas_vermelha= 0
            print("A pressão está na ZONA VERDE")
        elif 250>=pressão_ajustada>180 or pressão_ajustada<120:
            zona_amarela+=1
            consecutivas_vermelha= 0
            print("A pressão está na ZONA AMARELA")
        elif pressão_ajustada>250:
            zona_vermelha+=1
            consecutivas_vermelha+=1
            print(f"ALERTA: pressão {pressão_ajustada:.2f} UPCs na ZONA VERMELHA")

        soma_ajustadas+= pressão_ajustada 

        if consecutivas_vermelha==2:    
            print(f"\nPROTOCOLO DE TRAVAMENTO")
            percent_de_leituras=(i/num_de_leituras)*100
            print(f"O percentual de leituras realizadas foi de {percent_de_leituras:.2f}%")
            print(f"O número de leituras realizadas foi {i}") 
            break

    if i > 0:
        media_ajustadas = soma_ajustadas/i
        porcentagem_verde=(zona_verde/i)*100
        print(f"\nRELATÓRIO")
        print(f"Foram concluídas {i} leituras de um total de {num_de_leituras} planejadas.")
        print(f"A menor pressão após o ajuste foi de {menor:.2f} UPCs")
        print(f"A maior pressão após o ajuste foi de {maior:.2f} UPCs")
        print(f"A média das pressões ajustadas foi de {media_ajustadas:.2f} UPCs")
        print(f"A porcentagem de leituras verdes foi de {porcentagem_verde:.2f}%\n")
        
    else:
        print(f"\nNenhuma leitura foi realizada para gerar o relatório.\n")
    continuar()

def continuar():
    print(f"Digite 1 para continuar as leituras do SEUC-4.\n")
    print(f"Digite 2 para retornar ao menu inicial.\n")

    opcao = int(input("Insira a opção!\n"))
    match opcao:
        case 1:
            menu_leituras()
        case 2:
            print(f"Retornando ao menu inicial...")
            menu_inicial()
        case _:
            print(f"Opção inválida!")
            continuar()



def login():
    usuários = [
    ['Eduardo Martins', 1234],
    ['Gustavo De Oliveira', 4321],
    ['Enzo Carletinhos', 5678],
    ['Pedro Businari', 8765]]

    nome = input(f"\nDigite o nome do usuario: ")
    senha = int(input(f"\nInforme a senha: "))

    login_sucesso = False
    for i in range(len(usuários)):
        if nome == usuários[i][0] and senha == usuários[i][1]:
            login_sucesso = True
            break
            
    
    if login_sucesso == True:
        print(f"\nEntrando...")   
        menu_leituras()

    else:
        print(f"\nErro no login.")
        login()
    
def menu_inicial():
    print(f"\nMENU INICIAL\n")
    print(f"Digite 1 para iniciar o SEUC-4.\n")
    print(f"Digite 2 para encerrar o sistema.\n")

    opcao = int(input("Insira a opção!\n"))
    match opcao:
        case 1:
            print(f"\nIniciando o SEUC-4...")
            login()
        case 2:
            print(f"\nEncerrando o SEUC-4...\n")
        case _:
            print(f"\nOpção inválida!\n")
            menu_inicial()


menu_inicial()
