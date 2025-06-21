import network
import time

POWER_SAVE_MODE = 0xa11140

wlan = network.WLAN(network.STA_IF)

def join(ssid, password, retries=10, verbose=True):
    """
    Connect to a WiFi network.

    Parameters:
        ssid (str): The SSID of the WiFi network.
        password (str): The password of the WiFi network.
        retries (int): The number of connection retries before giving up (default: 10).
        verbose (bool): If True, print connection status messages (default: True).
    """
    wlan.active(True)
    wlan.config(pm=POWER_SAVE_MODE)
    wlan.connect(ssid, password)
    
    if verbose:
        print('Connecting to ' + ssid, end=' ')
        
    while retries > 0 and wlan.status() != network.STAT_GOT_IP:
        retries -= 1
        if verbose:
            print('.', end='')
        time.sleep(1)    
        
    if wlan.status() != network.STAT_GOT_IP:
        if verbose:
            print('\nConnection failed. Check ssid and password')
        raise RuntimeError('WLAN connection failed')
    else:
        if verbose:
            print('\nConnected. IP Address = ' + wlan.ifconfig()[0])

