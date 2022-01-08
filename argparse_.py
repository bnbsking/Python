import argparse, os

parser = argparse.ArgumentParser(description="info. before args", epilog="info. after args", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--foo', help='This is foo arg')
parser.add_argument('-n', '--name', default="bobo", help='This is name arg')
arg = parser.parse_args() # show in cmd / arg.xxx (--xxx only)

print( "Hello {}".format(arg.foo) )
