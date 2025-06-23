from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

model = load_model('stock_model.keras')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict_stock():
    stock = request.form['stock']
    start = '2012-01-01'
    end = '2022-12-31'

    data = yf.download(stock, start, end)
    data = data.reset_index()

    # Prepare data for prediction
    data_test = data[['Close']].copy()
    scaler = MinMaxScaler(feature_range=(0,1))
    data_test_scale = scaler.fit_transform(data_test)

    x = []
    for i in range(100, data_test_scale.shape[0]):
        x.append(data_test_scale[i-100:i])
    x = np.array(x)

    # Make predictions
    predictions = model.predict(x)
    predictions = predictions * (1/scaler.scale_)

    # Plot predicted prices
    plt.figure(figsize=(10, 8))
    plt.plot(predictions, 'b', label='Predicted Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.title(f'Predicted Prices for {stock}')
    plt.grid(True)

    # Convert plot to base64 encoding
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    return render_template('result.html', stock=stock, data=data.to_html(), plot_data=plot_data)

if __name__ == '__main__':
    app.run(debug=True)
