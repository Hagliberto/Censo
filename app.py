import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Definir o layout
st.title("Situação do censo 2023")

# # Criar campos de entrada para cada coluna
# regional = st.sidebar.text_input("Regional")
# nome = st.sidebar.text_input("Nome")
# matricula = st.sidebar.text_input("Matrícula")
# data_censo = st.sidebar.text_input("Data do Censo")
# data_analise = st.sidebar.text_input("Data da Análise")
# status = st.sidebar.text_input("Status")

# # Criar um DataFrame com os dados inseridos manualmente
# df_manual = pd.DataFrame({
#     'Regional': [regional],
#     'Nome': [nome],
#     'Matrícula': [matricula],
#     'Data do Censo': [data_censo],
#     'Data da Análise': [data_analise],
#     'Status': [status]
# })

# Permitir upload de arquivo CSV ou XLSX
csv_file = st.file_uploader("Faça o upload do arquivo CSV ou XLSX", type=['csv', 'xlsx'])

if csv_file is not None:
    # Ler o arquivo CSV ou XLSX
    if csv_file.name.endswith('.xlsx'):
        df_original = pd.read_excel(csv_file)
    else:
        df_original = pd.read_csv(csv_file, sep=';', encoding='UTF8')

    # Exibir todos os dados em um expander
    with st.expander("Visualizar todos os dados"):
        st.write(df_original)

    # Pesquisar por termos nos dados originais
    search_term = st.text_input("Buscar em todas as colunas")
    if search_term:
        search_result = df_original[df_original.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        st.subheader("Resultados da Busca")
        st.write(search_result)

    # Análise entre regionais e status
    with st.expander("Análise entre Regionais e Status"):
        crosstab = pd.crosstab(df_original['Regional'], df_original['Status'])
        st.write(crosstab)
