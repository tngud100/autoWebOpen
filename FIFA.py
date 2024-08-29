import subprocess
import time
import pygetwindow as gw
import os
from shutil import which

# Chrome 경로를 동적으로 검색
def find_chrome_path():
    # 기본적인 경로에서 검색
    potential_paths = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    ]
    
    # 환경 변수에서 검색
    chrome_path = which("chrome")
    if chrome_path:
        return chrome_path
    
    for path in potential_paths:
        if os.path.exists(path):
            return path
    
    raise FileNotFoundError("Chrome executable not found.")

chrome_path = find_chrome_path()

# 첫 번째 창에 열고자 하는 URL 목록
urls_window_1 = [
    'https://피파대낙.com/main.jsp',
]

# 두 번째 창에 열고자 하는 URL 목록
urls_window_2 = [
    'https://피파대낙.com/main.jsp',
]

# 세 번째 창에 열고자 하는 URL 목록
urls_window_3 = [
    'https://피파대낙.com/main.jsp',
]

# 첫 번째 창 열기 (임의 위치, 크기 설정)
command_window_1 = [chrome_path, '--new-window'] + urls_window_1
subprocess.Popen(command_window_1)

# 두 번째 창 열기 (임의 위치, 크기 설정)
command_window_2 = [chrome_path, '--new-window'] + urls_window_2
subprocess.Popen(command_window_2)

# 세 번째 창 열기 (임의 위치, 크기 설정)
command_window_3 = [chrome_path, '--new-window'] + urls_window_3
subprocess.Popen(command_window_3)

# 창이 열리기를 기다림
time.sleep(3)

# 첫 번째 창의 위치와 크기 설정
windows = gw.getWindowsWithTitle('인터넷')  # 창 제목을 정확히 입력
if len(windows) >= 1:
    window_1 = windows[0]
    window_1.resizeTo(560, 1050)
    window_1.moveTo(-7, 0)

# 두 번째 창의 위치와 크기 설정
if len(windows) >= 2:
    window_2 = windows[1]
    window_2.resizeTo(560, 450)
    window_2.moveTo(538, 0)

# 세 번째 창의 위치와 크기 설정
if len(windows) >= 3:
    window_3 = windows[2]
    window_3.resizeTo(560, 610)
    window_3.moveTo(538, 440)
