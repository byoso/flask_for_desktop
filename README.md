![silly-gui-icon](https://i.goopics.net/tou3jl.png)

# Flask for desktop

_Build a desktop application with flask._
_All you need is to add the provided file, and Flask for desktop in your dependencies_



## How it works in a few words

Basicaly, when the app is launched, Flask for desktop runs the flask server alongside a desktop window and/or the main browser of the user's system.

The user's experience is similar with an 'electron' application, but there, it is python inside instead of JS.

## How to do it

### 1. Code your flask app as usual


### 2. Installation

```
pip install flask-fd
```

### 3. get the files
If you start your app from scratch:

```sh
flask-fd plop starter
```
If you've already done your app and just want to convert it:

```sh
flask-fd plop converter
```
This one will give you a file that you'll just have to configure following
the steps in the comments.

The file appear in your current working directory.
Fill the parameters in the given file.
