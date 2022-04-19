import librosa
import wave 
#filename = librosa.example('nutcracker')
obj = wave.open(r'G:\anything\minor project\Speech-Dataset-in-Hindi-Language-master\Speech-Dataset-in-Hindi-Language-master\TestingAudio\Aadiksha_6.wav','rb')
y,sr = librosa.load(obj)
tempo,beat_frames=librosa.beat.beat_track(y=y,sr=sr)
print('estimated tempo:{:.2f} beats per minute'.format(tempo))
beat_times=librosa.frames_to_time(beat_frames,sr=sr)
obj.close()