# Draft.vim
Quickly writeup and save drafts for messaging apps in your favorite editor

## Why use Draft.vim
I often write important messages in a vim buffer before I send it.
- The main reason for this is because it is simply faster.
- The second reason is you might want syntax highlighting or auto formating. 
- Also, sometimes you want to write a message without worrying about accidentally sending it.

## Features
- Quickly open a new file, well named
- File contains attributes like date, title, and platform that can be searchable

## Use
- Open vim and run `:Draft <Title>` or `:Draft` to auto name with the date and time
- Draft will open a new file in a specific directory, with a unique name
- The file will be based on a template

## TODO
- Open file in vim buffer
- Have keybind and directory set in plugin
- Have search to reopen and view other drafts
- Make command to run command `:Draft <Title>` and `:Draft`
- Have keybind call function
- Have plugin contain correct api, for new file and search
