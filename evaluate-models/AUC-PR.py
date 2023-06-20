from sklearn.metrics import precision_recall_curve, auc

# Calculate the probabilities of the positive class
y_pred_prob = model.predict(test_data)[:, 1]

# Compute precision-recall curve
precision, recall, thresholds = precision_recall_curve(y_true, y_pred_prob)

# Compute AUC-PR
auc_pr = auc(recall, precision)

print('AUC-PR score:', auc_pr)

# To plot the precision-recall curve
import matplotlib.pyplot as plt

plt.figure()
plt.plot(recall, precision, color='darkorange', lw=2, label='PR curve (area = %0.2f)' % auc_pr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc="lower right")
plt.show()
