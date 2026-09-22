import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(
    "transacoes.csv",
    encoding="latin1"
)

print("\nDados carregados:")
print(df.head())


df["valor"] = df["valor"].fillna(
    df.groupby("estado_cliente")["valor"].transform("median")
)

print("\nValores nulos após o tratamento:")
print(df.isna().sum())


df["plataforma"] = "Mobile"


df["data_transacao"] = pd.to_datetime(
    df["data_transacao"]
).astype("datetime64[ns]")

df["data_transacao"] = df["data_transacao"].dt.tz_localize(
    "America/Sao_Paulo"
)

print("\nTipo da coluna data_transacao:")
print(df["data_transacao"].dtype)


df["dia_semana"] = df["data_transacao"].dt.day_name()
df["mes"] = df["data_transacao"].dt.month

print("\nDatas tratadas:")
print(
    df[
        [
            "data_transacao",
            "dia_semana",
            "mes"
        ]
    ].head()
)


quantidade_antes = len(df)

df = df.drop_duplicates(
    keep="first"
)

quantidade_depois = len(df)

print("\nQuantidade antes de remover duplicados:", quantidade_antes)
print("Quantidade depois de remover duplicados:", quantidade_depois)
print(
    "Duplicados removidos:",
    quantidade_antes - quantidade_depois
)


filtro = (
    (df["mes"] == 9)
    &
    (
        (df["estado_cliente"] == "SP")
        |
        (df["estado_cliente"] == "RJ")
    )
    &
    (df["valor"] > 5000)
)

df_filtrado = df[filtro]

print("\nTransações filtradas:")
print(df_filtrado.head())

print("\nQuantidade de transações filtradas:")
print(len(df_filtrado))


risco_dict = {
    "C100": "Baixo",
    "C101": "Alto",
    "C102": "Medio",
    "C103": "Baixo",
    "C104": "Alto"
}

df["nivel_risco"] = df["id_cliente"].map(risco_dict)

print("\nNíveis de risco:")
print(
    df[
        [
            "id_cliente",
            "nivel_risco"
        ]
    ].head()
)


tabela_dinamica = pd.pivot_table(
    df,
    index="mes",
    columns="nivel_risco",
    values="valor",
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)

print("\nTabela dinâmica:")
print(tabela_dinamica)


def calcular_zscore(valores):
    media = valores.mean()
    desvio = valores.std(ddof=0)

    return (valores - media) / desvio


df["z_score"] = (
    df.groupby("estado_cliente")["valor"]
    .transform(calcular_zscore)
)


df_anomalias = df[
    df["z_score"] > 2.5
].copy()

print("\nPossíveis anomalias/fraudes:")
print(
    df_anomalias[
        [
            "id_cliente",
            "estado_cliente",
            "valor",
            "z_score"
        ]
    ]
)

print("\nQuantidade de possíveis anomalias:")
print(len(df_anomalias))


total_diario = (
    df.set_index("data_transacao")
    .resample("D")["valor"]
    .sum()
)


media_movel_7_dias = total_diario.rolling(7).mean()


fig, ax = plt.subplots(
    figsize=(12, 6)
)

ax.plot(
    total_diario.index,
    total_diario.values,
    label="Total diário de transações"
)

ax.plot(
    media_movel_7_dias.index,
    media_movel_7_dias.values,
    label="Média móvel de 7 dias"
)

ax.set_title(
    "Desempenho das Transações Financeiras"
)

ax.set_xlabel(
    "Data"
)

ax.set_ylabel(
    "Valor total das transações (R$)"
)

ax.set_ylim(
    bottom=0
)

ax.legend()

ax.grid(
    True,
    alpha=0.3
)

fig.autofmt_xdate()

plt.tight_layout()

plt.savefig(
    "relatorio_transacoes.png"
)

plt.show()


df_filtrado.to_csv(
    "transacoes_filtradas.csv",
    index=False,
    encoding="utf-8"
)

df_anomalias.to_csv(
    "anomalias.csv",
    index=False,
    encoding="utf-8"
)

tabela_dinamica.to_csv(
    "tabela_dinamica.csv",
    encoding="utf-8"
)

print("\nArquivos gerados com sucesso!")