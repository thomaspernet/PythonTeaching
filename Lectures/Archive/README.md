# How to Download and Install Anaconda Windows

In this tutorial, we will explain how to install
**Anaconda**. You will learn how to use Python with Jupyter. Jupyter
is a notebook viewer.

## how to proceed

Here is how to proceed

Windows User:

-   Install Anaconda

-   Launch Jupyter Notebook

## Install Anaconda

Download [Anaconda](https://www.anaconda.com/download/) version 4.3.1 (for Python 3.7) for the appropriate system.

Anaconda will help you to manage all the libraries required either for
Python or R.


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

We are interested to know the name of the folder where Anaconda is
installed because we want to create our new environment inside this
path. For instance, in the picture above, Anaconda is installed in the
`Admin` folder. For you, it can the same, i.e. `Admin` or the user's
name.

In the next, we will set the working directory from `c:\` to
`Anaconda3`.

**Step 2)** Set working directory

You need to specify the working directory where you want to create the
`yml` file. As said before, it will be located inside Anaconda.

For Windows user (make sure of the folder before Anaconda3):

    cd C:\Users\AXXXXXX\Anaconda3

or the path "where anaconda" command gives you

## Download Package

Go to environment variable from Windows search box. From here, you can add the paths you need for Anaconda to work properly. The simplest way to add libraries to conda is by adding this proxy in two variables named `http_proxy` and `https_proxy`:

```
http://USERACCOUNT:PASSWORD@proxy-sgt.si.socgen:8080
```

To be sure Anaconda works seamlessly with the command line, you should add few other variable in the **Path**.

Open the **Path** variable and add the following (change `USERNAME`):

```
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Scripts
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Library\bin
```

If you installed Anaconda in a different folder, use `where conda` to know the path.

You should reboot the machine for the path to be effective.

### From Anaconda

There are two ways to install a package. The first one is through Anadonca while the second way is with Pip. Choose Conda by default, if the library is not available in Conda, then go for pip.

To install a package with Anaconda, you first need to override the current settings. Open Anaconda prompt and paste the following. 

```
conda config --show
conda config --set remote_read_timeout_secs 1000
conda config --set ssl_verify false
```

Try now to install a library.

```
conda install -c plotly plotly
```

### From Pip

The second way to download a library is with `pip`. It's straighforward to download a package with `pip`. Go to Google, type the name of the library preceded by `pip`. For instance, if you want to download `plotly`, go to Google and type down `pip plotly`. Goole will point you to this website https://pypi.org/project/plotly/. Go to Anaconda Prompt and paste `pip install plotly` with the following arguments:

```
--trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
```

the full code is:

```
pip install plotly --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
```

to upgrade a package with pip, use `--upgrade`:

```
pip install --upgrade plotly --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org
```
