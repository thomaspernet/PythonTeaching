import argparse
parser = argparse.ArgumentParser()


parser.add_argument('-l','--MyList', nargs='+', help='(Optional) Add list',
 required=False)


args = parser.parse_args()
mylist = args.MyList

print("You input the following list {}".format(mylist))
