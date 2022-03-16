import sklearn
import shap
from sklearn.model_selection import train_test_split

# print the JS visualization code to the notebook
# shap.initjs()
# import matplotlib.pyplot as plt
# # train a SVM classifier
# X_train,X_test,Y_train,Y_test = train_test_split(*shap.datasets.boston(), test_size=0.2, random_state=0)
# svm = sklearn.svm.SVC(kernel='rbf', probability=True)
# svm.fit(X_train, Y_train)
#
# # use Kernel SHAP to explain test set predictions
# explainer = shap.KernelExplainer(svm.predict_proba, X_train, link="logit")
# shap_values = explainer.shap_values(X_test, nsamples=100)
#
# # plot the SHAP values for the Setosa output of the first instance
# shap.force_plot(explainer.expected_value[0], shap_values[0][0,:], X_test.iloc[0,:], link="logit",matplotlib=True,)


import xgboost
import shap
from matplotlib import pyplot as plt
# train an XGBoost model
def shap_plot():
    X, y = shap.datasets.boston()
    model = xgboost.XGBRegressor().fit(X, y)
    # explain the model's predictions using SHAP
    # (same syntax works for LightGBM, CatBoost, scikit-learn, transformers, Spark, etc.)
    explainer = shap.Explainer(model)
    shap_values = explainer(X)
    # visualize the first prediction's explanation
    # shap.plots.force(shap_values[0],matplotlib=True)
    a = shap.force_plot(shap_values[0], matplotlib=True, show=True)
    # a = shap.force_plot(shap_values[0])
    # a.matplotlib()
    plt.show()
if __name__ =="__main__":
    shap_plot()