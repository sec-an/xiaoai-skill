import requests
from urllib import parse


def search(keyword):
    mp3_urls = []
    try:
        url = f"https://pd.musicapp.migu.cn/MIGUM3.0/v1.0/content/search_all.do"
        params = {
            "text": keyword,
            "pageNo": 1,
            "searchSwitch": "{song:1}"
        }
        res = requests.get(url=url, params=params).json()["songResultData"]["result"]
        for item in res:
            mp3_urls.append(f"https://xiaoai.sec-an.cn/play?s=migu&id={item['copyrightId']}")
    except Exception as e:
        print(e)
    return mp3_urls


def play(id):
    try:
        url = "https://c.musicapp.migu.cn/MIGUM2.0/v1.0/content/resourceinfo.do"
        params = {
            "copyrightId": id,
            "resourceType": 2
        }
        res = requests.get(url=url, params=params).json()["resource"][0]
        detail = res["newRateFormats"][-1] if len(res.get("newRateFormats", "")) != 0 else res["rateFormats"][-1]
        file_url = detail.get("androidUrl", detail.get("url", ""))
        return f"https://freetyst.nf.migu.cn{parse.urlparse(file_url).path}"
    except Exception as e:
        print(e)
        return ""


if __name__ == '__main__':
    # print(search("张学友"))
    print(play("6005663SX43"))