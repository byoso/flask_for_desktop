![silly-gui-icon](https://i.goopics.net/tou3jl.png)
# WIP


# Silly Gui

If you are a web developper, then you are a desktop developper too.

Silly Gui allows to simply shell any web application to convert it
into a desktop application.


# Why should I use it instead of PyGObject or tkinter or else ?

Simply to save some time if you already know flask or django.


# How it works

Basicaly, when the app is launched, silly-gui runs the server needed
by your web application localy and hidden, you can then show your app
in a desktop window and/or the main browser of the user's system.

The user's experience is similar with an 'electron' application, but there
it is python inside instead of JS.

# Developpment notes

## Flask
Works fine as it is

## Django
Still experimental.
Works, but it is prudent to include a virtual environment with all dependencies
included.
For some reason the free port detection doesn't work.
(Why ? if you know the answer, i'd be glad to know and fix it)
