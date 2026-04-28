import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

#Loadin the dataset
df = pd.read_csv('tax_data.csv')

# Defining Features (x) and target (y)
# X is what the AI looks at (Invoice Value)
# y is what the AI needs to predict (calculated ICMS)
X = df[['invoice_value']]
y = df['calculated_icms']

# Spltting: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializing the model
model = LinearRegression()
# Training the model with our 80% data
model.fit(X_train, y_train)

# Making predicion on the test set
prediction = model.predict(X_test)

# Calculating the RMSE (Root Mean Squared Error)
rmse = np.sqrt(mean_absolute_error(y_test, prediction))

# Checking the "Inteligence" Level (Coefficient)
print(f"Model Coefficient (Tax Rate found by AI): {model.coef_[0]:.4f}")
print(f"RMSE: {rmse:.2f}")