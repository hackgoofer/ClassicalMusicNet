from pydub import AudioSegment
import sys
if len(sys.argv) != 0:
    print("error, needs exactly 1 argument (the mp3 location")
else:
    sound = AudioSegment.from_mp3(sys.argv[0])
    sound.export("/output/path", format="wav")
