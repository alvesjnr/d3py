from datetime import datetime
import d3py
import pandas

dates = [
    datetime(2006, 1, 26, 11, 17, 32),
    datetime(2006, 2, 22, 1, 37, 33),
    datetime(2006, 3, 16, 1, 30, 11),
    datetime(2006, 3, 26, 19, 16, 43),
    datetime(2006, 4, 10, 20, 49, 38),
    datetime(2006, 4, 25, 22, 5, 23),
    datetime(2006, 5, 7, 3, 8, 9)
]

values = [
    0,
    3.1622776601683795,
    6.9039350469423209,
    9.9039350469423209,
    12.732362171688511,
    16.196463786826264,
    20.886879546649695
]

df = pandas.DataFrame({
    'x' : dates,
    'y' : values
})

with d3py.Figure(df, 'd3py_line', width=600, height=200) as fig:
    fig += d3py.geoms.Line('x', 'y')
    fig += d3py.geoms.Point('x', 'y', fill='BlueViolet')
    fig += d3py.xAxis('x')
    fig += d3py.yAxis('y')
    fig.show()