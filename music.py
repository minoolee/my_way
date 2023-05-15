from pydub import AudioSegment
import os
import shutil
from pydub.playback import play


audio = AudioSegment.from_wav("Sammim_Said_Sharab_Jan_Maida_Maida_-_صمیم_سعید_.mp3")
play(audio)
# boost volume by 6 dB
audio += 6

# repeat the clipe twice
audio *= 2

# 2 2 sec fade in
audio = audio.fade_in(2000)

# audio.export("_assets/maschup.mp3", format="mp3")
# display(Audio("_assets/maschup.mp3"))

def convert_musik(unconverted_files_folder):
    for file in os.scandir(unconverted_files_folder):
        # get all possible alternative formats
        if file.path.endswith(".mkv") or file.path.endswith(".webm") or file.path.endswith("mav") or file.path.endswith(".m4a") or file.path.endswith(".flac"):
            # create new mp3 filename
            converted_file = os.path.splitext(os.path.basename(file.path))[0] + ".mp3"
            print("Converting: ", file)
            # Export the converted file
            AudioSegment.from_file(file.path).export(converted_file, format="mp3")
            # Insert path to the converted files folder
            converted_files_folder = "/home/user/PycharmProjects/my_way/Converted files"
            # Move the converted files
            shutil.move(converted_file, converted_files_folder)

convert_musik(unconverted_files_folder=os.chdir(os.getcwd()))