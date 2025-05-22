import os
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize
def start():
    
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Bypassing Face Authentication for testing")
        # Temporarily bypass face authentication
        flag = 1
        eel.hideFaceAuth()
        speak("Face Authentication Successful")
        eel.hideFaceAuthSuccess()
        speak("Hello, Welcome Sir, I am SHASHANK, How can I help you?")
        eel.hideStart()
        playAssistantSound()
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)