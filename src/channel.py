from helper.youtube_api_manual import *
from src.utils import *
import json

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id, self.__title, self.__url, self.__subscriber_count, self.__video_count, self.__view_count = get_inf_dict(channel_id)
    @property
    def channel_id(self) -> str:
        return self.__channel_id
    @property
    def title(self) -> str:
        return self.__title

    @property
    def url(self) -> str:
        return self.__url

    @property
    def subscriber_count(self) -> int:
        return int(self.__subscriber_count)

    @property
    def video_count(self) -> str:
        return self.__video_count

    @property
    def view_count(self) -> str:
        return self.__view_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))

    @staticmethod
    def get_service() -> None:
        """возвращающий объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self,json_file):
        data = {}
        data['channel_id'] = self.__channel_id
        data['title'] = self.__title
        data['url'] = self.__url
        data['subscriber_count'] = self.__subscriber_count
        data['video_count'] = self.__video_count
        data['view_count'] = self.__view_count

        with open (json_file,'w') as outfile:
            json.dump(data, outfile)

    def __str__(self):
        return f"{self.__title} ({self.__url})"

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def __ne__(self, other):
        return self.subscriber_count != other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count
    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count








