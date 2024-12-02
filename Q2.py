# Questão 2

import gurobipy as gp

# Função para ler dados do arquivo Tab_Func.txt
def ler_dados_tab_func(nome_arquivo):
    identificadores = [] # Cria vetor de identificadores de horários
    horarios = [] # Cria vetor de horários
    quantidades_minimas_empregados = [] # Cria vetor de quantidades mínimas de empregados
    multiplicadores_salario = [] # Cria vetor de multiplicadores de salário pela hora
    
    with open(nome_arquivo, 'r') as arquivo: 
        for linha in arquivo: # Loop para cada linha do arquivo
            partes = linha.strip().split() # Dividir a linha em partes
            identificadores.append(int(partes[0])) # Adicionar o identificador do horário
            horarios.append(partes[1]) # Adicionar o horário
            quantidades_minimas_empregados.append(int(partes[2])) # Adicionar a quantidade mínima de empregados
            multiplicadores_salario.append(float(partes[3])) # Adicionar o multiplicador de salário
    return identificadores, horarios, quantidades_minimas_empregados, multiplicadores_salario # Retornar os vetores

# Ler dados do arquivo Tab_Func.txt
identificadores, horarios, quantidades_minimas_empregados, multiplicadores_salario = ler_dados_tab_func('Tab_Func.txt')

# Imprimir os dados lidos
#print("Dados lidos do arquivo Tab_Func.txt:")
for identificador, horario, quantidade_minima_empregado, multiplicador_salario in zip(identificadores, horarios, quantidades_minimas_empregados, multiplicadores_salario):
    print(f"Período: {identificador}, Horário: {horario}, Quantidade Minima de Empregados: {quantidade_minima_empregado}, Salário: {multiplicador_salario}")

# Criando um modelo de otimização
modelo = gp.Model()

# Criando variáveis de decisão
x = modelo.addVars(len(identificadores), name="x")  # Funcionários que entram na hora i
Q = modelo.addVars(len(identificadores), name="Q")  # Quantidade total de funcionarios na hora i
y = modelo.addVars(len(identificadores), name="y", vtype=gp.GRB.BINARY) # Indentificar 

# Função objetivo
modelo.setObjective(gp.quicksum(Q[i]*multiplicadores_salario[i] for i in range(len(identificadores))), sense=gp.GRB.MINIMIZE)

# Restrições
modelo.addConstrs(
    (gp.quicksum(x[j%24] for j in range(i-5, i+1)) == Q[i] for i in range(len(identificadores))), name="Restrição de quantidade total de empregados"
)

modelo.addConstrs(
    (Q[i] >= quantidades_minimas_empregados[i] for i in range(len(identificadores))), name="Restrição de quantidade mínima de empregados"
)

# Suprimir saída no terminal
modelo.setParam("OutputFlag", 0)

# Resolver o modelo
modelo.optimize()


# Lista de arquivos de instâncias
arquivos_instancias = ['inst_4a.txt', 'inst_4b.txt', 'inst_5a.txt', 'inst_5b.txt', 'inst_6a.txt', 'inst_6b.txt']

# Função para ler dados de instâncias USANDO A PRIMEIRA LINHA
def ler_dados_instancia(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        # A primeira linha contém o tamanho do vetor M
        M = int(linhas[0].strip())
        
        # As linhas subsequentes contêm as quantidades mínimas de empregados
        quantidades_minimas_empregados = [int(linha.strip()) for linha in linhas[1:]]
        
    return M, quantidades_minimas_empregados


# Loop para processar cada arquivo de instância
for arquivo_instancia in arquivos_instancias:
    # Lendo os dados da instância
    M, quantidades_minimas_empregados_instancia = ler_dados_instancia(arquivo_instancia)

    # Exemplo de uso do vetor M
    print(f"Vetor M (tamanho definido pela primeira linha): {M}")

    
    # Verificar se o número de quantidades mínimas de empregados na instância corresponde ao número de identificadores únicos
    if len(quantidades_minimas_empregados_instancia) != len(set(identificadores)):
        print(f"Erro: O número de quantidades mínimas de empregados na instância {arquivo_instancia} não corresponde ao número de identificadores únicos.")
        continue

    # Repetir as quantidades mínimas de empregados para cada identificador
    quantidades_minimas_empregados = []
    for i in range(len(identificadores)):
        periodo = identificadores[i]
        quantidades_minimas_empregados.append(quantidades_minimas_empregados_instancia[periodo - 1])
    
    # Remover as restrições antigas
    modelo.remove(modelo.getConstrs())

    # Adicionar novas restrições com os vetores atualizados
    modelo.addConstrs(
        (gp.quicksum(x[j%24] for j in range(i-5, i+1)) == Q[i] for i in range(len(identificadores))), name="Restrição de quantidade total de empregados"
    )

    modelo.addConstrs(
        (Q[i] >= quantidades_minimas_empregados[i] for i in range(len(identificadores))), name="Restrição de quantidade mínima de empregados"
    )

    modelo.addConstr(
        gp.quicksum(y[i] for i in range(len(identificadores))) <= M, name="..."
    )

    modelo.addConstrs(
        (x[j]  <= 1000*y[j] for j in range(len(identificadores))), name="..."
    )
    
    # Imprimir os dados lidos
    print(f"Dados atualizados {arquivo_instancia}:") 
    
    # Resolver o modelo novamente
    modelo.optimize()
    
    # Imprimir a solução para a instância atual
    print(f"\n=== Solução para {arquivo_instancia} ===")
    for i in range(len(identificadores)):
        if x[i].x > 0:
            print(f"Horário {horarios[i]}:00 - Entrada {x[i].x:.0f}, Total {Q[i].x:.0f}")
    print(f"Custo total (objetivo): {modelo.objVal}")
    print(" ")