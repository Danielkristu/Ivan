import mediapipe as mp  # Import mediapipe
import cv2  # Import opencv
import csv
import os
import numpy as np
import pandas as pd
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score  # Accuracy metrics


def TrainMod():
    df = pd.read_csv(
        "D:\Eagleies\SLAVIK AI Project\slavik\BodyLanguageDecoder\coords.csv"
    )
    X = df.drop("class", axis=1)  # features
    y = df["class"]  # target value

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1234
    )

    pipelines = {
        "lr": make_pipeline(StandardScaler(), LogisticRegression()),
        "rc": make_pipeline(StandardScaler(), RidgeClassifier()),
        "rf": make_pipeline(StandardScaler(), RandomForestClassifier()),
        "gb": make_pipeline(StandardScaler(), GradientBoostingClassifier()),
    }
    fit_models = {}
    for algo, pipeline in pipelines.items():
        model = pipeline.fit(X_train, y_train)
        fit_models[algo] = model

    fit_models["rc"].predict(X_test)

    for algo, model in fit_models.items():
        yhat = model.predict(X_test)
        print(algo, accuracy_score(y_test, yhat))

    fit_models["rf"].predict(X_test)

    with open(
        "D:\Eagleies\SLAVIK AI Project\slavik\BodyLanguageDecoder/body_language.pkl",
        "wb",
    ) as f:
        pickle.dump(fit_models["lr"], f)

    print(y_test)


