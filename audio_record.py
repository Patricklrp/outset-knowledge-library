import pyaudio
import wave

# 配置录音参数
FORMAT = pyaudio.paInt16
CHANNELS = 1  # 单声道
RATE = 16000  # 采样率（每秒采样点数）
CHUNK = 1024  # 每次读取的音频帧数
RECORD_SECONDS = 15  # 录制时长（秒）



def record_audio(output_file = "output.pcm"):
    
    # 创建PyAudio对象
    print("flag")
    audio = pyaudio.PyAudio()

    #打开麦克风流
    stream = audio.open(format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []
    try:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
         # 读取音频数据
         data = stream.read(CHUNK)
         frames.append(data)
    except KeyboardInterrupt:
        print("Recording stopped.")

    # 关闭流和PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 将录制的音频数据写入WAV文件
    with wave.open(output_file, 'wb') as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(b''.join(frames))

    # print(f"WAV file saved as {output_file}")