# Stock and Cryptocurrency Price Pridiction Web app

## Overview

This project is designed to predict stock and cryptocurrency prices based on historical data. It uses a type of neural network called LSTM (Long Short-Term Memory) to learn from past prices and make future predictions. A web application built with Flask lets users enter a stock or cryptocurrency symbol and a date range to see the predicted and actual prices, calculated after analyzing the past 10 days of data

## Screenshots

1.Home Page: The main interface where users can input the stock symbol and date range.


![screenshot_2](https://github.com/user-attachments/assets/1dff70f6-5e52-4e07-b97a-7262027699ef)


2.Prediction Result: Display of predicted vs actual prices along with the stock data.

![Dashboard](https://github.com/user-attachments/assets/afe3ead4-2fec-43ca-b663-edc82b1bac6f)


3.Stock Data: Detailed view of the stock data in a scrollable table.

![google_colab](https://github.com/user-attachments/assets/27aef3a4-2bb1-4670-b4e0-31537d370d60)


4.Flowchart.

![Flowchart](https://github.com/user-attachments/assets/d69fbfd4-601e-451a-867a-de7783a2d540)

## Technologies Used
**1.Python:** 
     Main programming language.
     
**2.Jupyter Notebook:** 
     For developing and training the machine learning model.
     
**3.Flask:**
     Web framework for the web application.
     
**4.yfinance:** 
     Library to fetch historical stock data.
     
**5.Keras & TensorFlow:** 
     Libraries for building and training the LSTM model.
     
**6.Matplotlib & Seaborn:**
     Libraries for plotting and visualizations.
     
**7.HTML & CSS:** 
     For the front-end interface. 

## Setup Instructions
1. **Clone the Repository:**
```bash
git clone https://github.com/wahid18-maqs/Stock-Cryptocurrency-Price-Pridiction.git
```

2. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the Application:**
```bash
pip install -r requirements.txt
```
## Usage

**1.Training the Model:**
     Run the Jupyter Notebook to train the LSTM model on historical stock data. Save the model architecture, weights, and scaler for later use in the web application.

**2.Web Application:**
    Use the Flask web application to input stock symbols and date ranges, and view the predicted vs actual prices.
    
 *Note:*
      This project is for educational purposes only and should not be used for real-life investment decisions.
      
## Contribution
Follow the standard guidelines for contributions and open issues for feature requests or bug reports.
Feel free to reach out for any questions or suggestions regarding this project.
  

