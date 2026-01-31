# Real-Time Crypto Order Book

A FastAPI-based web application that fetches and displays live cryptocurrency order book data using the Binance Depth API.
The project demonstrates backend–frontend data flow, REST API integration, JSON parsing, and auto-refreshing UI updates.

## 📝 Description

A real-time cryptocurrency order book viewer built using **FastAPI**, **JavaScript**, and the **Binance Depth API**.  
This project focuses on understanding API integration, frontend–backend communication, and auto-refreshing live data using a modern Python API framework.

> **The Real-Time Crypto Order Book** is a FastAPI-based web application that displays live bid and ask price levels for cryptocurrency pairs.  
It visualizes market depth in near real time by fetching data every two seconds from the Binance public API.

This project demonstrates:
- Fetching live data from a REST API
- Building API endpoints using FastAPI
- Updating the UI dynamically using JavaScript
- Separating backend API logic from frontend rendering
- Serving static files and templates in FastAPI

Main features include:
- Real-time bid/ask updates
- Retry + timeout error handling
- Clean, beginner-friendly architecture
- Framework migration from Flask → FastAPI

---

## 📛 Badges

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Binance](https://img.shields.io/badge/Binance-Depth%20API-orange)

---

## ✨ Features

- **Live Data Fetching:** Retrieves market depth every 2 seconds.
- **Auto Refresh:** UI updates without page reload.
- **Symbol Selection:** Supports symbols like BTCUSDT and ETHUSDT.
- **Reliable API Calls:** Retry + timeout handling for external API stability.
- **Clean UI:** Bids and asks displayed in separate tables.
- **FastAPI Backend:** Explicit request handling and API-first design.

---

## 🖼️ Screenshots

![Order Book Preview](./images/orderbook-preview.png)

---

## 🚀 Running Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
