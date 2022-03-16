from flask import Flask
from flask import render_template
import matplotlib.pyplot as plt
import io
import base64
import xgboost
import shap
from matplotlib import pyplot as plt
# train an XGBoost model
app = Flask(__name__)

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


def return_img_stream(img_local_path):
    """
    工具函数:获取本地图片流
    :param img_local_path:文件单张图片的本地绝对路径
    :return: 图片流
    """
    with open(img_local_path, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream).decode()

    return img_stream


@app.route("/")
def hello_world():
    img_path = 'D:/Software/Pycharm/pycharm2019/PyCharm 2019.3.3/Project/RAFA/RAFA/test.png'
    plot_url = return_img_stream(img_path)
    return render_template('log_in.html', plot_url=plot_url, img_path=img_path)

if __name__ == '__main__':
    shap_plot()
    app.debug = True
    app.run()