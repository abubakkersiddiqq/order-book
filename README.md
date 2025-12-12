#  Real-Time Crypto Order Book

A Flask-based web application that fetches and displays live cryptocurrency order book data using the Binance Depth API.
The project demonstrates backend–frontend data flow, REST API integration, JSON parsing, and auto-refreshing UI updates.

 ## 📝 Description
A real-time cryptocurrency order book viewer built using Flask, JavaScript, and the Binance Depth API.  
This project is designed for beginners who want to understand API integration, frontend–backend communication, and auto-refreshing live data.


  > **The Real-Time Crypto Order Book** is a Flask-based web application that displays live bid and ask price levels for cryptocurrency pairs.  
It helps users visualize market depth in real time by fetching data every two seconds from the Binance public API.
 This project aims to demonstrate :
  > - How to fetch live data from a REST API 
  > - How to update a UI dynamically using JavaScript  
  > - How to structure a Flask backend for API responses  
  > - How to deploy a web app using Render  
 Main features include:
  > - Real-time bid/ask updates 
  > - Retry + timeout error management 
  > - Clean, beginner-friendly architecture

---

  ## 📛 Badges
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-black)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)
![Binance](https://img.shields.io/badge/Binance-Depth%20API-orange)
![Render](https://img.shields.io/badge/Hosted%20on-Render-purple)

  --- 

  ## ✨ Features
- **Live Data Fetching:** Retrieves market depth every 2 seconds.
- **Auto Refresh:** UI updates without reloading the page.
- **Symbol Selection:** Choose BTCUSDT or ETHUSDT.
- **Reliable API Calls:** Retry + timeout implemented for stability.
- **Clean UI:** Bids and asks displayed in separate tables.
- **Deployed Online:** Hosted using Render free tier.
 
---

  ## 🖼️ Screenshots
  Here are some screenshots of the application:
  
  ![Screenshot 1](./images/orderbook-preview.png)

   ---

  ## 🎥 Demo

  Live Demo: https://order-book-dz9z.onrender.com
  
  Note: This may take 20–50 seconds to load on Render free tier due to autosleep.

  --- 

  ## 📜 License
  This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
  
