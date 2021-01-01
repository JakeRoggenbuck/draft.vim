" draft.vim - Quickly writeup and save drafts for messaging apps in your favorite editor
" Authors:      Jake Roggenbuck
" Version:      0.1
" License:      MIT

if exists('g:loaded_draft_plugin') || &compatible || v:version < 700
	finish
endif

let g:loaded_draft_plugin = 1

let g:drafts_directory = "~/Library/drafts"
let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')


func! s:SourcePython()
py3 << EOF
import sys
from os.path import normpath, join
import vim
plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
EOF
endfunc


call s:SourcePython()


func! g:NewDraft(...)
py3 << EOF
from draft import Draft

args = vim.eval("a:0") 
if int(args) > 0:
	draft_name = vim.eval("a:1")
else:
	draft_name = None

drafts_directory = vim.eval("g:drafts_directory")

draft = Draft(draft_name, drafts_directory)
vim.command(f":e {draft.path}")
EOF
endfunc


func! g:ListDrafts()
py3 << EOF
from draft import list_drafts

for x in list_drafts():
	print(x)
EOF
endfunc
