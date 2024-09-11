from src.connect_voicevox import ConnectVoicevox
from src.play_sound import PlaySound


def test_voicevox():
    sentence = 'Please input the sentense you want VOICEVOX to speak.\n→'
    input_str = input(sentence)
    voicevox_adapter = ConnectVoicevox()
    play_sound = PlaySound("CABLE Input")
    data, rate = voicevox_adapter.get_voice(input_str)
    play_sound.play_sound(data, rate)


# execute after starting VOICEVOX
if __name__ == '__main__':
    test_voicevox()
