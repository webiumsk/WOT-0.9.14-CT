# 2016.02.14 12:48:46 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/lib-tk/ScrolledText.py
"""A ScrolledText widget feels like a text widget but also has a
vertical scroll bar on its right.  (Later, options may be added to
add a horizontal bar as well, to make the bars disappear
automatically when not needed, to move them to the other side of the
window, etc.)

Configuration options are passed to the Text widget.
A Frame widget is inserted between the master and the text, to hold
the Scrollbar widget.
Most methods calls are inherited from the Text widget; Pack, Grid and
Place methods are redirected to the Frame widget however.
"""
__all__ = ['ScrolledText']
from Tkinter import Frame, Text, Scrollbar, Pack, Grid, Place
from Tkconstants import RIGHT, LEFT, Y, BOTH

class ScrolledText(Text):

    def __init__(self, master = None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)
        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() + vars(Grid).keys() + vars(Place).keys()
        methods = set(methods).difference(text_meths)
        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)


def example():
    import __main__
    from Tkconstants import END
    stext = ScrolledText(bg='white', height=10)
    stext.insert(END, __main__.__doc__)
    stext.pack(fill=BOTH, side=LEFT, expand=True)
    stext.focus_set()
    stext.mainloop()


if __name__ == '__main__':
    example()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\lib-tk\scrolledtext.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:48:46 St�edn� Evropa (b�n� �as)
