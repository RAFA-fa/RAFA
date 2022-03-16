import xgboost as xgb
import pandas as pd
import numpy as np
from itertools import chain
from scripts.Feature_Engineering import DataProcess


class XgbModel(DataProcess):
    def load_model_predict(self, X_test, k_fold, path):
        "ensemble the five XGBoost models by averaging their output probabilities"
        test_pred = np.zeros((X_test.shape[0], k_fold))
        X_test = xgb.DMatrix(X_test)
        for k in range(k_fold):
            model_path_name = path + '\model{}.mdl'.format(k + 1)
            print(model_path_name)
            xgb_model = xgb.Booster(model_file=model_path_name)
            y_test_pred = xgb_model.predict(X_test)
            test_pred[:, k] = y_test_pred
        test_pred = pd.DataFrame(test_pred)
        result_pro = test_pred.mean(axis=1)

        return result_pro

    def predict(self, risk_threshold=0.525):
        model_path = "D:\Software\Pycharm\pycharm2019\PyCharm 2019.3.3\Project\RAFA\RAFA\scripts\model"
        patient = pd.read_csv("D:\Software\Pycharm\pycharm2019\PyCharm 2019.3.3\Project\RAFA\RAFA\dataSets\p100004.psv",
                              sep='|')
        features, labels = super().feature_extraction(patient)

        # predict_pro = self.load_model_predict(features, k_fold = 5, path =  model_path)
        predict_pro = 0.4
        PredictedProbability = np.array(predict_pro)
        PredictedLabel = [0 if i <= risk_threshold else 1 for i in predict_pro]

        return features, PredictedProbability, PredictedLabel[-3:]
