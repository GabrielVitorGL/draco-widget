import sys
import time
import requests
import ctypes
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')

SW_HIDE = 0

hWnd = kernel32.GetConsoleWindow()
if hWnd:
    user32.ShowWindow(hWnd, SW_HIDE)
    
app = QApplication(sys.argv)

trayIcon = QSystemTrayIcon(QIcon('icon.ico'), parent=app)
trayIcon.setToolTip('Obtendo valor, por favor aguarde')
trayIcon.show()

menu = QMenu()
exitAction = menu.addAction('Fechar')
exitAction.triggered.connect(app.quit)
trayIcon.setContextMenu(menu)

url = 'https://economia.awesomeapi.com.br/json/all/USD-BRL'
url_draco = 'https://api.mir4global.com/wallet/prices/draco/lastest'
loop = 1
while loop == 1:
    try:
        response = requests.get(url).json()
        response_draco = requests.post(url_draco).json()
    except:
        pass
    trayIcon.setToolTip(f"${round(float(response_draco['Data']['USDDracoRate']),2)} / R${round(float(response_draco['Data']['USDDracoRate']) * float(response['USD']['low']),2)}")
    time.sleep(61)
    

sys.exit(app.exec_())
