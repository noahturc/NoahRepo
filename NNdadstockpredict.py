import pandas as pd
import math
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU, Dropout
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
#loading csv file 
df_raw = pd.read_csv(r'C:\Users\15862\Downloads\StcksML.csv')

#gets the unique symbols from the symbol column in df_raw
df_distinct = df_raw['Symbol'].unique()

'''visualize = pd.DataFrame()
visualize_8 = pd.DataFrame()'''
#creates an empty dictionary
results = {}
for symbol in df_distinct:
    df = df_raw[df_raw['Symbol'] == symbol]
    df.set_index('yyyymmdd', inplace=True)


    total_rows = len(df)
    eighty_percent = int(0.8 * total_rows)
    ten_percent = int(0.1 * total_rows)
    training_data = df.iloc[:eighty_percent]
    validation_data = df.iloc[eighty_percent:eighty_percent + ten_percent]
    testing_data = df.iloc[eighty_percent + ten_percent:]

    target = ['isLastCloseTarget']
    features = ['isHKGreen', 'isDMPlus', 'isRSI']

    X_train = training_data[features]
    y_train = training_data[target]
    X_test = testing_data[features]
    y_test = testing_data[target]
    validation_X = validation_data[features]
    validation_y = validation_data[target]
    validation_data_tuple = (validation_X, validation_y)

  

    # input shape = 3 because there are 3 features
    model = Sequential([
        Dense(12, activation=LeakyReLU(alpha=0.1), input_dim=3),  # Input layer with leaky ReLU activation
        Dense(8, activation=LeakyReLU(alpha=0.1)),  # Hidden layer with leaky ReLU activation
        Dropout(0.2),
        Dense(1, activation='sigmoid')  # Output layer with sigmoid activation for binary classification
    ])

    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train, y_train, epochs=100, batch_size=8, validation_data=validation_data_tuple, callbacks=[early_stopping])


    '''predictions = model.predict(X_test)
    predictions = predictions.flatten()
    y_test = y_test.values.flatten()

    if len(predictions) == 8 and len(y_test) == 8:
        visualize_8['Prediction_' + symbol] = predictions
        visualize_8['Actual_' + symbol] = y_test
    else:
        visualize['Prediction_' + symbol] = predictions
        visualize['Actual_' + symbol] = y_test'''

    #model.summary()


    loss, accuracy = model.evaluate(X_test, y_test)
    #print(symbol, "Accuracy:", accuracy)
    results[symbol] = accuracy
print(results)

'''print(visualize)
print(visualize_8)'''

'''plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()'''