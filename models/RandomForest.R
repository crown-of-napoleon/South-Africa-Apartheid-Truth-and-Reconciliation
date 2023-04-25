library(randomForest)

# Load and preprocess the data
data <- read.csv("path/to/your/data.csv")
x <- data[, -ncol(data)]
y <- data[, ncol(data)]

# Split the data into training and testing sets
train_index <- sample(1:nrow(data), size = round(0.8 * nrow(data)), replace = FALSE)
x_train <- x[train_index, ]
y_train <- y[train_index]
x_test <- x[-train_index, ]
y_test <- y[-train_index]

# Train the model
model <- randomForest(x = x_train, y = y_train, ntree = 500, mtry = 4)

# Evaluate the model
pred <- predict(model, x_test)
accuracy <- sum(pred == y_test) / length(y_test)
cat("Accuracy:", accuracy, "\n")

# Save the model
saveRDS(model, "south_africa_segregation_rf_model.rds")
