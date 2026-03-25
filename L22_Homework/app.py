import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# 1. Setup Page Config
st.set_page_config(page_title="Crypto Tracker", layout="wide")
st.title("📈 Cryptocurrency Market Dashboard")

# 2. Cached API Fetching Function
@st.cache_data
def fetch_data(url, params=None):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch data from API: {e}")
        return None

# --- SIDEBAR: USER INPUTS ---
st.sidebar.header("Dashboard Settings")

# Input 1: Select Coin (Dropdown)
coin_choice = st.sidebar.selectbox(
    "Select Cryptocurrency",
    options=["bitcoin", "ethereum", "solana", "cardano", "dogecoin"],
    index=0
)

# Input 2: Date Range (Slider)
days_choice = st.sidebar.slider("Historical Data Range (Days)", 1, 30, 7)

# --- DATA PROCESSING ---
# Base URL for CoinGecko
BASE_URL = "https://api.coingecko.com/api/v3"

# Fetch Current Market Data for Metric
market_data = fetch_data(f"{BASE_URL}/coins/markets", params={
    "vs_currency": "usd",
    "ids": coin_choice
})

# Fetch Historical Data for Time Series Chart
history_data = fetch_data(f"{BASE_URL}/coins/{coin_choice}/market_chart", params={
    "vs_currency": "usd",
    "days": days_choice,
    "interval": "daily"
})

if market_data and history_data:
    # Transform Market Data
    current_price = market_data[0]['current_price']
    price_change = market_data[0]['price_change_percentage_24h']
    
    # Transform Historical Data into Pandas DataFrame
    df = pd.DataFrame(history_data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    # --- DASHBOARD COMPONENTS ---
    
    # Component 1: Metric Display
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=f"Current {coin_choice.title()} Price", 
                  value=f"${current_price:,.2f}", 
                  delta=f"{price_change:.2f}% (24h)")

    # Component 2: Time Series Chart (Required)
    st.subheader(f"{coin_choice.title()} Price Trend (Last {days_choice} Days)")
    st.line_chart(df.set_index('timestamp'))

    # Component 3: Data Table
    with st.expander("View Raw Historical Data"):
        st.dataframe(df, use_container_width=True)

else:
    st.warning("Please wait a moment or check your connection if data doesn't load.")

st.info("Data provided by CoinGecko API. No API key required for this tier.")