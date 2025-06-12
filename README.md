<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>ToDo List CLI Tools</h1>
        <p>this is my first attempt at making a cli tool with python or any language I decided to start with a project I did before</p>
        <p>to stay simple to be able to easily learn the libraries needed for making cli tools with python and then I could move to </p>
        <p>harder projects</p>
        <hr>
        <h2>Table Of Contents</h2>
        <ul>
            <li><a href="#general-use">General use</a></li>
            <ul>
                <li><a href="#add-command">add command</a></li>
                <li><a href="#list-command">list command</a></li>
                <li><a href="mark-done-command">mark-done command</a></li>
                <li><a href="remove-command">remove command</a></li>
            </ul>
        </ul>
        <hr>
        <h2 id="general-use">General use</h2>
        <p>there are four commands in total in this program which are <code>add, list, mark-done</code> and <code>remove</code></p>
        <hr>
        <h2 id="add-command">add command</h2>
        <div>
            <p>the command takes one parameter which is the task you want to add</p>
            <p>if you want to add multiple commands at once write them with ', ' as a seperation for example</p>
            <p>to add multiple tasks wrtie:</p>
            <p><code>add "do dishes, homework, practice coding, learn from this repo :)"</code></p>
            <p>and make sure you have " " outside of your tasks as shown for it to work since the function expects a string</p>
            <p>and the library by default if it takes multiple ones with commas will be taken as a list not string</p>
        </div>
        <hr>
        <h2 id="list-command">list command</h2>
        <p>the command takes no parameters just call it and it will list the tasks one indexed and shows wether it is done or not</p>
        <hr>
        <h2 id="mark-done-command">mark-done command</h2>
        <div>
            <p>the command takes one parameter which is the number next to the task make sure you are typing them 1 indexed not zero indexed</p>
            <p>it will mark it as done</p>
        </div>
        <h2 id="remove-command">remove command</h2>
        <div>
            <p>the command could take two options</p>
            <ul>
                <li><code>--index</code></li>
                <li><code>--all</code></li>
            </ul>
            <p>the <code>--index</code> takes in the index one indexed not zero indexed and its default is one so it will remove the fist task</p>
            <p>the <code>--all</code> takes nothing and it will remove the entire list so be careful!</p>
            <p>there is a confirmation message before it removes anything if you don't enter anything but 'y' it will not remove it</p>
        </div>
    </body>
</html>