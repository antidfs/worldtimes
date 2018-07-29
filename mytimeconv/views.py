from django.shortcuts import render
from datetime import datetime
from pytz import timezone

def makeDateStr(tz_dict = {}, date_dict = {}):  #入力したタイムゾーンをフォーマットしたものの文字列を作成
    while tz_dict:
        tz_name, tz_str = tz_dict.popitem()
        try:
            date = datetime.now(timezone(tz_str))
            date_str = "{0:!%Y-%m-%d!%H:%M:%S}".format(date)

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

    return render(request, "mytimeconv/mytimeconv_page.html", date_dict)
# Create your views here.
