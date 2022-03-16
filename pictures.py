from pyecharts import options as opts
from pyecharts.charts import Grid, Gauge, Line, Pie, Bar, Bar3D, Boxplot, Geo, Liquid, Tab
from pyecharts.commons.utils import JsCode
from scripts.XGBmodel import XgbModel
from utils import DataSelect
from pyecharts.faker import Faker
import random

# model = XgbModel()
# patientdata, PredictedProbability, PredictedLabel = model.predict()
# threshold = 0.525
# p_0 = PredictedProbability[-1]
# p_1 = PredictedProbability[-2]
# p_2 = PredictedProbability[-3]
# PredictedProbability_10 = PredictedProbability[-10:]
# PredictedProbability_10 = np.random.random(10)
PredictedProbability_10 = [0.4, 0.41, 0.43, 0.45, 0.43, 0.5, 0.6, 0.54, 0.65, 0.67]


# 风险预测变化图


class DrawPictures():
    # def __init__(self, p_0):
    #     self.p_0 = p_0

    def line(self) -> Line:
        data = DataSelect().get_vital_data()
        HR = []
        SBP = []
        MBP = []
        DBP = []
        RESP = []
        SPO2 = []
        for i in range(len(data)):
            HR.append(float(data[i][2]))
            SBP.append(float(data[i][4]))
            MBP.append(float(data[i][5]))
            DBP.append(float(data[i][6]))
            RESP.append(float(data[i][7]))
            SPO2.append(float(data[i][8]))
        line = (
            Line(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add_xaxis(["{}".format(i) for i in range(10)])
                .add_yaxis(
                series_name="",
                y_axis=HR,
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(
                    title="ICU病人生命体征信息",
                    title_textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=16,
                    )
                ),
                # x轴
                xaxis_opts=opts.AxisOpts(
                    type_="value",
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                    ),
                ),
                # y轴
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                    ),
                ),
            )
        )
        return line

    def sepsis_line(self) -> Line:
        line = (
            Line(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add_xaxis(["{}".format(i) for i in range(10)])
                .add_yaxis(
                series_name="",
                y_axis=[PredictedProbability_10[j] * 100 for j in range(10)],
                is_smooth=True,
                label_opts=opts.LabelOpts(is_show=False),
            )
                .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(
                    title="近十小时脓毒症风险预测变化",
                    title_textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=16,
                    )
                ),
                # x轴
                xaxis_opts=opts.AxisOpts(
                    type_="value",
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3"),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                    ),
                ),
                # y轴
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3"),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                    ),

                ),
            )
        )
        return line

    def creat_pressure_chart(self, P_0) -> Gauge:
        c = (
            Gauge(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add("",
                     [("脓毒症预测概率", P_0)],
                     is_selected=True,
                     min_=['0'],  # 最小值
                     max_=['1'],  # 最大值
                     split_number=5,
                     title_label_opts=opts.GaugeTitleOpts(

                         offset_center=[0, "20%"],
                         color="skyblue",
                         font_size=20,
                         font_style='normal',
                         font_weight='bold',

                     ),
                     axisline_opts=opts.AxisLineOpts(
                         linestyle_opts=opts.LineStyleOpts(
                             color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                         )
                     ),
                     detail_label_opts=opts.GaugeDetailOpts(

                         offset_center=[0, "35%"],
                         color="#36AAFF",
                         font_size=15,
                         font_style='normal',
                         font_weight='bold',

                     )

                     )  # 格式

                .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="当前脓毒症风险预测概率",
                    title_textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=16,
                    )
                ),

            )
        )
        return c

    def vital_line(self):
        x_data = ["{}h".format(i) for i in range(1, 16)]
        data = DataSelect().get_vital_data()
        HR = []
        SBP = []
        MBP = []
        DBP = []
        RESP = []
        SPO2 = []
        for i in range(len(data)):
            HR.append(data[i][2])
            SBP.append(data[i][4])
            MBP.append(data[i][5])
            DBP.append(data[i][6])
            RESP.append(data[i][7])
            SPO2.append(data[i][8])
        # HR：心率、Temp：体温、SBP：心脏收缩压、DBP：心脏舒张压、Resp：呼吸频率、O2Sqt：氧饱和度、MBP：平均血压
        line = (
            Line(init_opts=opts.InitOpts(
                width="900px",
                height="500px",
                bg_color='#FFFFFF', )
            )
                .add_xaxis(xaxis_data=x_data)
                .add_yaxis(
                series_name="HR",
                y_axis=HR,
                yaxis_index=1,  # 右1
                # color='black',  # 标记点颜色
                # 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
                symbol='roundRect',  # 标记的图形
                symbol_size=10,  # 标记的大小
                # 线的颜色
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    color='pink'
                ),
                label_opts=opts.LabelOpts(is_show=False),
            )
                .add_yaxis(
                series_name="SBP",
                y_axis=SBP,
                # color='Pink',  # 标记点颜色
                symbol='triangle',  # 标记的图形
                symbol_size=6,  # 标记的大小
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color='skyBlue'),
                label_opts=opts.LabelOpts(
                    is_show=False,
                    position="top",
                    color='black'
                ),
                # 线的颜色
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    color='skyBlue',
                    # 线的类型。可选：
                    # 'solid', 'dashed', 'dotted'
                    type_='dotted',
                ),
            )
                .add_yaxis(
                series_name="DBP",
                y_axis=DBP,
                areastyle_opts=opts.AreaStyleOpts(opacity=1, color='white'),
                label_opts=opts.LabelOpts(is_show=False),
                # color='red',  # 标记点颜色
                symbol='rect',  # 标记的图形
                symbol_size=6,  # 标记的大小
                # 线的颜色
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    color='skyBlue',
                    type_="dashed"

                ),
            )
                .add_yaxis(
                series_name="MBP",
                y_axis=MBP,
                yaxis_index=2,
                # areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
                # color='#9CEB9F',  # 标记点颜色
                # color='red',
                symbol='diamond',  # 标记的图形
                symbol_size=10,  # 标记的大小
                # 线的颜色
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    color='purple'
                ),
            )
                .add_yaxis(
                series_name="RESP",
                y_axis=RESP,
                yaxis_index=0,
                # areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=False),
                # color='#9CEB9F',  # 标记点颜色
                # symbol='arrow',  # 标记的图形
                symbol_size=10,  # 标记的大小
                # 线的颜色
                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    color='yellow'
                ),
            )

                .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    name="HR|",
                    min_=0,
                    max_=115,
                    position="right",
                    # 坐标轴名称显示位置
                    name_location='start',
                    name_gap=25,
                    offset=-3,

                    # 轴的文本
                    name_textstyle_opts=opts.TextStyleOpts(
                        font_family='Times New Roman',
                        font_size=14,
                        color='Black',
                        font_style='normal',
                        font_weight='bold',
                    ),
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    axislabel_opts=opts.LabelOpts(
                        formatter="{value}",
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=False,
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    axispointer_opts=opts.AxisPointerOpts(
                        is_show=False,
                    ),
                    # splitline_opts=opts.SplitLineOpts(
                    #     is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    # ),
                )
            )
                .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    name="RESP",
                    min_=0,
                    max_=95,
                    position="right",
                    offset=27,
                    # 坐标轴名称显示位置
                    name_location='start',
                    name_gap=25,
                    # 轴的文本
                    name_textstyle_opts=opts.TextStyleOpts(
                        font_family='Times New Roman',
                        font_size=14,
                        color='Black',
                        font_style='normal',
                        font_weight='bold',
                    ),
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    axislabel_opts=opts.LabelOpts(
                        formatter="{value}",
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=False,
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    axispointer_opts=opts.AxisPointerOpts(
                        is_show=False,

                    ),
                    # splitline_opts=opts.SplitLineOpts(
                    #     is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    # ),
                )
            )
                # pyEcharts修改主图颜色后，图例不能随之修改，用该方法解决此问题如果使用了叠加图功能，在add_yaxis()后用set_colors方法设置的颜色将失效。
                # 必须将set_colors放置于叠加方法overlap()之后。
                .set_colors(
                ['pink', 'skyBlue', 'skyBlue', 'purple', 'yellow']
            )

                .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(
                    title="生命体征",

                    title_textstyle_opts=opts.TextStyleOpts(
                        color='skyblue',
                        font_size=16,
                    )
                ),
                # 图例
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    # 图例位置
                    pos_top='12%',
                    textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=14,

                    )
                ),

                tooltip_opts=opts.TooltipOpts(

                    trigger="axis",
                    # is_show_content = True,
                    axis_pointer_type="cross",
                    background_color='pink'
                ),  # 设置横竖显示值得线
                # toolbox_opts=opts.ToolboxOpts(is_show=True),

                # X轴
                xaxis_opts=opts.AxisOpts(
                    type_="category",  # 离散的
                    # boundary_gap=['20%',True],
                    name_textstyle_opts=opts.TextStyleOpts(
                        font_family='Times New Roman',
                        font_size=14,
                        color='red',
                    ),
                    # grid_index=1,
                    # split_number = 5,
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),
                    axispointer_opts=opts.AxisPointerOpts(
                        is_show=True,
                        label=opts.LabelOpts(is_show=False),
                        linestyle_opts=opts.LineStyleOpts(
                            opacity=1
                        )

                    ),

                ),
                # yaxis_opts=opts.AxisOpts(type_="value"),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    min_=0,
                    max_=200,
                    name='SBP',
                    # 坐标轴名称显示位置
                    name_location='start',
                    name_gap=25,

                    name_textstyle_opts=opts.TextStyleOpts(
                        font_family='Times New Roman',
                        font_size=14,
                        font_style='normal',
                        font_weight='bold',

                        color='black'),
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color='#666666', ),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=False,
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                        # position = 'insideBottomLeft'
                    ),
                    axispointer_opts=opts.AxisPointerOpts(
                        is_show=True,
                        label=opts.LabelOpts(is_show=False),  # 去掉轴上的指示器
                        linestyle_opts=opts.LineStyleOpts(
                            opacity=1
                        )
                    ),

                    # # 坐标轴指示器
                    # axispointer_opts=opts.AxisPointerOpts(
                    #     label=opts.LabelOpts(color='#5793f3'),
                    #     linestyle_opts=opts.LineStyleOpts(color="green")
                    # ),

                    # splitline_opts=opts.SplitLineOpts(is_show=True),# 是否显示分割线
                ),

                # axispointer_opts=opts.LabelOpts(
                #     font_size=12,
                #     color='black',
                #     font_family='Times New Roman'
                # ),

            )
            # .set_series_opts(
            #     label_opts=opts.LabelOpts(
            #         font_size=12,
            #         font_family='Times New Roman'
            #     )
            # )
            #     .set_global_opts(
            #     title_opts=opts.TitleOpts(title="堆叠区域图"),
            #     tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
            #     yaxis_opts=opts.AxisOpts(
            #         type_="value",
            #         axistick_opts=opts.AxisTickOpts(is_show=True),
            #         splitline_opts=opts.SplitLineOpts(is_show=True),
            #     ),
            #     xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            # )

        )
        return line

    def Gender_Bar(self):
        bar = (
            Bar(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add_xaxis(["F", "M"])
                .add_yaxis(
                series_name="Gender_number",
                y_axis=[2000, 3000],
                bar_width=35,
                # category_gap=0,
                # gap=0,无效
                color='skyblue',

                label_opts=opts.LabelOpts(
                    position="right",
                    distance=10,
                    is_show=True,
                    color="black",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                    font_family='Times New Roman',
                ),
            )
                .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(
                    title="数据分布",
                    title_textstyle_opts=opts.TextStyleOpts(
                        color='skyblue',
                        font_size=16,
                    )
                ),
                # 图例
                legend_opts=opts.LegendOpts(
                    is_show=True,
                    # 图例位置
                    pos_top='5%',
                    pos_left='23%',
                    inactive_color='skyblue',  # 图例关闭时的颜色
                    textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=14,

                    )
                ),

                # X轴
                xaxis_opts=opts.AxisOpts(
                    # 坐标轴线
                    is_show=False,

                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),

                ),
                yaxis_opts=opts.AxisOpts(
                    # 坐标轴线

                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),

                ),

            )
                .reversal_axis()
        )

        dataselect = DataSelect()
        res = dataselect.get_age_data()
        x_data = []
        y_data = []
        for i in range(len(res)):
            x_data.append(int(res[i][0]))
            y_data.append(res[i][1])

        line = (
            Line(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add_xaxis(x_data)
                .add_yaxis(
                series_name="Age Distribution",
                y_axis=y_data,
                # color='skyblue',  # 标记点颜色
                # symbol='dot',  # 标记的图形
                symbol_size=0,  # 标记的大小

                areastyle_opts=opts.AreaStyleOpts(opacity=0.5, color='#72FF0D'),

                linestyle_opts=opts.LineStyleOpts(
                    width=3,
                    color='#A5FF08',
                    # 线的类型。可选：
                    # 'solid', 'dashed', 'dotted'
                    type_='dotted',
                ),
                # bar_width=2,
                # category_gap=0,
                # gap=0,#无效
                # bar_min_width=2,

                label_opts=opts.LabelOpts(is_show=True),
            )
                .set_colors(
                ['skyblue', 'blue']
            )
                .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(
                    title="Age Distribution",
                    pos_top='43%',
                    pos_left='14%',
                    title_textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=14,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    )
                ),
                # 图例
                legend_opts=opts.LegendOpts(
                    is_show=False,
                    # 图例位置
                    pos_top='42%',
                    pos_left='16%',
                    textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=10,

                    )
                ),
                # x轴
                xaxis_opts=opts.AxisOpts(
                    max_=104,
                    min_=2,

                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666"),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),
                ),
                # y轴
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666"),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),

                ),
            )
            # .reversal_axis()

        )

        sepsis_line = (
            Line(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add_xaxis(["{}".format(i) for i in range(10)])
                .add_yaxis(
                series_name="脓毒症预测曲线",
                color="#675bba",
                # color='black',
                symbol='roundRect',
                symbol_size=7,
                markpoint_opts=opts.MarkPointOpts(
                    label_opts=opts.LabelOpts(position="inside", color="#fff"),
                ),
                y_axis=[PredictedProbability_10[j] * 100 for j in range(10)],
                is_smooth=True,
                label_opts=opts.LabelOpts(
                    is_show=True,
                    color="black",
                    font_size=12,
                    font_style='normal',
                    font_weight='bold',
                    font_family='Times New Roman',

                ),

                #         self.colors = (
                # "#c23531 #2f4554 #61a0a8 #d48265 #749f83 #ca8622 #bda29a #6e7074 "
                # "#546570 #c4ccd3 #f05b72 #ef5b9c #f47920 #905a3d #fab27b #2a5caa "
                # "#444693 #726930 #b2d235 #6d8346 #ac6767 #1d953f #6950a1 #918597"
                # ).split()
                linestyle_opts=opts.LineStyleOpts(
                    width=5,
                    color='#2073A0',
                    # 线的类型。可选：
                    # 'solid', 'dashed', 'dotted'
                    type_='solid', )
            )
                .set_colors(
                ['skyblue', 'blue']
            )
                .set_global_opts(
                # 标题
                title_opts=opts.TitleOpts(
                    title="脓毒症风险预测",
                    pos_top='43%',
                    pos_left='64%',
                    title_textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=14,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',

                    )
                ),
                # # 图例
                legend_opts=opts.LegendOpts(
                    is_show=False,
                    # 图例位置
                    pos_top='45%',
                    pos_left='65%',
                    textstyle_opts=opts.TextStyleOpts(
                        color='Black',
                        font_size=12,

                    )
                ),
                # x轴
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666"),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),
                ),
                # y轴
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    max_=100,
                    # 坐标轴线
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#666666"),
                    ),
                    # 坐标轴刻度
                    axistick_opts=opts.AxisTickOpts(
                        is_show=True,
                        linestyle_opts=opts.LineStyleOpts(color="#666666")
                    ),
                    # 坐标轴标签
                    axislabel_opts=opts.LabelOpts(
                        color="black",
                        font_size=12,
                        font_style='normal',
                        font_weight='bold',
                        font_family='Times New Roman',
                    ),

                ),

            )
        )

        grid = (
            Grid(init_opts=opts.InitOpts(bg_color='#FFFFFF'))
                .add(bar, grid_opts=opts.GridOpts(pos_top="10%", pos_left='5%', width='50%', height='30%'))
                .add(line, grid_opts=opts.GridOpts(pos_top="50%", pos_left='5%', width='40%', height='45%'))
                .add(sepsis_line, grid_opts=opts.GridOpts(pos_top="50%", pos_left='55%', width='40%', height='45%'))
            # .add(gauge, grid_opts=opts.GridOpts(pos_top="50%", pos_left="50", width='30%', height='35%'))

        )

        return grid

    def tab_picture(self):
        c = (
            Bar()
                .add_xaxis(Faker.days_attrs)
                .add_yaxis("商家A", Faker.days_values)
                .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
                datazoom_opts=[opts.DataZoomOpts()],
            )
        )
        d = (
            Line()
                .add_xaxis(Faker.choose())
                .add_yaxis(
                "商家A",
                Faker.values(),
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="min")]),
            )
                .add_yaxis(
                "商家B",
                Faker.values(),
                markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max")]),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="Line-MarkPoint"))
        )
        tab = (Tab()
               .add(c, "bar-example")
               .add(d, "line-example")
               )
        return tab


if __name__ == "__main__":
    drawpoctures = DrawPictures()
    drawpoctures.vital_line()
