import subprocess
import sys
import matplotlib

if __name__ == "__main__":
    address = "cadencelm.uvm.edu"
    mtrprocess = subprocess.Popen(["mtr","-l",address],stdout=subprocess.PIPE)
    print("test")
    while True:
        l = mtrprocess.stdout.readline()
        mtrprocess.stdout.flush()
        if l: print(l)
