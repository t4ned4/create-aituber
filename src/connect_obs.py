import obsws_python as obs
import os
from dotenv import load_dotenv


class ConnectOBS:
    def __init__(self) -> None:
        load_dotenv()
        password = os.environ.get('OBS_WS_PASSWORD')
        host = os.environ.get('OBS_WS_HOST')
        port = os.environ.get('OBS_WS_PORT')

        if (password is None or host is None or port is None):
            raise Exception('OBS not configured')
        self.ws = obs.ReqClient(host=host, port=port, password=password)

    def set_test(self, text: str):
        self.ws.set_input_settings(
            name='test',
            settings={'text': text},
            overlay=True
        )


if __name__ == '__main__':
    test_txt = 'This is a test.'
    connext_obs = ConnectOBS()
    connext_obs.set_test(test_txt)
