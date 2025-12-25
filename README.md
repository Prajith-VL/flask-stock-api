Flask Stock Market Data & Analytics API :

A Flask-based REST API that provides real-time stock market data, company information, historical price data, and analytical insights using the Yahoo Finance API.

This project demonstrates how to build APIs using Flask, integrate external data sources, process financial data, and return JSON responses.

---

 Features

 1. Company Information API  
Fetches:
- Company name  
- Sector  
- Industry  
- Business summary  
- Key officers  

---

 2. Real-Time Market Data API  
Provides:
- Current market price  
- Market state  
- Price change  
- Percentage change  

---

 3. Historical Market Data API (POST)  
Returns daily stock prices (Open, Close, High, Low, Volume) for a specific date range.

---

 4. Analytical Insights API  
Analyzes stock performance:
- Average closing price  
- Volatility  
- Trend (Upward/Downward)

---

 Project Structure

flask_stock_api/
│── app.py # Main Flask application
│── requirements.txt # Python dependencies
│── README.md # Documentation (this file)
│── venv/ # Virtual environment (optional/not uploaded)


---

 Tech Stack

  Flask (Backend Framework)  
  YFinance(Stock market data)  
  Pandas(Data processing)  
  NumPy(Numerical operations)  
  Python 3.9+

---

Installation & Setup

1. Clone the Repository

git clone https://github.com/your-username/flask-stock-api.git
cd flask-stock-api

2️. Create Virtual Environment

Copy code
python -m venv venv

3️. Activate Virtual Environment
Windows:

  venv\Scripts\activate

4️. Install Dependencies

pip install -r requirements.txt

5️. Run the Flask App

python app.py

Server runs at:
  http://127.0.0.1:5000
  
API Endpoints Documentation
1. Company Information
GET
/company-info/<symbol>
  
Example:

arduino
  http://127.0.0.1:5000/company-info/AAPL

2. Real-Time Market Data
GET
/market-data/<symbol>

3. Historical Market Data
POST
/historical-data

Example JSON Body:

json
{
  "symbol": "AAPL",
  "start": "2023-01-01",
  "end": "2023-01-31"
}

 4. Analytical Insights
POST
/analysis

Example JSON Body:

json
{
  "symbol": "AAPL",
  "start": "2023-01-01",
  "end": "2023-01-31"
}

Response Example:

json
{
  "average_price": 135.6,
  "volatility": 4.23,
  "trend": "Upward"
}

Testing the APIs:
Use:
  Postman



Error Handling:
The API returns helpful error messages:

json
{"error": "Invalid company symbol"}

json
{"error": "Missing JSON fields"}

json
{"error": "No historical data found"}

Future Enhancements
  Add advanced technical indicators (RSI, MACD, SMA)
  
  Add authentication using API keys
  
  Add charts/graphs for visualization
  
  Deploy on Render/Railway/AWS
  
  Add caching for faster response times

Conclusion:
  This project successfully demonstrates:
  
  Building APIs using Flask
  
  Working with real-time data
  
  Using POST and GET methods
  
  Performing financial analysis
  
  Returning structured JSON responses

It can serve as:

  A mini-project
  
  A portfolio backend project
  
  A base for financial tools

👤 Author
Prajith VL
GitHub: https://github.com/Prajith-VL
