"""
Project Configuration File
Author: Vaibhav Pandey
"""

# ==========================
# General Configurations
# ==========================

RANDOM_STATE = 42
TEST_SIZE = 0.2
CV = 5
N_ITER = 20
N_JOBS = -1

# ==========================
# File Names
# ==========================

MODEL_FILE_NAME = "model.pkl"
PREPROCESSOR_FILE_NAME = "preprocessor.pkl"
RESULT_FILE_NAME = "model_results.json"

# ==========================
# Target Column
# ==========================

TARGET_COLUMN = "Target"

# ==========================
# Regression Hyperparameters
# ==========================

REGRESSION_PARAMS = {
    "Linear Regression": {},
    "Lasso": {
        "alpha": [0.001, 0.01, 0.1, 1, 10]
    },
    "Ridge": {
        "alpha": [0.001, 0.01, 0.1, 1, 10]
    },
    "K-Neighbors Regressor": {
        "n_neighbors": [3, 5, 7, 9],
        "weights": ["uniform", "distance"]
    },
    "Decision Tree": {
        "criterion": ["squared_error", "friedman_mse"],
        "max_depth": [None, 5, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    },
    "Random Forest": {
        "n_estimators": [100, 200, 300, 500],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"]
    },
    "AdaBoost": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.05, 0.1, 1]
    },
    "XGBoost": {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [3, 5, 7],
        "subsample": [0.8, 1],
        "colsample_bytree": [0.8, 1]
    },
    "CatBoost": {
        "iterations": [200, 300, 500],
        "learning_rate": [0.01, 0.05, 0.1],
        "depth": [4, 6, 8],
        "l2_leaf_reg": [1, 3, 5, 7]
    }

}

# ==========================
# Classification Hyperparameters
# ==========================

CLASSIFICATION_PARAMS = {
    "Logistic Regression": {
        "C": [0.01, 0.1, 1, 10, 100]
    },
    "K-Neighbors Classifier": {
        "n_neighbors": [3, 5, 7, 9],
        "weights": ["uniform", "distance"]
    },
    "Decision Tree": {
        "criterion": ["gini", "entropy", "log_loss"],
        "max_depth": [None, 5, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    },
    "Random Forest": {
        "n_estimators": [100, 200, 300, 500],
        "max_depth": [None, 10, 20, 30],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2"]
    },
    "AdaBoost": {
        "n_estimators": [50, 100, 200],
        "learning_rate": [0.01, 0.05, 0.1, 1]
    },

    "Gradient Boosting": {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [3, 5, 7]
    },
    "SVM": {
        "C": [0.1, 1, 10, 100],
        "kernel": ["linear", "rbf"],
        "gamma": ["scale", "auto"]
    },

    "XGBoost": {
        "n_estimators": [100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1],
        "max_depth": [3, 5, 7],
        "subsample": [0.8, 1],
        "colsample_bytree": [0.8, 1]
    },
    "CatBoost": {
        "iterations": [200, 300, 500],
        "learning_rate": [0.01, 0.05, 0.1],
        "depth": [4, 6, 8],
        "l2_leaf_reg": [1, 3, 5, 7]
    }
}