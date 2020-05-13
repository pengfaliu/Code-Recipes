#!/bin/env python
# -*- coding: utf-8 -*-
# date: 2019-12-18
# liufapeng

import threading
import time

cancel_tmr = False

def heart_beat():
    print time.strftime('%Y-%m-%d %H:%M:%S')

    if not cancel_tmr:
        threading.Timer(1, heart_beat).start()

if __name__ == "__main__":
    try:
        heart_beat()
        # 15秒后停止定时器
        time.sleep(15) 
        cancel_tmr = True
        
    except KeyboardInterrupt as e:
        print("exit by you ctrl+c")