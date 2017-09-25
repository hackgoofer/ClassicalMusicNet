from pydub import AudioSegment
import sys
import os

if len(sys.argv) != 2:
    print("error, needs exactly 1 argument (the absolute path to mp3 directory")
    os.exit()

directory_in_str = sys.argv[1]
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp3"): 
        try:
            sound = AudioSegment.from_mp3(os.path.join(directory_in_str,filename))
            # sound = AudioSegment.from_mp3(sys.argv[0])
            sound.export(directory_in_str+"wav/"+filename+".wav", format="wav")
            log = "converted from mp3 to wav and saved: "+str(filename)
        except:
            log = "something went wrong. Maybe bad mp3? "+str(filename)
            
        with open("mp3towav.py.log", "a") as logfile:
            logfile.write(log)
        print(log)

