Getting started



1) Installing
    pip install SpeechRecognition
    pip install gTTS
    pip install playsound

2) hshshs









3) For the linux terminal 

'''PulseAudio is a general purpose sound server intended to run as a middleware between your applications and your hardware devices,
either using ALSA or OSS. It also offers easy network streaming across local devices using Avahi if enabled. While its main purpose 
is to ease audio configuration, its modular design allows more advanced users to configure the daemon precisely to best suit their
needs.'''

Install PulseAudio sound server
 $ sudo apt-get install pulseaudio

Remove the ALSA packages.

 $ sudo apt-get --purge remove linux-sound-base alsa-base alsa-utils

Reinstall the same packages.

 $ sudo apt-get install linux-sound-base alsa-base alsa-utils

Installing other sound packages.

 $ sudo apt-get install libasound2 alsa-utils alsa.oss

set the sound volume using alsamixer.

 $ alsamixer