

from src.utils import *

class Video:
    '''Реализуйте инициализацию реальными данными следующих атрибутов экземпляра класса `Video`:
  - id видео
  - название видео
  - ссылка на видео
  - количество просмотров
  - количество лайков'''
    def __init__(self, video_id: str):
        self.video_id, self.video_title, self.url_video, self.view_count, self.like_count = get_name_vide_info(video_id)

    def __str__(self):
        return f'{self.video_title}'


class PLVideo():
    '''Реализуйте инициализацию реальными данными следующих атрибутов экземпляра класса `PLVideo`:
  - id видео
  - название видео
  - ссылка на видео
  - количество просмотров
  - количество лайков
  - id плейлиста'''
    def __init__(self, video_id, playlist_id):
        self.video_id, self.video_title, self.url_video, self.view_count, self.like_count, self.playlist_id = get_info_playlist(video_id, playlist_id)

    def __str__(self):
        return f'{self.video_title}'


