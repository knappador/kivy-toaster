kivy-toaster
=============

[Android toasts.](http://developer.android.com/guide/topics/ui/notifiers/toasts.html)  Very simple user feedback when you do something in the background.  Toasts also stay visible if the App pauses, so if you have to pause and move to another activity, you can tell the user what's going on.

#### Supported Option
Long and short toast duration supported.  Oh my.

#### Install
Pre-built application in ```/bin```.  Install with:
```adb install -r /bin/Toaster-0.1-debug-unaligned.apk```

#### Build
Copy the netcheck.sh to a P4A dist then run:
```toast.sh my/path/to/app/```
If it doesn't work, edit toast.sh to configure P4A to build this.  Need PyJNIus in your dist. 

#### Emulation in Kivy for Development
```python ./toast/src/main.py``` This is somewhat of a mock object.  The drawing doesn't look so good, but you have a FOSS license =)

#### Docs
Public API.
