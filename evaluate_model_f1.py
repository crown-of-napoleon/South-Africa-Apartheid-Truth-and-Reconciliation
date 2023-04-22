from sklearn.metrics import f1_score

# Load the test data and preprocess it
test_data, test_labels = load_data('test_data_path')
test_data = preprocess_data(test_data)

# Make predictions on the test data
y_pred = model.predict(test_data)

# Convert the predicted probabilities to class labels
y_pred = np.argmax(y_pred, axis=1)

# Convert the true labels to class labels
y_true = np.argmax(test_labels, axis=1)

# Calculate the F1 score
f1 = f1_score(y_true, y_pred, average='weighted')

print('F1 score:', f1)
