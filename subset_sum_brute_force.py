def encontrar_subconjunto_soma_zero_com_passos(arr):
    n = len(arr)
    print(f"\n--- Iniciando a busca de subconjuntos para: {arr} ---")
    
    # Iterar de 1 a 2^n - 1 para gerar todas as combinações de subconjuntos não vazios
    for i in range(1, 1 << n):  # 1 << n é equivalente a 2^n
        subconjunto_atual = []
        soma_atual = 0
        
        print(f"\nTentativa de combinação (índice binário {i:0{n}b}):") # Mostra a combinação binária
        
        for j in range(n):
            # Se o j-ésimo bit de 'i' for 1, incluir o elemento no subconjunto
            if (i >> j) & 1:
                subconjunto_atual.append(arr[j])
                soma_atual += arr[j]
                print(f"  Incluindo o elemento: {arr[j]} (na posição {j})")
            else:
                print(f"  Excluindo o elemento: {arr[j]} (na posição {j})")
        
        print(f"  Subconjunto formado: {subconjunto_atual}")
        print(f"  Soma do subconjunto: {soma_atual}")
        
        if soma_atual == 0:
            print(f"  *** Subconjunto encontrado que soma zero! ***")
            return subconjunto_atual
            
    print(f"\n--- Nenhum subconjunto que soma zero foi encontrado para: {arr} ---")
    return None  # Retorna None se nenhum subconjunto que soma zero for encontrado

# Exemplos de uso com os passos:
conjunto_passos1 = [-7, -3, -2, 5, 8]
resultado_passos1 = encontrar_subconjunto_soma_zero_com_passos(conjunto_passos1)
if resultado_passos1:
    print(f"Resultado final para {conjunto_passos1}: {resultado_passos1}")
else:
    print(f"Resultado final para {conjunto_passos1}: Nenhum subconjunto encontrado.")

conjunto_passos2 = [1, 2, 3]
resultado_passos2 = encontrar_subconjunto_soma_zero_com_passos(conjunto_passos2)
if resultado_passos2:
    print(f"Resultado final para {conjunto_passos2}: {resultado_passos2}")
else:
    print(f"Resultado final para {conjunto_passos2}: Nenhum subconjunto encontrado.")

conjunto_passos3 = [0]
resultado_passos3 = encontrar_subconjunto_soma_zero_com_passos(conjunto_passos3)
if resultado_passos3:
    print(f"Resultado final para {conjunto_passos3}: {resultado_passos3}")
else:
    print(f"Resultado final para {conjunto_passos3}: Nenhum subconjunto encontrado.")