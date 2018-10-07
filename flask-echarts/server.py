import pymongo
import pandas as pd
from pandas import DataFrame
from pyecharts import Bar, Pie, Page, Map
from pyecharts import configure
from flask import Flask, render_template

app = Flask(__name__)

REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def conn_mongo():
    # 连接数据库
    client = pymongo.MongoClient('127.0.0.1:27017')
    db = client['hupu']
    collections = db['user']

    # 加载数据
    data = DataFrame(list(collections.find()))

    # 删除不需要的字段
    data_new = data.drop(columns=['_id', 'uid', 'name'])
    data_new.round(2)

    client.close()

    return data_new


class DataPreview(object):
    """
    数据分析&可视化
    """
    def __init__(self, data):
        self.df = data
        self.conf = configure(global_theme='chalk')

        # 修改缺失值
        self.df['address'].fillna('无', inplace=True)
        self.df['team'].fillna('无', inplace=True)

    def bar_count_team(self):
        """
        主队数量分布
        :return:
        """
        # 分组
        team_df = self.df.groupby(['team'])['level'].agg(['count'])

        # 删除未填写主队用户
        team_df = team_df.drop(index='无')
        # 排序
        team_df = team_df.sort_values('count', ascending=False)
        team_df.reset_index(inplace=True)

        attr = team_df['team']
        v = team_df['count']

        bar = Bar('用户主队分布')
        bar.add('球队', attr, v, xaxis_rotate=60, is_splitline_show=False, mark_point=['min', 'max'])
        return bar

    def pie_count_gender(self):
        """
        用户性别分布
        :return:
        """
        # 分组
        gender_df = self.df.groupby(['gender'])['level'].agg(['count'])
        gender_df.reset_index(inplace=True)

        attr = gender_df['gender']
        v = gender_df['count']

        pie = Pie('用户性别分布')
        pie.add('', attr, v, is_label_show=True, legend_orient="vertical", legend_pos="80%")
        return pie

    def user_map_count(self):
        """
        国内用户地区分布
        :return:
        """
        # 分组
        user_count_df = self.df.groupby(['address'])['level'].agg(['count'])
        address_df = user_count_df.drop(index=['无', '海外'])
        address_df.reset_index(inplace=True)

        # 数据修改
        for i in address_df.index:
            if address_df.loc[i, 'address'] not in ['黑龙江', '内蒙古']:
                address_df.loc[i, 'address'] = address_df.loc[i, 'address'][0:2]

        # 绘制地图
        value = address_df['count']
        attr = address_df['address']
        _map = Map('国内用户地区分布')
        _map.add("注册人数", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000', is_label_show=True,
                 visual_range=[0, 10000])
        # _map.render()
        return _map

    def user_count_pie(self):
        """
        用户地区分布
        :return:
        """
        # 分组
        user_count_df = self.df.groupby(['address'])['level'].agg(['count'])
        overseas = user_count_df['count']['海外']
        nil = user_count_df['count']['无']
        home = user_count_df['count'].sum() - overseas - nil

        attr = ['国内', '海外', '无']
        value = [home, overseas, nil]
        pie = Pie('用户地区分布')
        pie.add("", attr, value, is_label_show=True)
        return pie

    def user_level_pie(self):
        """
        用户等级区间分布
        :return:
        """
        # 离散化
        binds = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 400]
        df1 = pd.cut(self.df['level'], binds, include_lowest=True, right=False,
                     labels=['0-29级', '30-59级', '60-89级', '90-119级', '120-149级', '150-179级', '180-209级',
                             '210-239级', '240-269级', '270-399级'])

        df2 = df1.value_counts().reset_index()
        # 重设字段名
        df2.columns = ['part', 'count']

        attr = df2['part']
        value = df2['count']
        pie = Pie('用户等级区间分布', title_pos='left')
        pie.add("", attr, value, radius=[40, 60], label_text_color=None, is_label_show=True, legend_orient="vertical",
                legend_pos="80%",)
        return pie

    def grid_pic(self):
        page = Page()
        page.add(self.bar_count_team())
        page.add(self.pie_count_gender())
        page.add(self.user_count_pie())
        page.add(self.user_level_pie())
        page.add(self.user_map_count())
        return page


@app.route('/')
def hello():
    data_preview = DataPreview(conn_mongo())
    page = data_preview.grid_pic()
    return render_template(
        'pyecharts.html',
        myechart=page.render_embed(),
        host=REMOTE_HOST,
        script_list=page.get_js_dependencies()
    )


if __name__ == '__main__':
    app.run()
