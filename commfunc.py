import math
import time
import json
import datetime
import decimal


# 数据类型转换相关
class DataTypeConvert:
    @staticmethod
    def DBNull2Float(strFloat):
        if strFloat is None or strFloat == '':
            return 0
        else:
            return float(strFloat)
    
    # 字符串整数判断
    @staticmethod
    def is_int(str):
        try:
            int(str)
            return True
        except ValueError:
            return False

    # 字符串正整数判断
    @staticmethod
    def is_positiveint(str):
        try:
            if int(str) > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    # 当前日期、时间格式输出
    @staticmethod
    def d_now_yyyymmdd():
        curr_time = datetime.datetime.now()
        return curr_time.strftime("%Y%m%d")

    @staticmethod
    def d_now_yyyy_mm_dd():
        curr_time = datetime.datetime.now()
        return curr_time.strftime("%Y-%m-%d")

    @staticmethod
    def d_now_yyyy_mm_dd_HH_MM_SS():
        curr_time = datetime.datetime.now()
        return curr_time.strftime("%Y-%m-%d %H:%M:%S")
  

# 坐标转换相关
class geoFunc:
    @staticmethod
    def bdToGaoDe(lon, lat):
        """
        百度坐标转高德坐标
        :param lon:
        :param lat:
        :return:
        """
        _lon = float(str(lon))
        _lat = float(str(lat))
        PI = 3.14159265358979324 * 3000.0 / 180.0
        x = _lon - 0.0065
        y = _lat - 0.006
        z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * PI)
        theta = math.atan2(y, x) - 0.000003 * math.cos(x * PI)
        _lon = z * math.cos(theta)
        _lat = z * math.sin(theta)
        return _lon, _lat


# json 特殊字段编码（数字，日期）
class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


# 判断是否有效日期
def is_valid_date(str_date):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(str_date, "%Y-%m-%d")
        return True
    except Exception:
        return False


# 转字符串，None=‘’
def xstr(s):
    if s is None:
        return ''
    return str(s)
