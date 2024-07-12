# Stock and Cryptocurrency Price Pridiction Web app

## Overview
The core of the project is an LSTM (Long Short-Term Memory) neural network model, which is trained on past price data to make future price predictions. A Flask web application is built to allow users to input a stock or cryptocurrency symbol and a date range, and then see the predicted versus actual prices.

## Screenshots

1.Home Page: The main interface where users can input the stock symbol and date range.

2.Prediction Result: Display of predicted vs actual prices along with the stock data.

3.Stock Data: Detailed view of the stock data in a scrollable table.

## Technologies Used
**1.Python:** Main programming language.
**2.Jupyter Notebook:** For developing and training the machine learning model.
**3.Flask:** Web framework for the web application.
**4.yfinance:** Library to fetch historical stock data.
**5.Keras & TensorFlow:** Libraries for building and training the LSTM model.
**6.Matplotlib & Seaborn:** Libraries for plotting and visualizations.
**7.HTML & CSS:** For the front-end interface. 

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
##Usage

**1.Training the Model:**
     Run the Jupyter Notebook to train the LSTM model on historical stock data. Save the model architecture, weights, and scaler for later use in the web application.

**2.Web Application:**
    Use the Flask web application to input stock symbols and date ranges, and view the predicted vs actual prices.

##Contribution
  1.Fork the repository.
  2.Create a new branch (git checkout -b feature-branch).
  3.Commit your changes (git commit -m 'Add new feature').
  4.Push to the branch (git push origin feature-branch).
  5.Open the pull request.

Feel free to reach out for any questions or suggestions regarding this project.
  

