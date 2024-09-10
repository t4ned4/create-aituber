from src.connect_voicevox import ConnectVoicevox
from src.play_sound import PlaySound


def test_voicevox():
    input_str = input('VOICEVOXに話させたい言葉を入力してください。\n⇒')
    voicevox_adapter = ConnectVoicevox()
    play_sound = PlaySound("CABLE Input")
    data, rate = voicevox_adapter.get_voice(input_str)
    play_sound.play_sound(data, rate)


# VOCEVOXを起動した上で実行する
if __name__ == '__main__':
    test_voicevox()
