from AppKit import NSApplication, NSApp
from Foundation import NSObject, NSLog
from Cocoa import NSEvent, NSKeyDownMask
from PyObjCTools import AppHelper
import pdb
from psonic import *

sc = scale(C3, MAJOR, num_octaves = 6)
scale_length = len(sc)
instruments = [PIANO]
instruments_length = len(instruments)

# pdb.set_trace()

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        mask = NSKeyDownMask
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(mask, handler)

def handler(event):
    try:
        keycode = event.keyCode()
        note = sc[keycode % scale_length]
        instrument = instruments[keycode % instruments_length]
        use_synth(instrument)

        play(event.keyCode())
    except KeyboardInterrupt:
        AppHelper.stopEventLoop()

def main():
    app = NSApplication.sharedApplication()
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)
    AppHelper.runEventLoop()

if __name__ == '__main__':
    main()
