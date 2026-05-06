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
    if pressão <= 150 and pressão>=120:
        pressão_ajustada = pressão*0.96
            
    elif pressão > 150:
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
        print(f"A pressão {pressão:.2f} continuará sendo {pressão_ajustada:.2f}")
    else:
        print(f"A pressão {pressão:.2f} foi ajustada para {pressão_ajustada:.2f}")

    if 180>=pressão_ajustada>=120:
        zona_verde+=1
        consecutivas_vermelha= 0
        print("A pressão está na zona verde")
    elif 250>=pressão_ajustada>180 or pressão_ajustada<120:
        zona_amarela+=1
        consecutivas_vermelha= 0
        print("A pressão está na zona amarela")
    elif pressão_ajustada>250:
        zona_vermelha+=1
        consecutivas_vermelha+=1
        print(f"ALERTA: pressão {pressão_ajustada:.2f} na zona vermelha")

    soma_ajustadas+= pressão_ajustada 

    if consecutivas_vermelha==2:    
        print(f"\nPROTOCOLO DE TRAVAMENTO")
        percent_de_leituras=(i/num_de_leituras)*100
        print(f"O percentual de leituras realizadas foi de {percent_de_leituras:.2f}%")
        print(f"O número de leituras realizadas foi {i}") 
        break

media_ajustadas = soma_ajustadas/i
porcentagem_verde=(zona_verde/i)*100
print(f"\nRELATÓRIO")
print(f"Foram concluídas {i} leituras de um total de {num_de_leituras} planejadas.")
print(f"A menor pressão após o ajuste foi de {menor:.2f}")
print(f"A maior pressão após o ajuste foi de {maior:.2f}")
print(f"A média das pressões ajustadas foi de {media_ajustadas:.2f}")
print(f"A porcentagem de leituras verdes foi de {porcentagem_verde:.2f}%\n")
