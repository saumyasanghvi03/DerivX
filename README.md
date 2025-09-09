# 🐋 DerivX - #CryptoWhale Options Trading Platform 💎

*Where legends are born and positions get REKT* 📈💀

> **"In the volatile seas of crypto derivatives, only the whales survive"** 🌊⚡

DerivX isn't just another options calculator - it's your ticket to the big leagues. Built for degens who think in Greeks and dream in leverage. This beast uses the Black-Scholes model to price crypto options like a pro, pulling live data faster than your portfolio can tank.

## 🚀 Why DerivX Hits Different

### 🔥 Whale-Tier Features
- **🎯 Precision Pricing**: Black-Scholes calculations that would make Wall Street jealous
- **⚡ Lightning-Fast Data**: Live crypto feeds from CoinMarketCap API
- **💰 Multi-Crypto Support**: BTC, ETH, SOL, BNB, XRP - all the coins that matter
- **🎨 Clean Interface**: Streamlit-powered UI that doesn't hurt your eyes during 3am trading sessions
- **⚙️ Full Control**: Adjust strike, maturity, risk-free rate, and vol like the whale you are
- **📊 Real-Time Pricing**: Watch your positions move with the market

### 💎 Built for the Culture
- No BS, just pure mathematical precision
- Mobile-friendly for trading on the toilet 🚽
- Dark mode friendly (because we trade in the shadows)
- Professional enough for your hedge fund interview

## ⚡ Quick Setup (For the Impatient)

### Prerequisites (Don't Skip This)
- Python 3.7+ (if you're still on 2.7, ngmi)
- CoinMarketCap API key ([Get yours here](https://coinmarketcap.com/api/) - it's free, unlike your trading advice)

### Installation (Copy-Paste Friendly)

```bash
# Clone this beauty
git clone https://github.com/saumyasanghvi03/DerivX.git
cd DerivX

# Install dependencies (shouldn't take long)
pip install -r requirements.txt

# Launch the rocket 🚀
streamlit run app.py
```

🎉 **BOOM!** Your app is now live at `http://localhost:8501`

### API Key Setup (30 Seconds Max)
1. Hit up [CoinMarketCap API](https://coinmarketcap.com/api/)
2. Sign up (yes, with your real email)
3. Grab your API key from the dashboard
4. Paste it in the app when prompted
5. Start calculating like a boss

## 📈 Usage Example (BTC Call Option)

Let's price a Bitcoin call option like we're managing a $100M fund:

1. Fire up the app: `streamlit run app.py`
2. Enter your CMC API key (keep it secret, keep it safe)
3. Select **Bitcoin (BTC)** from the dropdown
4. Configure your position:
   - **Option Type**: Call (we're bullish here)
   - **Strike Price**: $65,000 (moon target)
   - **Days to Expiry**: 30 (one month to Valhalla)
   - **Risk-Free Rate**: 5.0% (Fed money)
   - **Implied Volatility**: 70.0% (because crypto)
5. Hit **"Calculate Option Price"**
6. Watch the magic happen ✨

### Live Calculation Example
**Current Setup:**
- BTC Spot: $63,500 (live from API)
- Strike: $65,000
- Time to Expiry: 30 days
- Risk-Free Rate: 5%
- Volatility: 70%

**Result**: Precise option pricing using battle-tested Black-Scholes mathematics

## 🛠️ Technical Stack (For the Nerds)

### Core Technologies
- **🐍 Python**: The language of legends
- **📊 Streamlit**: Web framework that doesn't suck
- **💹 CoinMarketCap API**: Real-time crypto data that matters

### Mathematical Foundation
- **📐 Black-Scholes Model**: The OG options pricing formula
- **📈 NumPy**: Number crunching at light speed
- **🔢 SciPy**: Statistical functions for the Greeks
- **🌐 Requests**: API calls that actually work

## 🏗️ Project Structure (Keep It Simple)

```
DerivX/
├── app.py              # Where the magic happens
├── requirements.txt    # Dependencies (don't touch)
├── README.md          # You are here
└── LICENSE           # Legal stuff
```

## 🎯 Supported Cryptocurrencies

| Crypto | Symbol | Status | Whale Approved |
|--------|--------|--------|-----------------|
| Bitcoin | BTC | ✅ | 🐋 |
| Ethereum | ETH | ✅ | 🐋 |
| Solana | SOL | ✅ | 🚀 |
| Binance Coin | BNB | ✅ | 💛 |
| XRP | XRP | ✅ | 💎 |

## ⚙️ Default Parameters (Sensible Defaults)
- **Risk-Free Rate**: 5.0% (adjustable)
- **Implied Volatility**: 70.0% (because crypto is wild)
- **Days to Maturity**: 30 (monthly options gang)

## 🔧 Development (For Contributors)

```bash
# Setup development environment
git clone https://github.com/saumyasanghvi03/DerivX.git
cd DerivX
pip install -r requirements.txt

# Run development server
streamlit run app.py --server.port 8501

# Start building features that matter
```

### Contributing
Pull requests welcome! Just make sure your code doesn't break existing functionality. We're building tools for serious traders here.

## 📄 License
CC0-1.0 License - Use it, modify it, make millions with it. See [LICENSE](LICENSE) for the legal text.

## 👨‍💻 Author

**Saumya Sanghvi** - The architect behind the magic
- GitHub: [@saumyasanghvi03](https://github.com/saumyasanghvi03)
- Repository: [DerivX](https://github.com/saumyasanghvi03/DerivX)

## 🙏 Acknowledgments

- **CoinMarketCap**: For keeping the price feeds alive
- **Streamlit**: For making web apps that don't require a PhD in frontend
- **Black-Scholes Model**: RIP Myron Scholes, your formula lives on
- **The Crypto Community**: For making volatility our daily bread

---

**Built with 💎 hands and ☕ caffeine**  
*Powered by Black-Scholes Mathematics • Real-Time Data by CoinMarketCap API*

> *"The market can stay irrational longer than you can stay solvent, but with the right tools, you can stay in the game."* 📊⚡

**#CryptoWhale #OptionsTrading #DerivX #ToTheMoon** 🚀🌙
