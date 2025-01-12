# Draft.vim
[![Vim](https://img.shields.io/badge/Vim-%2311AB00.svg?logo=vim&logoColor=white&style=for-the-badge)](https://vimawesome.com/plugin/draft-vim)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/JakeRoggenbuck?tab=repositories&q=&type=&language=python&sort=stargazers)
[![Version](https://img.shields.io/badge/v0.8-blue?style=for-the-badge)](#)
[![Python](https://img.shields.io/github/actions/workflow/status/jakeroggenbuck/draft.vim/python.yml?branch=main&style=for-the-badge)](https://github.com/JakeRoggenbuck/draft.vim/actions)

:pencil: Quickly write up and save drafts for messaging apps in your favorite editor [vimawesome.com/plugin/draft-vim](https://vimawesome.com/plugin/draft-vim)

## Why use Draft.vim
I often write important messages in a vim buffer before I send it.

- The main reason for this is because it is simply faster.
- The second reason is you might want syntax highlighting or auto formatting. 
- Also, sometimes you want to write a message without worrying about accidentally sending it.

## Requirements
- Pandoc
- wkhtmltopdf
- Dragon (https://github.com/mwh/dragon)

## Features
- Quickly open a new, well named file in a consistent directory
- Each file automatically contains attributes like the date and title that can be searchable

## Setup and Config

#### Make a drafts directory
```vim
" Add the command to setup a drafts directory
let g:drafts_directory = "/path/to/drafts/"
```

## Optional, create a keybind for the commands

#### `NewDraft` Keybind
```vim
nnoremap <Leader>nd :call NewDraft()<CR>
```

#### `ListDrafts` Keybind
```vim
nnoremap <Leader>ld :call ListDrafts()<CR>
```

#### `OpenDrafts` Keybind
```vim
nnoremap <Leader>z :call OpenDrafts()<CR>
```

## Usage


### Commands

| Command                | Description                                     |
|------------------------|-------------------------------------------------|
| Draft                  | Open a blanck new draft                         |
| Draft `"title"`        | Open a draft with a title                       |
| DraftExt `"extension"` | Change the file extension of a draft            |
| Drafts                 | Open the draft directory in a buffer            |
| DraftCopy              | Copy the contents of the draft to the clipboard |
| DraftSearch            | Search through drafts by keyword                |

### More info

- New draft: run `:Draft` or `:Draft "<Title>"` to auto name with the date and time
- Edit the file extension: run `:DraftExt .md` to change the file to markdown
- Open the drafts directory: run `:Drafts`
- Copy the contents of the current draft `:DraftCopy`
- Draft will open a new file in a specific directory, with a unique name
- The file will be based on a template with stuff like the title and datetime

## Install
#### Vim-Plug
```vim
Plug 'jakeroggenbuck/draft.vim'
```

#### Vundle
```vim
Plugin 'jakeroggenbuck/draft.vim'
```

## Changelog

#### 0.1 draft.vim - not fully functional, just a concept

- Open a new draft with a name
- List the draft but no reopening them

#### 0.2 draft.vim - first complete version

- Add `OpenDrafts()`
- Add new command aliases `Draft`, `DraftExt`

#### 0.3 draft.vim - more features

- Add `ClipDraft()` for `DraftCopy`
- Add `Buffer reload for DraftExt`

#### 0.4 draft.vim - convert features

- Add `ConvertMDToHTML()` for `DraftToHTML`
- Add `ConvertMDToPDF()` for `DraftToPDF`
- Add `ConvertHTMLToPDF` and `ConvertToPDFFromTemplate()` for `DraftToTemplatePDF`
- Add template for html conversion
- Change readme format a little
- Add vimawesome link!

#### 0.5 draft.vim - more features

- Add `DraftDragonPDF` for `DraftDragonPDF`
- Add `DraftOpenPDF` for `OpenPDF`
- Add requirements

#### 0.6 draft.vim - added search

- Add `DraftSearch` by word
```
:DraftSearch <term>

:DraftSearch school
```

#### 0.7 draft.vim - search fixes

- Rank searches
- Fix parenthesis in filename bug

#### 0.8 draft.vim - date format fix

- Change default date format to `m/d/y`
- Documentation fixes and additions
- Fix rename symbols issue
- Add testing for python

## Testing
```sh
pip install -r requirements.txt
```
```sh
cd python

pytest
```

## TODO
- Make md to template pdf correctly do syntax highlight

## Maybe TODO
- Make a draft file type with metadata and parse out the metadata when opened in vim, then use this data to search for notes better and stuff, like have raw data for python to search better with
