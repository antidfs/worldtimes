from django.shortcuts import render
from datetime import datetime
from pytz import timezone

def addDateStr(tz_name: str, tz_str: str, date_dict = {}):  #入力したタイムゾーンをフォーマットしたものの文字列を作成
    try:
        date = datetime.now(timezone(tz_str))
        date_str = "{0:%Y-%m-%d %H:%M:%S}".format(date)

        date_dict[tz_name] = date_str;
    except:
        print("タイムゾーン名 \"" + tz_str + "\" の追加に失敗しました(addDateStr)")

def makeDateStr(tz_dict = {}, date_dict = {}):  #入力したタイムゾーンをフォーマットしたものの文字列を作成
    while tz_dict:
        tz_name, tz_str = tz_dict.popitem()
        try:
            date = datetime.now(timezone(tz_str))
            date_str = "{0:%Y-%m-%d %H:%M:%S}".format(date)

            date_dict[tz_name] = date_str;
        except:
            print("タイムゾーン名 \"" + tz_str + "\" の追加に失敗しました(addDateStr)")

def appmain(request):
    # write your python code
    date_dict = {}

    tz_name_dict = {"utc": "UTC",
                    "jst": "Asia/Tokyo",
                    "msk": "Europe/Moscow",
                    "eet": "Africa/Cairo",
                    "cet": "Europe/Madrid",
                    "ny":  "America/New_York",
                    "los": "America/Los_Angeles"}

    makeDateStr(tz_name_dict, date_dict)

    """
    date_utc = datetime.now(timezone('UTC'))
    date_utc_str = "{0:%Y-%m-%d %H:%M:%S}".format(date_utc)

    date_jst = datetime.now(timezone('Asia/Tokyo'))
    date_jst_str = "{0:%Y-%m-%d %H:%M:%S}".format(date_jst)

    date_new_york = datetime.now(timezone('America/New_York'))
    date_new_york_str = "{0:%Y-%m-%d %H:%M:%S}".format(date_new_york)

    date_test = datetime.now(timezone('America/Detroit'))
    date_test_str = "{0:%Y-%m-%d %H:%M:%S}".format(date_test)
"""
    return render(request, "mytimeconv/mytimeconv_page.html", date_dict)
# Create your views here.
