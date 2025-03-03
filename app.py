import requests
from bs4 import BeautifulSoup 
import streamlit as st

def get_player_stats(player_name, year):
    url = f'https://www.espn.com/soccer/player/stats/_/id/{player_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            stats_table = soup.find('div', {'class': 'PlayerStats__Container'})
            stats = []

            for stat in stats_table.find_all('div', {'class': 'Stat'}):
                label = stat.find('div', {'class': 'Stat__Label'}).text.strip()
                value = stat.find('div', {'class': 'Stat__Value'}).text.strip()
                stats.append((label, value))

            return stats
        except AttributeError:
            return "Estatísticas não encontradas para este jogador."   
        else:
            return f"Erro ao acessar a página do jogador: {response.status_code}."

st.title('Estatísticas de Jogadores de Futebol')

year = st.selectbox("Escolha o ano:", [2025, 2024, 2023, 2022])
player_name = st.text_input("Digite o nome do jogador:")

if st.button("Buscar"):
    if player_name:
        stats = get_player_stats(player_name, year)
        if isinstance(stats, list):
            st.write(f"Estatísticas de {player_name} em {year}:")
            for label, value in stats:
                st.write(f"{label}: {value}")
        else:
            st.write(stats)  # Caso não encontre as estatísticas
    else:
        st.write("Por favor, insira o nome do jogador.")


