import sublime, sublime_plugin

BufSize = max(
    len('#!/usr/local/bin rubyN.NN.NN'), 
    len('#!/usr/bin/env rubyN.NN.NN'),
    len('#!/usr/local/bin awk -f'),
    len('exec '),
    len('#!/usr/local/bin/expect'),
    80 + len('#include "textflag.h"'),
    80 + len('#include "go_asm.h"'),
    80 + len('.global'),
)


class SyntaxFix(sublime_plugin.EventListener):

    def on_load(self, view):
        buf = view.substr(sublime.Region(0, BufSize))
        st  = view.settings()

        if '/bin/ruby' in buf or '/bin/env ruby' in buf:
           st.set('syntax', 'Packages/Ruby/Ruby.sublime-syntax')

        elif '/bin/awk' in buf or '/bin/env awk' in buf:
            st.set('syntax', 'Packages/Awk/Awk.sublime-syntax')

        elif buf.startswith('exec '):
            st.set('syntax', 'Packages/ShellScript/Bash.sublime-syntax')

        elif '/bin/expect' in buf or '/bin/env expect' in buf:
            st.set('syntax', 'Packages/TCL/Tcl.sublime-syntax')

        elif '"textflag.h"' in buf or '"go_asm.h"' in buf:
            st.set('syntax', 'Packages/sublime-goasm/Goasm.sublime-syntax')

        elif '.global' in buf:
            st.set('syntax', 'Packages/ARM Assembly/Syntaxes/ARM Assembly.tmLanguage')
