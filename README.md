# 🪙 DerivX - Crypto Options Price Calculator

A sophisticated web application for calculating Call and Put option prices for major cryptocurrencies using the Black-Scholes model. Built with Streamlit and powered by real-time data from CoinMarketCap API.

## 🎯 Project Purpose

DerivX is designed to provide traders and financial analysts with accurate options pricing for cryptocurrencies. The application combines the mathematical precision of the Black-Scholes model with real-time cryptocurrency price data, making it an essential tool for cryptocurrency derivatives trading and risk management.

## ✨ Main Features

- **Real-time Crypto Pricing**: Live price feeds from CoinMarketCap API for major cryptocurrencies
- **Black-Scholes Options Pricing**: Accurate Call and Put option price calculations
- **Multi-Crypto Support**: Bitcoin (BTC), Ethereum (ETH), Solana (SOL), Binance Coin (BNB), and XRP
- **Interactive Web Interface**: User-friendly Streamlit-based GUI
- **Customizable Parameters**: Adjustable strike price, maturity, risk-free rate, and volatility
- **Live Price Display**: Real-time spot prices for selected cryptocurrencies
- **Professional UI**: Clean, intuitive design with emoji indicators and clear formatting

## 🚀 Quick Start Guide

### Prerequisites

1. **Python 3.7 or higher**
2. **CoinMarketCap API Key** (get yours at [coinmarketcap.com/api](https://coinmarketcap.com/api/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saumyasanghvi03/DerivX.git
   cd DerivX
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your web browser**
   - The app will automatically open at `http://localhost:8501`
   - Or navigate to the URL shown in your terminal

### Getting Your CoinMarketCap API Key

1. Visit [CoinMarketCap API](https://coinmarketcap.com/api/)
2. Sign up for a free account
3. Navigate to your API dashboard
4. Copy your API key
5. Enter it in the app when prompted

## 📊 Usage Example

Here's how to calculate a Bitcoin call option:

1. **Launch the app**: `streamlit run app.py`
2. **Enter your CoinMarketCap API key** in the password field
3. **Select cryptocurrency**: Choose "Bitcoin (BTC)" from the dropdown
4. **Set option parameters**:
   - Option Type: Call
   - Strike Price: $65,000
   - Days to Maturity: 30
   - Risk-Free Rate: 5.0%
   - Implied Volatility: 70.0%
5. **Click "Calculate Option Price"**
6. **View results**: The app displays the calculated option price

### Live Option Calculation Example

For a Bitcoin call option with:
- **Current BTC Price**: $63,500 (live from API)
- **Strike Price**: $65,000
- **Time to Expiry**: 30 days
- **Risk-Free Rate**: 5%
- **Volatility**: 70%

The app will calculate and display the theoretical option price using the Black-Scholes formula.

## 🔑 API Key Requirement

**Important**: This application requires a valid CoinMarketCap API key to function.

- **Free Tier**: 10,000 calls per month (sufficient for most users)
- **Setup**: Simply paste your API key in the secure input field
- **Security**: API keys are handled securely and not stored

## 🛠️ Tech Stack

### Core Technologies
- **[Streamlit](https://streamlit.io/)**: Web application framework for Python
- **[Python](https://python.org/)**: Primary programming language
- **[CoinMarketCap API](https://coinmarketcap.com/api/)**: Real-time cryptocurrency data

### Libraries & Dependencies
- **NumPy**: Numerical computing and mathematical operations
- **SciPy**: Statistical functions (normal distribution for Black-Scholes)
- **Requests**: HTTP library for API calls
- **Streamlit**: Web app framework and UI components

### Mathematical Model
- **Black-Scholes Formula**: Industry-standard options pricing model
- **Normal Distribution**: Statistical calculations via SciPy

## 📁 Project Structure

```
DerivX/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── LICENSE           # CC0-1.0 License
```

## 🔧 Configuration

### Supported Cryptocurrencies

| Cryptocurrency | Symbol | Supported |
|---------------|--------|-----------|
| Bitcoin       | BTC    | ✅        |
| Ethereum      | ETH    | ✅        |
| Solana        | SOL    | ✅        |
| Binance Coin  | BNB    | ✅        |
| XRP          | XRP    | ✅        |

### Default Parameters
- **Risk-Free Rate**: 5.0% (adjustable)
- **Implied Volatility**: 70.0% (adjustable)
- **Days to Maturity**: 30 (adjustable)

## 🏗️ Development

### Local Development
```bash
# Clone and setup
git clone https://github.com/saumyasanghvi03/DerivX.git
cd DerivX
pip install -r requirements.txt

# Run development server
streamlit run app.py --server.port 8501
```

### Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📄 License

This project is licensed under the CC0-1.0 License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Saumya Sanghvi**
- GitHub: [@saumyasanghvi03](https://github.com/saumyasanghvi03)
- Repository: [DerivX](https://github.com/saumyasanghvi03/DerivX)

## 🙏 Acknowledgments

- **CoinMarketCap** for providing reliable cryptocurrency price data
- **Streamlit** for the excellent web app framework
- **Black-Scholes Model** for the mathematical foundation of options pricing

---

*Built with ❤️ using Streamlit • Powered by Black-Scholes Model • Data by CoinMarketCap API*
