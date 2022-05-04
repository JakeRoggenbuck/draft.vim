# Draft.vim
Quickly writeup and save drafts for messaging apps in your favorite editor [vimawesome.com/plugin/draft-vim](https://vimawesome.com/plugin/draft-vim)

## Why use Draft.vim
I often write important messages in a vim buffer before I send it.

	- The main reason for this is because it is simply faster.
	- The second reason is you might want syntax highlighting or auto formating. 
	- Also, sometimes you want to write a message without worrying about accidentally sending it.

## Requirements
- Pandoc
- wkhtmltopdf
- Dragon (https://github.com/mwh/dragon)

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

#### `OpenDrafts` Keybind
```vim
nnoremap <Leader>z :call OpenDrafts()<CR>
```

## Use


### Commands

| Command                | Description                                     |
|------------------------|-------------------------------------------------|
| Draft                  | Open a blanck new draft                         |
| Draft `"title"`        | Open a draft with a title                       |
| DraftExt `"extension"` | Change the file extension of a draft            |
| Drafts                 | Open the draft directory in a buffer            |
| DraftCopy              | Copy the contents of the draft to the clipboard |

### More info

	- New draft: run `:Draft` or `:Draft "<Title>"` to auto name with the date and time
	- Edit the file extension: run `:DraftExt .md` to change the file to markdown
	- Open the drafts directory: run `:Drafts`
	- Copy the contents of the current draft `:DraftCopy`
	- Draft will open a new file in a specific directory, with a unique name
	- The file will be based on a template with stuff like the title and datetime

## Install
#### Vim-Plug
`Plug 'jakeroggenbuck/draft.vim'`

#### Vundle
`Plugin 'jakeroggenbuck/draft.vim'`

## Versions

#### 0.1 draft.vim - not fully functional, just a concept

- Open a new draft with a name
- List the draft but no reopening them

#### 0.2 draft.vim - first complete version

- Add `OpenDrafts()`
- Add new command aliases `Draft`, `DraftExt`

#### 0.3 draft.vim - more features

- Add `ClipDraft()` or `DraftCopy`
- Add `Buffer reload for DraftExt`

#### 0.4 draft.vim - convert features
- Add `ConvertMDToHTML()` for `DraftToHTML`
- Add `ConvertMDToPDF()` for `DraftToPDF`
- Add `ConvertHTMLToPDF` and `ConvertToPDFFromTemplate()` for `DraftToTemplatePDF`
- Add template for html conversion
- Change readme format a little
- Add vimawesome link!

## TODO
- BUG: having certain symbols like `(` or `)` in the title break things like the `DraftCopy`
- Keybind or function call to copy contents without header to file
- Make md to template pdf correctly do syntax highlight
- Add feature to xdg open your pdf or html file

## Maybe TODO
- Make a draft file type with metadata and parse out the metadata when opened in vim, then use this data to search for notes better and stuff, like have raw data for python to search better with
