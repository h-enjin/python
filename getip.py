# coding: utf-8
import json
import urllib2

# JSONIPからjson取得
data = urllib2.urlopen('http://jsonip.com/')
# jsonデータを読み込んだファイルオブジェクトからPythonデータを作成
jsonip = json.load(data)
# ファイルを閉じる
data.close()

# jsonデータから抽出
print(jsonip["ip"])