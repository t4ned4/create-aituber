import obsws_python as obs
import os
from dotenv import load_dotenv


class ConnectOBS:
    def __init__(self) -> None:
        load_dotenv()
        password = os.environ.get('OBS_WS_PASSWORD')
        host = os.environ.get('OBS_WS_HOST')
        port = os.environ.get('OBS_WS_PORT')

        # 設定されていない場合はエラーを表示
        if (password is None or host is None or port is None):
            raise Exception('OBSが未設定です')
        self.ws = obs.ReqClient(host=host, port=port, password=password)

    def set_question(self, text: str):
        self.ws.set_input_settings(
            name='Question',
            settings={'text': text},
            overlay=True)

    def set_answer(self, text: str):
        self.ws.set_input_settings(
            name='Answer',
            settings={'text': text},
            overlay=True
        )

    def set_test(self, text: str):
        self.ws.set_input_settings(
            name='test',
            settings={'text': text},
            overlay=True
        )


# ファイルを直接指定したとき
if __name__ == '__main__':
    test_txt = 'This is a test.'
    ConnectOBS.set_answer(test_txt)
