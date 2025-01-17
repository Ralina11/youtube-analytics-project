from helper.youtube_api_manual import *
from src.channel import *
from src.video import *
from googleapiclient.errors import HttpError



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
#написать две функции одна для класса видео вторая для класса плейлист
def get_name_vide_info(video_id: str):
    """
  - id видео
  - название видео
  - ссылка на видео
  - количество просмотров
  - количество лайков"""
    video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                        id=video_id
                                        ).execute()
    try:
        video_title: str = video_response['items'][0]['snippet']['title']
        view_count: int = video_response['items'][0]['statistics']['viewCount']
        like_count: int = video_response['items'][0]['statistics']['likeCount']
        url_video: str = "https://youtu.be/" + video_id
    except LookupError:
        return video_id, None, None, None, None

    return video_id, video_title, url_video, view_count, like_count

def get_info_playlist(video_id: str, playlist_id: str) -> tuple or None:

    videos_in_playlist = youtube.playlistItems().list(playlistId=playlist_id,
                                                   part='contentDetails',
                                                   maxResults=50,
                                                   ).execute()
    ''' получить все id видеороликов из плейлиста'''
    video_ids = []
    for video in videos_in_playlist['items']:
        video_ids.append(video['contentDetails']['videoId'])

    for id in video_ids:
        if id == video_id:
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=id
                                                ).execute()

            video_title: str = video_response['items'][0]['snippet']['title']
            view_count: int = video_response['items'][0]['statistics']['viewCount']
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            url_video: str = "https://youtu.be/" + id
            return video_id, video_title, url_video, view_count, like_count, playlist_id

    raise Exception(f"Video with id {video_id} does not exist in playlist {playlist_id}")

def get_info_name(playlist_id: str):
    playlist_info = youtube.playlists().list(id=playlist_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
    title = playlist_info['items'][0]['snippet']['title']
    url = f"https://www.youtube.com/playlist?list={playlist_id}"
    return title, url


