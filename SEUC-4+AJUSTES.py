num_de_leituras = int(input("digite o num de leituras:"))
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
    pressão = float(input("digite a pressão:"))
    if pressão<=124.8:
        pressão = float(input("digite a pressão:"))
        i-=1
    if pressão <= 150 and pressão>124.8:
        pressão_ajustada = pressão*0.96
            
    elif pressão > 150:
        pressão_ajustada = pressão*1.08
    if i == 1:
        menor=pressão_ajustada
        maior=pressão_ajustada
    else:
        if pressão_ajustada < menor:
            menor = pressão_ajustada
        else:
            if pressão_ajustada > maior:
                maior = pressão_ajustada 
    i+=1

    if 180>=pressão_ajustada>=120:
        zona_verde+=1
    elif 250>=pressão_ajustada>180:
        zona_amarela+=1
    elif pressão_ajustada>250:
        zona_vermelha+=1
        consecutivas_vermelha+=1
    else:
        consecutivas_vermelha= 0

    if consecutivas_vermelha==2:    
        print("protocolo de travamento")
        percent_de_leituras=(i/num_de_leituras)*100
        print(f"{percent_de_leituras:.2f}%")
        break
            
    
    soma_ajustadas+= pressão_ajustada 

media_ajustadas = soma_ajustadas/i
porcentagem_verde=(zona_verde/i)*100
print(f"\nRELAÓRIO")
print(f"{menor:.2f}")
print(f"{media_ajustadas:.2f}")
print(f"{porcentagem_verde:.2f}%")
