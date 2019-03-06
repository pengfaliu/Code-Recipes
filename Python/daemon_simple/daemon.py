#!/usr/bin/python
#coding:utf8
# daemon 
#  这个脚本是可以正常运行的。
# authoer pengfaliu@163.com
# QQ:569342194

import os
import sys
import time
#----------------------------------------------------------------------
def test(tmpdir):
    while True:
        time.sleep(5)
        f=open(tmpdir+'daemon.log','a')   
        f.write('%s : the is a daemon script by python\n' % 
                time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))   
        f.close()      

def daemon():
    """daemon script of python style
    1. escape from parent process
    2. escape from current session
    3. runing.. 
    """
    try:
        pid = os.fork()
        if pid > 0:
            # Exit first parent 脱离父进程
            sys.exit(0)
    except OSError,e:
        sys.stderr.write( "fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
        sys.exit(1)
    
    # Decouple from parent environment 脱离从父进程继承过来的变量环境
    os.chdir("/")
    os.setsid()
    os.umask(022)
    
    #do second fork 脱离终端会话
    try:
        pid =os.fork()
        if pid > 0:
            #Exit first parent 
            sys.exit(0)
            
    except OSError, e:
        sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))   
        sys.exit(1)
    
    # Redirect the standard I/O file descriptors to /dev/null
    if hasattr(os, "devnull"):
        REDIRECT_TO = os.devnull
    else:
        REDIRECT_TO = "/dev/null"
    fd = os.open(REDIRECT_TO, os.O_RDWR)
    os.dup2(fd, 0)  # standard input (0)
    os.dup2(fd, 1)  # standard output (1)
    os.dup2(fd, 2)  # standard error (2)    
            
    # write the pid file
    pidfile="/tmp/daemon.pid"
    tmpdir="/tmp/tmp/"
    
    # write the pid file
    with open(pidfile, "w") as f:
        f.write("%s\n" % str(os.getpid()))
    
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir, 0o750)   
    test(tmpdir)    
 
            
if __name__ == "__main__":
    if os.getuid() != 0:
        print("You need to be root to run %s." % sys.argv[0])
        sys.exit(-1)    
    else:
        daemon()