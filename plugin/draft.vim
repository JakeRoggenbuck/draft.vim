" draft.vim - Quickly writeup and save drafts for messaging apps in your favorite editor
" Authors:      Jake Roggenbuck
" Version:      0.1
" License:      MIT

if exists('g:loaded_draft_plugin') || &compatible || v:version < 700
	finish
endif

let g:loaded_draft_plugin = 1

let g:drafts_directory = "~/Library/draft"

func! g:NewDraft(draft_num)
py3 << EOF
from draft import Draft
import vim

draft_name = vim.eval("a:draft_name")
drafts_directory = vim.eval("g:drafts_directory")

draft = Draft(draft_name, drafts_directory)
vim.command(f":e {draft.path}")
EOF
endfunc
