# ToDo List CLI Tools

This is my first attempt at making a CLI tool with Python or any language. I decided to start with a project I did before to stay simple, to be able to easily learn the libraries needed for making CLI tools with Python, and then I could move to harder projects.

---

## Table Of Contents

- [General use](#general-use)
  - [add command](#add-command)
  - [list command](#list-command)
  - [mark-done command](#mark-done-command)
  - [remove command](#remove-command)

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
