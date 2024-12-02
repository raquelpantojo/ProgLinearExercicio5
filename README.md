# ProgLinearExercicio5

Trabalho final da disciplina de **Programação Linear** na **Fatec Ribeirão Preto**.

Este projeto foi desenvolvido pelos alunos da Fatec Ribeirão Preto como parte do trabalho final da disciplina de Programação Linear.
**:**
- Ângelo Imon  [@Angelo Imon](https://github.com/ImonHBnLT)
- João Vitor Bravo Arruda  
- Mariana Taba  
- Melissa Nascimento  
- Raquel Pantojo  

**Professor:**  
Prof. Me. Júnior Bonafim

---

## 📝 Problema


Uma empresa possui um call center com demanda variável de acordo com o período do dia. O número mínimo de funcionários em cada período é exemplificado na tabela abaixo: 
![image](https://github.com/user-attachments/assets/8badecff-99d7-430b-9b42-f8afe22f2024)


Devido a acordos trabalhistas, a jornada diária de um funcionário deve ser de 6 horas. Para horas trabalhadas entre as 22:00 e 05:00 deve-se pagar adicional noturno que representa um acréscimo de 20% no valor da hora trabalhada.  

a) Sabendo que um funcionário pode começar seu turno de trabalho em qualquer hora exata do dia (03:00, 8:00, 16:00, por exemplo), determine o número de funcionários que devem iniciar seu turno de trabalho em cada hora do dia a fim de que a empresa mantenha seu nível de atendimento e minimize os custos salariais.  

b) Considere que a empresa deseja que as entradas de funcionários ocorram em apenas m momentos do dia (horas exatas com anteriormente). Determine quais são estes momentos e o número de funcionários que entrarão em cada um deles de modo que se minimize os custos salariais. 



---
## 🔍 Objetivos

### a) Turnos livres
Determinar quantos funcionários devem iniciar o turno em cada hora do dia para minimizar os custos salariais, atendendo à demanda mínima em cada período.

### b) Turnos fixos
Definir os **m** horários fixos de entrada e o número de funcionários em cada um, de forma a minimizar os custos.

---

## 📂 Arquivos de Instância

Os arquivos a seguir fornecem os dados para testar os modelos:

- `inst_4a.txt`  
- `inst_4b.txt`  
- `inst_5a.txt`  
- `inst_5b.txt`  
- `inst_6a.txt`  
- `inst_6b.txt`  

**Formato:**
- A primeira linha contém o valor de **m** (apenas para o item b).
- As linhas subsequentes contêm o número mínimo de funcionários necessários por intervalo de tempo.

---

## 🧮 Implementação

A implementação foi realizada em Python utilizando a biblioteca **Gurobi** para resolver o problema de otimização linear. 

**Principais etapas do código:**
1. **Leitura de dados:**  
   Funções para carregar informações dos arquivos de entrada (`Tab_Func.txt` e arquivos de instâncias).
   
2. **Modelo de otimização:**  
   - Variáveis de decisão:
     - `x[i]`: número de funcionários que iniciam o turno no horário `i`.
     - `Q[i]`: número total de funcionários no horário `i`.
     - `y[i]`: variável binária que identifica se o horário `i` é usado como entrada no item b.
   - Função objetivo: Minimizar os custos salariais.
   - Restrições:
     - Atender à demanda mínima em cada período.
     - Garantir o limite de horários de entrada (item b).

3. **Execução do modelo:**  
   Processamento dos arquivos de instância em loop, ajustando as restrições conforme necessário.

---

## 📊 Resultados

O código retorna:
- Horários de entrada dos funcionários.
- Número de funcionários total em cada período.
- Custo total (função objetivo) para cada instância.


## 🚀 Como Executar

1. Certifique-se de ter o **Gurobi** instalado e configurado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/ProgLinearExercicio5.git

