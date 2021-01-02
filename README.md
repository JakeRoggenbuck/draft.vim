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

## Setup and Config

#### Make a drafts directory
- Add the command to setup a drafts directory `let g:drafts_directory = "/path/to/drafts/"`

### Optional, create a keybind for the commands

#### `NewDraft` Keybind
```vim
nnoremap <Leader>nd :call NewDraft()<CR>
```

#### `ListDrafts` Keybind
```vim
nnoremap <Leader>ld :call ListDrafts()<CR>
```

## Use
- Open vim and run `:call NewDraft()` or `:call NewDraft("<Title>")` to auto name with the date and time
- Draft will open a new file in a specific directory, with a unique name
- The file will be based on a template with stuff like the title and datetime

## Install
#### Vim-Plug
`Plug 'jakeroggenbuck/draft.vim'`

#### Vundle
`Plugin 'jakeroggenbuck/draft.vim'`


## TODO
- Open file in vim buffer
- Have keybind and directory set in plugin
- Have search to reopen and view other drafts
- Make command to run command `:Draft <Title>` and `:Draft`
- Have plugin contain correct api, for new file and search
- Make a search in python
- Make list, let you open listed files to edit
