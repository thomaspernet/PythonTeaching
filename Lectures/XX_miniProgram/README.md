# Argparse Tutorial

This tutorial is intended to be a gentle introduction to argparse, the recommended command-line parsing module in the Python standard library.

## The basics

Let us start with a very simple example which does (almost) nothing:

Create a python file name `prog.py`

```
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
```

run the follwoing command in the CLI

```
python prog.py
python prog.py --help
```

Here is what is happening:

- Running the script without any options results in nothing displayed to stdout. Not so useful.

- The second one starts to display the usefulness of the argparse module. We have done almost nothing, but already we get a nice help message.

- The --help option, which can also be shortened to -h, is the only option we get for free (i.e. no need to specify it). Specifying anything else results in an error. But even then, we do get a useful usage message, also for free.

## Introducing Positional arguments

Create a python file name `prog1.py`

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
```

run the follwoing command in the CLI

```
python prog1.py
python prog1.py --help
```

Here is what’s happening:

We’ve added the add_argument() method, which is what we use to specify which command-line options the program is willing to accept. In this case, I’ve named it echo so that it’s in line with its function.

Calling our program now requires us to specify an option.

The parse_args() method actually returns some data from the options specified, in this case, echo.

The variable is some form of ‘magic’ that argparse performs for free (i.e. no need to specify which variable that value is stored in). You will also notice that its name matches the string argument given to the method, echo.

```
python3 prog1.py foo
```

Note however that, although the help display looks nice and all, it currently is not as helpful as it can be. For example we see that we got echo as a positional argument, but we don’t know what it does, other than by guessing or by reading the source code. So, let’s make it a bit more useful:

Create a python file name `prog2.py`

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)
```

run the follwoing command in the CLI

```
python prog2.py --help
```
Here is what’s happening:

We’ve added the add_argument() method, which is what we use to specify which command-line options the program is willing to accept. In this case, I’ve named it echo so that it’s in line with its function.

Calling our program now requires us to specify an option.

The parse_args() method actually returns some data from the options specified, in this case, echo.

The variable is some form of ‘magic’ that argparse performs for free (i.e. no need to specify which variable that value is stored in). You will also notice that its name matches the string argument given to the method, echo.

Note however that, although the help display looks nice and all, it currently is not as helpful as it can be. For example we see that we got echo as a positional argument, but we don’t know what it does, other than by guessing or by reading the source code. So, let’s make it a bit more useful:

Create a python file name `prog3.py`

```
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.square**2)
```

We specify the type in the `add_argument`

run the follwoing command in the CLI

```
python prog3.py 3
```

## Introducing Optional arguments

So far we have been playing with positional arguments. Let us have a look on how to add optional ones:

Create a python file name `prog4.py`

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

run the follwoing command in the CLI

```
python prog4.py --verbosity 1
python prog4.py
python prog4.py --help
```

Here is what is happening:

The program is written so as to display something when --verbosity is specified and display nothing when not.

To show that the option is actually optional, there is no error when running the program without it. Note that by default, if an optional argument isn’t used, the relevant variable, in this case args.verbosity, is given None as a value, which is the reason it fails the truth test of the if statement.

The help message is a bit different.

When using the --verbosity option, one must also specify some value, any value.

## Combining Positional and Optional arguments

If you are familiar with command line usage, you will notice that I haven’t yet touched on the topic of short versions of the options. It’s quite simple:

Create a python file name `prog5.py`

```
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-s" "--square", type=int,
                    help="display a square of a given number")

parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)
```

Note that we now specify a new keyword, action, and give it the value "store_true". This means that, if the option is specified, assign the value True to args.verbose. Not specifying it implies False.

run the follwoing command in the CLI

```
python prog5.py -s 4 --verbose
python prog5.py
python prog5.py --help
```

## Extra arguments

If you need to pass a list, then use the argument `nargs='+'`

Create a python file name `prog6.py`

```
import argparse
parser = argparse.ArgumentParser()


parser.add_argument('-l','--MyList', nargs='+', help='(Optional) Add list',
 required=False)


args = parser.parse_args()
mylist = args.MyList

print("You input the following list {}".format(mylist))
```

run the follwoing command in the CLI

```
python prog6.py -l 'first' 'second' 'third'
python prog6.py --help
```
