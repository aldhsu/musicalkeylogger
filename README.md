# MusicalKeylogger

## WARNING
This is a bad idea. Few things are as low reward and high risk as installing a keylogger just to make terrible music.

## Why?
- Synthesia
    - have you ever tried using a different keyboard layout or setup?
    It's difficult as you brain has to work overtime telling your fingers what to do.
    It leaves little for thinking.
    My hypothesis, is the reverse is also true.
    If we can recruit other senses like we do with muscle memory, it may help us think and make connections we would not have otherwise.
- Give my eyes a rest
    -  It's possible to play an instrument with closed eyes because the aural feedback is enough to highlight errors and correct positioning.
    If I use this long enough a similar effect will occur.

## Why not?
- its a keylogger use at your own risk
- it will play your passwords over your speakers (use headphones or a password manager, not on login though)

## Requirements
- MacOS only ATM
- python 3
- sonic-pi
    - Mac: `brew install sonic-pi`
- python-sonic
    - `pip install python-sonic`
- pyobjc
    - `pip install pyobjc`

## Running
1. Allow your terminal program to control your computer. `System Preferences -> Privacy -> Accessibility -> Tick your chose terminal program`
1. start sonic-pi
1. `python3 main.py`
 NB: for some reason keyboard interrupt doesn't work I haven't figured out why yet I just kill the process

## TODO
- make it sound more pleasing
- remove dependency on sonic-pi

