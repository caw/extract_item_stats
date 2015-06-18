import sys, traceback

try:
    f = flab
except Exception as e:
    print sys.exc_info()[0]
    print sys.exc_info()[1]
    print sys.exc_info()[2].tb_lineno
    traceback.print_tb(sys.exc_info()[2])
