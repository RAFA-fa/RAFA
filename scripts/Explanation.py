import numpy as np
import shap
import xgboost as xgb
# from XGBmodel import data_process, feature_extraction
from scripts.Feature_Engineering import DataProcess
import matplotlib.pyplot as plt
import pandas as pd
import base64

dp = DataProcess()

def shap_value(input_data, model_path, k_fold):
    shap.initjs()
    all_shap_values = np.zeros((input_data.shape[0], input_data.shape[1]))
    dat = xgb.DMatrix(input_data)
    for k in range(k_fold):
        file_name = model_path + '\model{}.mdl'.format(k + 1)
        # xgb_model = xgb.Booster(model_file = file_name)
        xgb_model = xgb.Booster(model_file=file_name)
        # 新加一行
        # xgb_model.params["objective"] = "binary"
        explainer = shap.TreeExplainer(xgb_model)
        shap_values = explainer.shap_values(dat)
        all_shap_values = all_shap_values + shap_values

    return explainer, all_shap_values / 5


if __name__ == "__main__":
    model_path = "D:\Software\Pycharm\pycharm2019\PyCharm 2019.3.3\Project\RAFA\RAFA\scripts\model"
    patient = pd.read_csv("D:\Software\Pycharm\pycharm2019\PyCharm 2019.3.3\Project\RAFA\RAFA\dataSets\p100004.psv", sep='|')

    features, labels = dp.feature_extraction(patient)
    explainer, shap_data = shap_value(features, k_fold=5, model_path=model_path)

    shap.summary_plot(shap_data, features, max_display=10, plot_type="bar")
    # shap.summary_plot(shap_data[1], features, max_display=20, plot_type="dot")
    c = shap_data[1]
    d = features[1, :]
    features = pd.DataFrame(features)
    shap.force_plot(explainer.expected_value[1], shap_data[1][0, :], features.iloc[1], matplotlib=True, show=True)
    # shap.force_plot(explainer.expected_value[1], shap_data[1][:1000, :], features.iloc[:1000, :])
    plt.show()
