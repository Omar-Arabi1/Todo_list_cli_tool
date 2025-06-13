# ToDo List CLI Tools

This is my first attempt at making a CLI tool with Python or any language. I decided to start with a project I did before to stay simple, to be able to easily learn the libraries needed for making CLI tools with Python, and then I could move to harder projects.

---

## Table Of Contents

- [General use](#general-use)
  - [add command](#add-command)
  - [list command](#list-command)
  - [mark-done command](#mark-done-command)
  - [remove command](#remove-command)
- [Installation](#installation)

---

## General use

There are four commands in total in this program: `add`, `list`, `mark-done`, and `remove`.

---

## add command

The command takes one parameter, which is the task you want to add.
If you want to add multiple commands at once, write them with ', ' as a separation. For example:

To add multiple tasks, write:

`"do dishes, homework, practice coding, learn from this repo :)"`

Make sure you have `" "` outside of your tasks as shown for it to work since the function expects a string.

---

## list command

The command takes no parameters. Just call it, and it will list the tasks one-indexed and show whether it is done or not.

---

## mark-done command

The command takes one parameter, which is the number next to the task. Make sure you are typing them 1-indexed, not zero-indexed. It will mark it as done.

---

## remove command

The command could take two options:

- `--index`
- `--all`

The `--index` takes in the index (one-indexed, not zero-indexed) and its default is one, so it will remove the first task.

The `--all` takes nothing and will remove the entire list, so be careful! There is a confirmation message before it removes anything; if you don't enter anything but 'y', it will not remove it.

## Installation

the inistallation is pretty simple just follow these steps:

1. install the program from [this link](https://github.com/Omar-Arabi1/Todo_list_cli_tool/releases/download/V1.1/install.sh)
2. (VERY IMPORTANT!) move the installed file into the home directory
3. run this command `chmod +x install.sh` to make it executable
4. run this command `sudo ./install.sh`
5. run `source ~/.bashrc`

and that is it what this script does is

- installs the program's zipped folder
- extracts the zipped folder
- moves it to the correct path
- adds the path to the .bashrc to be accessable from everywhere
- and removes the installed zipped folder

this is it you installed it congrats!

**NOTE**: for now the app is only available on Linux if you know how to make it available on other operating systems like mac
          or windows send it in the repo as well as any issues you may encounter

---
please do not ask me to add any more code for this you are free to fork it, but I won't improve it
based on any given code from you because of many reasons which are

- I don't know how to (I am still new to all this)
- I did this to learn how to make cli tools so I may not put more to this project unless later if I see any learning value 

--
thanks for installing the program enjoy!