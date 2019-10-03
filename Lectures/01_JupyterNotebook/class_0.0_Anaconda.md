# How to Download and Install Anaconda Windows and Mac 

In this tutorial, we will explain how to install
**Anaconda**. You will learn how to use Python with Jupyter. Jupyter
is a notebook viewer.

## how to proceed

Here is how to proceed

MacOS User:

-   Install Anaconda

-   Create a `.yml` file to install Tensorflow and dependencies

-   Launch Jupyter Notebook

Windows User:

-   Install Anaconda

-   Create a `.yml` file to install dependencies

-   Use pip to add TensorFlow

-   Launch Jupyter Notebook


## Install Anaconda 

Download [Anaconda](https://www.anaconda.com/download/) version 4.3.1 (for Python 3.6) for the appropriate system.

Anaconda will help you to manage all the libraries required either for
Python or R. 



For a quick setup in Mac:

```shell
#### Step 1: Download Anaconda

curl -O https://repo.continuum.io/archive/Anaconda3-2019.03-MacOSX-x86_64.sh

#### Step 2: Install Anaconda
bash ./Anaconda3-2019.03-MacOSX-x86_64.sh
```



## Extra knowledge

It includes

1.   Locate the path of Anaconda

2.   Set the working directory to Anaconda

**Step 1)** Locate Anaconda

The first step you need to do is to locate the path of Anaconda. You
will create a new conda environment that includes the necessaries
libraries you will use during the tutorials about TensorFlow.

**Windows**

If you are a Windows user, you can use *Anaconda Prompt* and type:

```markdown
C:\>where anaconda
```

![](https://github.com/thomaspernet/Tensorflow/blob/master/tensorflow/7_install-tensorflow_files/image001.png?raw=true)

We are interested to know the name of the folder where Anaconda is
installed because we want to create our new environment inside this
path. For instance, in the picture above, Anaconda is installed in the
`Admin` folder. For you, it can the same, i.e. `Admin` or the user's
name.

In the next, we will set the working directory from `c:\` to
`Anaconda3`.

**MacOS**

for MacOS user, you can use the Terminal and type:

    which anaconda



![](https://github.com/thomaspernet/Tensorflow/blob/master/tensorflow/7_install-tensorflow_files/image002.png?raw=true)

You will need to create a new folder inside Anaconda which will contains
**Ipython**, **Jupyter** and **TensorFlow**. A quick way to install
libraries and software is to write a `yml` file.

**Step 2)** Set working directory

You need to specify the working directory where you want to create the
`yml` file. As said before, it will be located inside Anaconda.

**For MacOS user:**

The Terminal sets the default working directory to **Users/USERNAME**.
As you can see in the figure below, the path of *anaconda3* and the
working directory are identical. In MacOS, the latest folder is shown
before the \$. The Terminal will install all the libraries in this
working directory.

If the path on the text editor does not match the working directory, you
can change it by writing `cd PATH` in the Terminal. PATH is the path you
pasted in the text editor. Don't forget to wrap the PATH with 'PATH'.
This action will change the working directory to PATH.

![](https://github.com/thomaspernet/Tensorflow/blob/master/tensorflow/7_install-tensorflow_files/image003.png?raw=true)

Open your Terminal, and type:

    cd anaconda3

For Windows user (make sure of the folder before Anaconda3):

    cd C:\Users\Admin\Anaconda3

or the path "where anaconda" command gives you

![](https://github.com/thomaspernet/Tensorflow/blob/master/tensorflow/7_install-tensorflow_files/image004.png?raw=true)