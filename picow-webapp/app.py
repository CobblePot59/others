from libs.microdot import Microdot
import libs.wlan_helper as wlan_helper

app = Microdot()
from config import *

wlan_helper.join(SSID, PASSWORD)

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)