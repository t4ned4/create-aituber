import sounddevice as sd

# execute once to check your sound devices
p = f"{__file__}\\.."
with open(f"{p}\\sound_device.txt", 'w', encoding='utf-8') as f:
    f.write(str(sd.query_devices()))
