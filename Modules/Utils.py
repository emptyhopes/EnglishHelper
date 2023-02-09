import termcolor
import gtts
import playsound

from Config import Config

class Utils:

    def Message(message, color):
        return termcolor.colored(message, color)
    
    def Speech(message, language):
        gtts.gTTS(message, lang=language).save(Config.paths["temporary"]["sound"])
        playsound.playsound(Config.paths["temporary"]["sound"])