import tushare as ts

# print(tushare.__version__)

# s = ts.get_hist_data('600848')
# print(s)

# s = ts.guba_sina()
# print(s)

df = ts.guba_sina(True)
print(df.ix[1]['content']) #第3条消息的内容
