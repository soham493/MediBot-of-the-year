#Setup Text to Speech -TTS model with gTTs (use gTTs(goggle text to specch)  Elevenlabs(generate realistic speech))
import os
from gtts import gTTS 

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audiobj = gTTS( 
        text = input_text,
        lang = language,
        slow = False
    )

    audiobj.save(output_filepath)


input_text = "hello my name is roger how can i help you" 
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")



# setup text to speech-TTS model with Elevenlabs(generate realistic speech))
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

ELEVENLABS_API_KEYS = os.environ.get("ELEVENLABS_API_KEYS")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key = ELEVENLABS_API_KEYS)
    audio = client.generate(
        text = input_text,
        voice = "Roger",
        output_format= "mp3_22050_32", #specific bit rate
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

#use model for text output to voice 

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audiobj = gTTS( 
        text = input_text,
        lang = language,
        slow = False
    )

    audiobj.save(output_filepath)

    # This is for different Operating System
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windowsx
             subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# input_text = "hello my name is roger how can i help you this is the my new version hello sir good morning, have great day" 
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key = ELEVENLABS_API_KEYS)
    audio = client.generate(
        text = input_text,
        voice = "Roger",
        output_format= "mp3_22050_32", #specific bit rate
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)

     # This is for different Operating System
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
           subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")