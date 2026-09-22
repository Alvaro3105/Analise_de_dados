# Atividade de Fixação 05 - Aplicação para Análise de Dados

Projeto desenvolvido para a disciplina de Python, com foco em análise e tratamento de dados utilizando **Pandas, NumPy e Matplotlib**.

A proposta da atividade é simular o trabalho de um Cientista de Dados em uma fintech, realizando limpeza, transformação, análise estatística, detecção de possíveis anomalias e geração de um relatório visual a partir de dados de transações financeiras.

## Professor

**Rubens Lemos da Cruz Junior**

## Autor

**Álvaro Pires**

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib

## Arquivos do projeto

- `app.py` - aplicação principal responsável pelo tratamento e análise dos dados.
- `criar_dados.py` - script utilizado para gerar os arquivos CSV da atividade.
- `transacoes.csv` - base com os dados das transações financeiras.
- `cotacoes.csv` - base com dados de cotações gerada pelo script fornecido.
- `.gitignore` - impede o envio de arquivos desnecessários para o repositório.

Ao executar a aplicação também são gerados:

- `transacoes_filtradas.csv`
- `anomalias.csv`
- `tabela_dinamica.csv`
- `relatorio_transacoes.png`

## Funcionalidades implementadas

A aplicação realiza as seguintes etapas:

1. Leitura do arquivo `transacoes.csv` utilizando encoding `latin1`.
2. Tratamento dos valores ausentes da coluna `valor`, preenchendo os valores com a mediana de cada estado.
3. Criação da coluna `plataforma` com o valor fixo `Mobile`.
4. Conversão de `data_transacao` para datetime.
5. Aplicação do fuso horário `America/Sao_Paulo`.
6. Criação das colunas de dia da semana e mês utilizando o acessor `.dt`.
7. Remoção de transações duplicadas, mantendo a primeira ocorrência.
8. Filtro vetorizado das transações de setembro:
   - realizadas em SP ou RJ;
   - com valor superior a R$ 5.000,00;
   - utilizando os operadores bitwise `&` e `|`.
9. Associação do nível de risco de cada cliente através de um dicionário e do método `.map()`.
10. Criação de uma tabela dinâmica com `pivot_table()`, agrupando os valores por mês e nível de risco, com totais através de `margins=True`.
11. Cálculo vetorizado do Z-Score do valor das transações por estado.
12. Identificação de possíveis anomalias utilizando o critério `Z-Score > 2.5`.
13. Cálculo do valor total de transações por dia.
14. Cálculo da média móvel de 7 dias com `.rolling(7).mean()`.
15. Geração de um gráfico utilizando a API orientada a objetos do Matplotlib.

## Regra utilizada para o Z-Score

O Z-Score é calculado pela fórmula:

```text
Z = (x - média) / desvio padrão
```

As transações que apresentam:

```text
Z > 2.5
```

são separadas como possíveis anomalias para análise.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Alvaro3105/Analise_de_dados.git
```

Depois entre na pasta:

```bash
cd Analise_de_dados
```

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
```

Ative o ambiente:

```powershell
venv\Scripts\activate
```

### 3. Instalar as bibliotecas

```bash
pip install pandas numpy matplotlib
```

### 4. Gerar os dados

Caso seja necessário gerar novamente os arquivos de entrada:

```bash
python criar_dados.py
```

### 5. Executar a análise

```bash
python app.py
```

## Resultados gerados

Ao final da execução, a aplicação salva os principais resultados em arquivos separados:

| Arquivo | Descrição |
|---|---|
| `transacoes_filtradas.csv` | Transações de setembro em SP ou RJ com valor acima de R$ 5.000 |
| `anomalias.csv` | Transações identificadas com Z-Score maior que 2.5 |
| `tabela_dinamica.csv` | Soma dos valores agrupados por mês e nível de risco |
| `relatorio_transacoes.png` | Gráfico com o total diário e a média móvel de 7 dias |

## Gráfico

O relatório visual apresenta duas linhas:

- valor total das transações por dia;
- média móvel de 7 dias.

O eixo Y inicia em zero e o gráfico possui título, legenda, identificação dos eixos e grade para facilitar a visualização.

---

Projeto desenvolvido como atividade acadêmica de fixação sobre análise de dados em Python.
