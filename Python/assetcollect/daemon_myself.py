#!/usr/bin/python

import subprocess
from daemon import runner
from lockfile import LockTimeout

cmd = "/Users/huamanda/Documents/code/shell-code/ping.sh"

class App():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/ping.pid'
        self.pidfile_timeout = 5
    def start_subprocess(self):
        return subprocess.Popen(cmd, shell=True)
    def run(self):
        p = self.start_subprocess()
        while True:
            res = p.poll()
            if res is not None:
                p = self.start_subprocess()


if __name__ == '__main__':
    app = App()
    daemon_runner = runner.DaemonRunner(app)
    try:
        daemon_runner.do_action()
    except LockTimeout:
        print "Error: couldn't aquire lock"
        print "the daemon must be run already"
        print "pls stop it first"        