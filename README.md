![silly-gui-icon](https://i.goopics.net/tou3jl.png)

# Flask for desktop

_Build a desktop application with flask._
_All you need is to add the provided file, and Silly gui in your dependencies_



## How it works in a few words

Basicaly, when the app is launched, silly-gui runs the flask server alongside a desktop window and/or the main browser of the user's system.

The user's experience is similar with an 'electron' application, but there, it is python inside instead of JS.

## How to do it

### 1. Code your flask app as usual


### 2. Installation

```
pip install flask-fd
```

### 3. get a converter file
For the simpliest version:

```
flask-fd plop 1
```
or for a more customizable and fancy interface (the best choice)
```
flask-fd plop 2
```
or just running the app in the default web browser
```
flask-fd plop 3
```

The file appear in your current working directory.
Fill the parameters in the given file.

### 4. launch the app

Execute the provided file, you'll see you flask app wrapped in a pretty
Gtk interface

### 5. get an installer (for linux)
This if you want to integrate your app in the system.
The installer uses [Geninstaller](https://github.com/byoso/geninstaller)

```
flask-fd plop installer
```
Fill the parameters in the installer.
