import argparse

parser = argparse.ArgumentParser(description="Basic direct input.")
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help="User's name")
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help="sum the integers (default: find the max)")

args = parser.parse_args()
print args.accumulate(args.integers)
