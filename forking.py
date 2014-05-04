import os
import time


def main():
    pid = os.fork()
    if pid:
        # Parent process
        print('fork pid %s' % pid)
        pid, status = os.waitpid(0, 0)
        print('pid %s exit, status %s' % (pid, status))
    else:
        # Child process.
        # This must never return, hence os._exit()!
        print('Im child %s' % os.getpid())
        time.sleep(3)
        os._exit(1)

if __name__ == '__main__':
    main()
