import pandas as pd

# Assuming `x_test` is your test data and `model` is your trained model
predictions = model.predict(x_test)

# Convert predictions to a DataFrame
predictions_df = pd.DataFrame(predictions)

# Save to CSV
predictions_df.to_csv('predictions.csv', index=False)
