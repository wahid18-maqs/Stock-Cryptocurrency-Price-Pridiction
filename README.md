# Stock and Cryptocurrency Price Pridiction Web app

## Overview

This project predicts stock and cryptocurrency prices using historical data with an LSTM neural network built with TensorFlow and Keras. Data preprocessing is done with scikit-learn to improve model performance. A Flask web application allows users to input a stock symbol and date range to see predicted and actual prices, based on the past 10 days of data. BytesIO and base64 are used to handle and display matplotlib plots on the web page.

## Screenshots

**1.Home Page:** The main interface where users can input the stock symbol and date range.


![screenshot_2](https://github.com/user-attachments/assets/1dff70f6-5e52-4e07-b97a-7262027699ef)


**2.Prediction Result:** Display of predicted vs actual prices along with the stock data.

![Dashboard](https://github.com/user-attachments/assets/afe3ead4-2fec-43ca-b663-edc82b1bac6f)


**3.Stock Data:** Detailed view of the stock data in a scrollable table.

![google_colab](https://github.com/user-attachments/assets/27aef3a4-2bb1-4670-b4e0-31537d370d60)


**4.Flowchart.**

![Flowchart](https://github.com/user-attachments/assets/d69fbfd4-601e-451a-867a-de7783a2d540)

## Features

- Predicts stock and cryptocurrency prices using an LSTM neural network model.
- Interactive web interface to input stock symbols and date ranges.
- Visual representation of predicted vs actual prices.
- Displays detailed stock data in a tabular format.

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
     
 **8.BytesIO & base64:** 
     For handling image data and encoding plots.    
     
## Requirements
- Python 3.x
- Flask
- Jupyter Notebook
- yfinance
- Keras & TensorFlow
- scikit-learn
- Matplotlib
- Seaborn
- joblib
- BytesIO
- base64
  
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

4. **Web Interface:**

   - Open your web browser and go to http://127.0.0.1:5000/.

   - Enter the stock or cryptocurrency symbol and the date range
   
   - Click "Predict" to see the results.
   
## Usage

**1.Training the Model:**
     Run the Jupyter Notebook to train the LSTM model on historical stock data. Save the model architecture, weights, and scaler for later use in the web application.

**2.Web Application:**
    Use the Flask web application to input stock symbols and date ranges, and view the predicted vs actual prices.
    
 *Note:*
      *This project is for educational purposes only and should not be used for real-life investment decisions.*
      
## Contribution
Follow the standard guidelines for contributions and open issues for feature requests or bug reports.
Feel free to reach out for any questions or suggestions regarding this project.
  

