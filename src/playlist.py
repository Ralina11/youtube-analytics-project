from src.utils import *
import  datetime
class Playlist:

    def __init__(self, playlist_id: str):
        self.title, self.url = get_info_name(playlist_id)

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        # printj(video_response)

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        videos_in_playlist = youtube.playlistItems().list(playlistId=playlist_id,
                                                          part='contentDetails',
                                                          maxResults=50,
                                                          ).execute()
        ''' получить все id видеороликов из плейлиста'''
        best_like = 0
        for video in videos_in_playlist['items']:
            video_id =(video['contentDetails']['videoId'])
            like_count = int(get_name_vide_info(video_id)[4])
            if like_count > best_like:
                best_like = like_count
                url = get_name_vide_info(video_id)[2]
        return url







