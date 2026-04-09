#                   LSTM Weather Forecasting

A custom Long Short-Term Memory(LSTM) network that we built from scratch in NumPy to predict the next day's maximum temperature using 
real world Seattle weather data as our base for this program. Every gate, every gradient, and every weight update is implemented by hand. 

**Results Achieved**
| **Model** | **Test MSE** | **Test RMSE** |
| --- | --- | --- |
| Persistence Baseline| 0.00114 | 3.97 C
| Linear Regression | 0.0091 | 3.54 C 
| Custom LSTM | 0.0084 | 3.41 C 

### Summary
Our custom LSTM achieves a 3.7% improvement over linear regression and a 14% improvement over the persistence baseline. 

# Dataset
This project uses the <ins>Seattle Weather Prediction dataset</ins> from [Kaggle](https://www.kaggle.com/datasets/ananthr1/weather-prediction?resource=download)
Download and place 'seattle-weather.csv' in the project root before running. 

### Dataset Features
This dataset contains 1,461 daily records between the years 2012-2015 with the following features: 
| **Feature** | **Description**|
| --- | --- |
| `precipitation` | Daily precipitation (mm)| 
| `temp_max` | Max Temp (C) (**Prediction Target**) |
| `temp_min` | Min Temp (C)| 
| `wind` | Wind Speed (m/s)| 
| `weather` | Categorical Label (sunny, rain, drizzle, fog, snow)| 

# LSTM Components 
**What is an LSTM?**
Long Short-Term Memory(LSTM) is an improved version of the Recurrent Neural Network(RNN). LSTMs are designed to capture long-term dependencies 
in sequential data. It uses memory cells to store data over time which solves the challenge that RNNs faced. 

## LSTM Components in our project
1. Gate Operations: forget, input, candidate cell state, and output gates.
2. Forward Pass: Full sequence across 7 time steps (7 previous days).
3. Backward Pass: Backpropagation Through Time (BPTT) with intermediate states being stored.
4. Adam Optimizer: Adapative moment estimation with bias correction included.
5. Gradient Clipping: Prevents possible exploding gradients during the training phase.
6. Xavier Weight Initialization: Proper scaling of variance for increased stability.

## LSTM Architecture
1. Input Gate: Controls what info is added to the memory cell
2. Forget Gate: Determines what info is removed from the memory cell
3. Output Gate: Controls what info is going to be output from the memory cell

This architecture allows LSTM networks such as ours to selective choose to keep or discard certain information as it flows through our program.
The **Short-Term** memory part of the LSTM is due to hidden states. Memory is updated using the current input, the previous hidden state, 
and the current state of the memory cell. 


## LSTM Applications
1. Language Modeling: Language Modeling, machine translation, and text summarization.
2. **Time Series Forecasting**: Stock price prediction, weather & energy consumption, weather forecasting.
3. Recommender Systems: Suggesting movies, music, and books.
4. Video Analysis: Object detection, activity recognition, action classification.


### Authors
Anthony Salto,
Pedro Garcia,
Sharvesh Suba Palaniraj,
Daisy Nguyen 
