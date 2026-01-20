import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open("D:/date.json", "r", encoding="utf-8")
date = json.load(f)
f.close()
date_list = []
for city in date["regions"].values():
    for city_name, city_population_dict in city.items():
        city_population = city_population_dict["population"]
        date_list.append((city_name, city_population))
print(date_list)
result =Map()
result.add("2020年全国各省人口统计地图", date_list, "china")
result.set_global_opts(
    title_opts=TitleOpts(title="全国人口地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 1999, "lable": "1-2000万人", "color": "#9ECAE1"},
            {"min": 2000, "max": 3999, "lable": "2000-4000万人", "color": "#FED976"},
            {"min": 4000, "max": 5999, "lable": "4000-6000万人", "color": "#FD8D3C"},
            {"min": 6000, "max": 7999, "lable": "6000-8000万人", "color": "#E31A1C"},
            {"min": 8000, "max": 9999, "lable": "8000-10000万人", "color": "#BD0026"},
            {"min": 10000, "lable": "10000万人以上", "color": "#800026"},
        ]
    )
)
result.render("全国人口.html")




