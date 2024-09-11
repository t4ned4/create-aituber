import os
from dotenv import load_dotenv

from connect_openai import ConnectOpenAI
from connect_obs import ConnectOBS
from connect_voicevox import ConnectVoicevox
from connect_comments import ConnectComments
from play_sound import PlaySound

load_dotenv()


class ExampleSystem:
    def __init__(self) -> None:
        video_id = os.getenv('VIDEO_ID')
        self.youtube_comment_adapter = ConnectComments(video_id)
        self.openai_adapter = ConnectOpenAI()
        self.thread = self.openai_adapter.create_thread()
        self.voice_adapter = ConnectVoicevox()
        self.obs_adapter = ConnectOBS()
        self.play_sound = PlaySound(output_device_name="CABLE Input")
        pass

    def talk_with_comment(self) -> bool:
        print('Loading comments…')
        comment = self.youtube_comment_adapter.get_comment()
        if comment is None:
            print("Comments couldn't be loaded ")
            return False
        response_text = self.openai_adapter.create_chat(self.thread, comment)
        data, rate = self.voice_adapter.get_voice(response_text)
        self.obs_adapter.set_question(comment)
        self.obs_adapter.set_answer(response_text)
        self.play_sound.play_sound(data, rate)
        return True
