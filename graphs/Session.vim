let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/Code/Python/Interactive\ Python/graphs
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +24 ~/Dropbox/Code/Python/Interactive\ Python/graphs/word_ladder.py
badd +85 term://.//41988:zsh\ \#\ terminal
badd +1 ~/Dropbox/Code/Python/Interactive\ Python/graphs/hello.txt
argglobal
silent! argdel *
$argadd word_ladder.py
edit ~/Dropbox/Code/Python/Interactive\ Python/graphs/word_ladder.py
set splitbelow splitright
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe '1resize ' . ((&lines * 30 + 21) / 43)
exe '2resize ' . ((&lines * 10 + 21) / 43)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 13 - ((12 * winheight(0) + 15) / 30)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
13
normal! 019|
lcd ~/Dropbox/Code/Python/Interactive\ Python/graphs
wincmd w
argglobal
if bufexists('term://.//41988:zsh\ \#\ terminal') | buffer term://.//41988:zsh\ \#\ terminal | else | edit term://.//41988:zsh\ \#\ terminal | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 113 - ((9 * winheight(0) + 5) / 10)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
113
normal! 03|
lcd ~/Dropbox/Code/Python/Interactive\ Python/graphs
wincmd w
exe '1resize ' . ((&lines * 30 + 21) / 43)
exe '2resize ' . ((&lines * 10 + 21) / 43)
tabnext 1
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOF
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
