#  Driver library for Raspbuggy - Sound control via VLC implementation
'''
Created on Apr 24, 2016

@author: bcopy
'''

from drivar.Drivar import Drivar

import time
import logging
import vlc

class SoundVLC(Drivar):
    def __init__(self, soundBasePath=None):
        self.playing = False
        self.currentlyPlaying = None
        self.logger = logging.getLogger(__name__)
        self.player = None
        self.basePath = soundBasePath
        self.currentVolume = 50
        if(self.basePath.endsWith("/")):
            self.basePath=self.basePath[:-1]
        
    
    def sound_playAsync(self, sound):
        try:
            self.currentlyPlaying = sound
            soundFile = sound
            if(self.basePath is not None):
                soundFile = "file://"+self.basePath+"/"+sound
            self.player = vlc.MediaPlayer(soundFile)
            self.player.audio_set_volume(self.currentVolume)
            if(self.player.play()==0):
              self.playing = True
              self.currentlyPlaying = soundFile
        except:
            self.logger.error("Drivar Sound VLC manager: could not play %s : %s",sound,sys.exc_info()[0])
            self.playing = False
            self.currentlyPlaying = None
    
    def sound_stop(self):
        if(self.player is not None):
            self.player.stop()
        self.playing = False
        self.currentlyPlaying = None
    
    def sound_setVolume(self, level):
        self.currentVolume = level
        if(self.player is not None):
            self.player.audio_set_volume(self.currentVolume)
