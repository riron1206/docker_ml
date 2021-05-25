import numpy as np
import joblib
from palmerpenguins import load_penguins

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.experimental import enable_iterative_imputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score


def train():
    # load dataset
    X, y = load_penguins(return_X_y=True, drop_na=True)

    # # check missing values
    # print(X.isnull().any())  # False
    # print(X.isnull().sum())  # 0

    # split dataset (train:valid = 7:3)
    X_train, X_valid, y_train, y_valid = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # learn
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # predict
    y_pred = model.predict(X_valid)

    # print precision, recall, f1-score, support
    print(classification_report(y_valid, y_pred))
    print("score:", accuracy_score(y_valid, y_pred))

    # save model
    name = "decisiontree_model"
    joblib.dump(model, f"model/{name}.pkl")
    print(f"save model: {name}")


def predict():
    # model name + path
    name = "decisiontree_model"
    saved_filename = (f"model/{name}.pkl")

    # test data
    x_test = np.array([[39.2, 17.7, 181, 3740]])

    # load model
    model = joblib.load(saved_filename)

    # predict
    y_pred = model.predict(x_test)
    print("predict:", y_pred)


if __name__ == "__main__":
    train()
    predict()
