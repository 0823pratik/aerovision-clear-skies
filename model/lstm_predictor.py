import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

def predict_aqi(series, forecast_hours=12):
    series = np.array(series[-100:])  # Use last 100 points
    X = []
    window = 10
    for i in range(len(series) - window):
        X.append(series[i:i + window])
    X = np.array(X)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Dummy LSTM model (simulate trained)
    model = Sequential()
    model.add(LSTM(32, input_shape=(window, 1)))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, series[window:], epochs=3, verbose=0)

    forecast_input = series[-window:].reshape((1, window, 1))
    forecast = []
    for _ in range(forecast_hours):
        next_val = model.predict(forecast_input, verbose=0)
        forecast.append(next_val[0][0])
        forecast_input = np.roll(forecast_input, -1)
        forecast_input[0, -1, 0] = next_val

    return forecast
