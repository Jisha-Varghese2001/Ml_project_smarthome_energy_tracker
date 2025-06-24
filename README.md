# Smart Home Energy Tracker
📌 Objective:
To develop a web-based application that tracks and predicts household energy consumption based on time-based and appliance-related usage patterns, enabling smarter energy management.

⚙️ How It Works:
🔹 User Interface (Front End) – Streamlit:
The project features a clean and interactive user interface built using Streamlit, allowing users to input relevant details about household conditions:

Temporal Inputs: Time of the day (Hour), Date, Day of Week, Month, Year

Environment Conditions: Temperature, Season

Appliance Usage Indicators: Different types of home appliances like Oven, Air Conditioner, Fridge, Heater etc.

🔹 Data Preprocessing and Transformation:
Once the user provides inputs:

Feature Engineering: Extracted features such as hour from the time and Day, Weekday, Month, Year from Date. Engineered new column named Time Category from hour using a function for better time-based analysis.

Encoding: Appliance Type and Season were encoded using Onehot encoder and Time Category encoded using Ordinal encoder.

Scaling: Inputs are scaled using a pre-trained MinMaxScaler to ensure uniformity.

Model-Ready Input: The transformed input is reshaped and passed to the ML model.

🧠 Machine Learning Model – Back End:
A pre-trained XGBoost Regressor (XGBRegressor) model is used for prediction, stored as a .pkl file.

The model was trained on labeled datasets with Energy Consumption (in kWh) as the target.

Model Output:

Predicts the energy consumption of a smart home in near real-time.

Output is displayed with enhanced styling and color to reflect energy load intensity.

📊 Machine Learning Techniques Used:
Several regression models were evaluated, including:

Linear Regression

KNeighborsRegressor

DecisionTreeRegressor

RandomForestRegressor

XGBRegressor (Best Performer)

🏆 Best Model:
XGBRegressor, selected based on the highest R² score (~0.75) and lowest RMSE during testing.

🌐 Deployment & Usability:
Interactive Web App: Built using Streamlit – requires no technical expertise to operate.

Instant Prediction: As soon as the user enters the data and clicks "Predict", energy consumption is estimated in real time.

Aesthetic UI: Features a soft background image and custom styling for a modern, user-friendly interface.
