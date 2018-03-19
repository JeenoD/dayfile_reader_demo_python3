from Stock import Stock
import struct

# 读取day文件内容
# input:
#     file: 文件所在的完整路径+文件名
# output:
# 	stock_list:	所有的日数据组成的列表
def loadDay(filelocation):
    file = open(filelocation, 'rb')	    # 打开文件
    stock_list = []
    while True:
        line = file.read(32)		# 读取文件中的32个字节大小数据
        if line:
            stock_info = Stock()
            line_p = struct.unpack('i4Ii2I', line)		# 按指定的格式分别对32个字节进行拆分并分装成一日的数据:line_p
            stock_info.setStock(line_p)					
            stock_list.append(stock_info)				# 读取的日数据存放进列表
        else:
            break
    file.close()				# 关闭文件
    print('读取结果如下:')
    for day_stock in stock_list:		# 遍历列表中元素
        print("日期:", day_stock.Date, "开盘价：", day_stock.OpenPrice, "收盘价：", day_stock.ClosePrice,
              "最高价：", day_stock.HighPrice, "最低价：", day_stock.LowPrice, "成交额：", day_stock.Amount,
              "成交量：", day_stock.Volume)
    print('共有', len(stock_list), '天数据')
    return stock_list


if __name__ == "__main__":
    # print("程序主入口")
    loadDay("D:\\zd_zszq\\vipdoc\\sh\\lday\\sh000001.day")  # 读取文件并输出