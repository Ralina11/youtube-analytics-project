from helper.youtube_api_manual import *
from src.channel import *
from src.video import *



def get_inf_dict(channel_id: str):
    """Возвращает информацию о канале in dictionaries"""
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
    format_dict_info =  channel["items"][0]
    title = format_dict_info["snippet"]["title"]
    url = "https://www.youtube.com/channel/"+ channel_id
    channel_id = format_dict_info["id"]
    subscriberCount = format_dict_info["statistics"]["subscriberCount"]
    videoCount = format_dict_info["statistics"]["videoCount"]
    viewCount = format_dict_info["statistics"]["viewCount"]

    return channel_id, title, url, subscriberCount, videoCount, viewCount



