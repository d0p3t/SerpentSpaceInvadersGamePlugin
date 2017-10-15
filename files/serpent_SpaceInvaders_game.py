from serpent.game import Game

from .api.api import SpaceInvadersAPI

from serpent.utilities import Singleton




class SerpentSpaceInvadersGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "executable"

        kwargs["window_name"] = "Snes9X v1.53 for Windows"



        kwargs["executable_path"] = "D:\\\\SNES\\\\snes9x.exe"



        super().__init__(**kwargs)

        self.api_class = SpaceInvadersAPI
        self.api_instance = None

        self.frame_transformation_pipeline_string = "RESIZE:100x100|GRAYSCALE"

        self.frame_width = 100
        self.frame_height = 100
        self.frame_channels = 0

    @property
    def screen_regions(self):
        regions = {
            "GAME_CURRENT_HEALTH": (408, 48, 427, 143),
            "GAME_CURRENT_SCORE": (33, 80, 50, 140)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
