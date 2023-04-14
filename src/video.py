from poetry.console.commands import self

from src.utils import get_name_vide_info, get_info_playlist

class Video:
    def __init__(self, video_id: str):
        self.video_id, self.video_title, self.url_video, self.view_count, self.like_count = get_name_vide_info(video_id)

    def __str__(self):
        return f'{self.video_title}'


class PLVideo():
    def __init__(self, video_id, playlist_id):
        self.video_id, self.video_title, self.url_video, self.view_count, self.like_count, self.playlist_id = get_info_playlist(video_id, playlist_id)

    def __str__(self):
        return f'{self.video_title}'


