# Automated Terminal

This is a automated terminal which takes a voice commands from user and perform the task.

## Required packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install pyaudio
pip install SpeechRecognition
pip install gTTS
pip install subprocess
pip install playsound
pip install webbrowser
```

# Voice command
## 0) Choose commands
```bash 
    1) terminal
    2) play music
    3) search web
    4) find location
```
## 1) For Terminal
```bash
1) 'change directory to <directoryName>'
2) 'go back' <-- it is used to one step back to the directory 
3) 'create a directory <dirname>',
4) 'create a file <filename>',
5) 'change permission for directory <dirname>'
6) 'change permission for file <filename>'
7) 'show list directory'
8) 'show me free space',df
9) 'show me use space' ,du commands
10) 'install Python module <moduleName>'
11) 'What is my ip'
12) 'rout <(www.google.com)>'
13) 'scan <(www.facebook.com)>'
14) 'remove file <filename>'
15) 'remove directory <directoryname>'
16) 'install package <packagename>'
17) 'update me'
18) 'upgrade me'
19) 'what is date today'
20) 'show directory', --> this is a "ls " commands

```
## 2) Play Music
```bash
Alex = 'speak the song that you like most...'
User = '...'
```
## 3) Web Searching
```bash
Alex = 'what do you want to search for...'
User = '...'
```
## 4) find location
```bash
Alex = 'Which location do you want to search...'
User = '...'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
