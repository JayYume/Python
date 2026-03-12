import requests
import pandas as pd
import streamlit as st

st.title("Pokemon Stat Comparison")

@st.cache_data
def get_stats(name):
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}")
    if r.status_code == 200:
        data = r.json()
        stats = {}
        for stat in data["stats"]:
            stat_name = stat["stat"]["name"]
            base_value = stat["base_stat"]
            stats[stat_name] = base_value
        return stats
    else:
        return None

names_input = st.text_input("Enter pokemon names, use commas: ") or "Charizard"

if st.button("Compare"):
    names = [n.strip() for n in names_input.split(",") if n.strip()]
    rows = {}
    
    for name in names:
        stats = get_stats(name)
        if stats:
            rows[name.title()] = stats
        else:
            st.warning(f"'{name}' not found - skipping.")

    if rows:
        df = pd.DataFrame(rows).T
        df.columns = [c.replace("-", " ").title() for c in df.columns]
        
        st.bar_chart(df)
        st.dataframe(df)