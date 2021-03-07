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
- Add the command to setup a drafts directory
```vim
let g:drafts_directory = "/path/to/drafts/"
```

#### Optional, create a keybind for the commands

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
- Keybind or function call to copy contents with and without header to file
- Make a convert to pdf for markdown

## Maybe TODO
- Make a draft file type with metadata and parse out the metadata when opened in vim, then use this data to search for notes better and stuff, like have raw data for python to search better with
