from flask import Flask, request, jsonify
import yfinance as yf
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Stock API is running!"})

@app.route('/company-info/<symbol>', methods=['GET'])
def company_info(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        result = {
            "company_name": info.get("longName"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "business_summary": info.get("longBusinessSummary"),
            "officers": info.get("companyOfficers")
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/market-data/<symbol>', methods=['GET'])
def market_data(symbol):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        data = {
            "current_price": info.get("currentPrice"),
            "market_state": info.get("marketState"),
            "change": info.get("regularMarketChange"),
            "change_percent": info.get("regularMarketChangePercent")
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})
    
@app.route('/historical-data', methods=['POST'])
def historical_data():
    data = request.get_json()

    symbol = data.get("symbol")
    start = data.get("start")
    end = data.get("end")

    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(start=start, end=end)

        result = hist.reset_index().to_dict(orient="records")
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/analysis', methods=['POST'])
def analysis():
    data = request.get_json()

    symbol = data.get("symbol")
    start = data.get("start")
    end = data.get("end")

    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(start=start, end=end)

        closing_prices = hist["Close"]

        avg_price = closing_prices.mean()
        volatility = closing_prices.std()

        trend = "Upward" if closing_prices[-1] > closing_prices[0] else "Downward"

        result = {
            "average_price": float(avg_price),
            "volatility": float(volatility),
            "trend": trend
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
