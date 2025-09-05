import streamlit as st
from scipy.stats import norm
import numpy as np
import requests

# --- Crypto Map
crypto_map = {
    "Bitcoin": {'symbol': 'BTC'},
    "Ethereum": {'symbol': 'ETH'},
    "Solana": {'symbol': 'SOL'},
    "Binance Coin": {'symbol': 'BNB'},
    "XRP": {'symbol': 'XRP'},
}

# --- Black-Scholes Function
def black_scholes(S, K, T, r, sigma, type="call"):
    d1 = (np.log(S / K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price

# --- Fetch crypto price using CoinMarketCap API
def fetch_crypto_price(crypto_label, api_key):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    symbol = crypto_map[crypto_label]['symbol']
    headers = {"X-CMC_PRO_API_KEY": api_key}
    params = {"symbol": symbol}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()
    return data['data'][symbol]['quote']['USD']['price']

# --- Streamlit UI
st.set_page_config(page_title="Crypto Option Price Calculator", layout="centered")
st.title("🪙 Crypto Option Price Calculator")
st.markdown(
    "This app calculates **European Call/Put option prices** for cryptocurrencies "
    "using the Black-Scholes model. "
    "*You must enter your CoinMarketCap API key to continue!*"
)

# API Key input
api_key = st.text_input(
    "Enter your CoinMarketCap API Key to begin",
    type="password"
)

if api_key:
    st.success("API Key accepted. Continue to select crypto and enter option details.")

    crypto_label = st.selectbox(
        "Choose Cryptocurrency",
        options=list(crypto_map.keys()),
        format_func=lambda k: f"{k} ({crypto_map[k]['symbol']})"
    )
    try:
        spot_price = fetch_crypto_price(crypto_label, api_key)
        st.success(f"Live {crypto_label} price: **${spot_price:,.2f}**")
    except Exception as e:
        st.error(f"Could not fetch live price: {e}")
        st.stop()

    # Option parameters
    st.header("Option Parameters")
    option_type = st.selectbox("Option Type", options=["Call", "Put"])
    strike = st.number_input("Strike Price ($)", min_value=0.0, value=spot_price)
    maturity_days = st.number_input("Days to Maturity", min_value=1, value=30)
    T = maturity_days / 365  # Convert to years
    r = st.number_input("Risk-Free Rate (Annual, %)", min_value=0.0, max_value=50.0, value=5.0) / 100
    sigma = st.number_input("Implied Volatility (Annual, %)", min_value=1.0, max_value=300.0, value=70.0) / 100

    if st.button("Calculate Option Price"):
        try:
            price = black_scholes(
                S=spot_price,
                K=strike,
                T=T,
                r=r,
                sigma=sigma,
                type=option_type.lower()
            )
            st.success(
                f"{option_type} Option Price for {crypto_label} ({crypto_map[crypto_label]['symbol']}): "
                f"**${price:,.2f}**"
            )
        except Exception as ex:
            st.error(f"Calculation error: {ex}")

else:
    st.info("Please enter your API key above to begin.")

st.markdown("---\n*Powered by Streamlit · Uses Black-Scholes Model · Data: CoinMarketCap API*")
