"""
author songjie
"""
from app.modules.helper_config import HelperConfig
from app.services.change_file_name import ChangeFileName
from app.services.handle_insomnia_music_service import HandleInsomniaMusicService
from app.services.my_game import MyGame
from app.spider.get_images import GetImages


class Helper(HelperConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def handle_insomnia_music(self):
        return HandleInsomniaMusicService(self.init_db)

    @property
    def get_images(self):
        return GetImages(self.init_db)

    @property
    def change_file_name(self):
        return ChangeFileName(self.init_db)

    @property
    def my_game(self):
        return MyGame()
