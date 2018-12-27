# Android TV remote
A simple wrapper around ADB to send commands to Android TVs.

Currently it only allows switching input sources (since this functionality is not exposed in the [Philips TV API](https://github.com/eslavnov/pylips/wiki)).

## Prerequisites

You need Android Debug Bridge (standard Android debugging app) installed for this tool to work, since it's just a wrapper around `adb` to send specific key inputs to the TV. Just google `install adb %your_os%` for installation instructions for your OS.

**Make sure `adb` is added to PATH!**

Install on Ubuntu:
```
sudo apt install adb  
```

## Enabling remote debugging on your TV
This has to be enabled to allow `adb` to talk to the TV:
1. On your TV find Android Settings > Device > About > Build and press it 7 times until you see a notification.
2. Go back to Android Settings > Preferences > Developer options 
3. In Developer options enable 'USB debugging'. If you have a separate option for LAN/WI-FI debugging, enable it instead.

## Using the tool

Set the TV's ip address with a `--host` parameter and a desired input source with an `--input` parameter (number from 1 to 6).
The first time you connect to your TV it will display a promt. Answer 'yes' so it does not show up at every request.

**Examples:**

Select HDMI1:

```python android-tv-remote.py --host %tv_ip_address% --input 1```

Select SCART:

```python android-tv-remote.py --host %tv_ip_address% --input 6```
