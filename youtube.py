import requests, json, datetime
import os
import setting


YT_DEVELOPPER_KEY = os.environ.get('YT_DEVELOPPER_KEY')
YT_CHANNEL_ID = os.environ.get('YT_CHANNEL_ID')

def get_clip_id(channel_id):
    '''
    指定Youtubeチャンネルの最新動画のIDを取得する
    str -> str
    '''
    url = "https://www.googleapis.com/youtube/v3/search" # endpoint

    query = {
        "channelId": channel_id,
        "part": "snippet",
        "key": YT_DEVELOPPER_KEY,
        "order": "date"
    }
    api_res = requests.get(url, params=query)
    # print("status:", api_res.status_code)
    # print("title:", api_res.json()["items"][0]["snippet"]["title"])
    # print("videoId:", api_res.json()["items"][0]["id"]["videoId"])
    clip_id = api_res.json()["items"][0]["id"]["videoId"]
    # clip_url = "https://www.youtube.com/watch?v=" + api_res.json()["items"][0]["id"]["videoId"]

    return clip_id



def search_pic_url(clip_id):
    '''
    指定動画で使われている画像のリンク先URLを取得する
    str -> str
    '''
    url = "https://www.googleapis.com/youtube/v3/videos" # endpoint

    query = {
        "id": clip_id,
        "part": "snippet",
        "key": YT_DEVELOPPER_KEY
    }
    api_res = requests.get(url, params=query)
    # print("status:", api_res.status_code)
    description = api_res.json()["items"][0]["snippet"]["description"]
    desc_lines = description.split("\n")
    pic_link_str = [s for s in desc_lines if "Picture Link" in s][0]
    # print(pic_link_str)
    pic_url = pic_link_str[pic_link_str.find(":") + 2:]
    

    return pic_url
def extract_pic_url(page_url):
    '''
    画像ページから画像URLを抜き出す
    str -> str
    '''
    
    # ページのすべてのimgタグ要素を取得
    # 最大サイズの画像を特定
        # width, height属性
        # その他の方法

if __name__ == "__main__":
    clip_id = get_clip_id(YT_CHANNEL_ID)
    print("clip_id:", clip_id)
    pic_url = search_pic_url(clip_id)
    print("pic_url:", pic_url)

    