" draft.vim - Quickly writeup and save drafts for messaging apps in your favorite editor
" Authors:      Jake Roggenbuck
" Version:      0.1
" License:      MIT

if exists('g:loaded_draft_plugin') || &compatible || v:version < 700
	finish
endif

let g:loaded_draft_plugin = 1

func! g:NewDraft()
py3 << EOF
from draft import Draft

draft_name = vim.eval("s:draft_name")
if draft_name == "":
	draft_name = False

draft = Draft()
draft.new(draft_name)

EOF
endfunc
