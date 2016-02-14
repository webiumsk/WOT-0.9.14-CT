# 2016.02.14 12:48:19 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/Bindings.py
"""Define the menu contents, hotkeys, and event bindings.

There is additional configuration information in the EditorWindow class (and
subclasses): the menus are created there based on the menu_specs (class)
variable, and menus not created are silently skipped in the code here.  This
makes it possible, for example, to define a Debug menu which is only present in
the PythonShell window, and a Format menu which is only present in the Editor
windows.

"""
from idlelib.configHandler import idleConf
menudefs = [('file', [('_New File', '<<open-new-window>>'),
   ('_Open...', '<<open-window-from-file>>'),
   ('Open _Module...', '<<open-module>>'),
   ('Class _Browser', '<<open-class-browser>>'),
   ('_Path Browser', '<<open-path-browser>>'),
   None,
   ('_Save', '<<save-window>>'),
   ('Save _As...', '<<save-window-as-file>>'),
   ('Save Cop_y As...', '<<save-copy-of-window-as-file>>'),
   None,
   ('Prin_t Window', '<<print-window>>'),
   None,
   ('_Close', '<<close-window>>'),
   ('E_xit', '<<close-all-windows>>')]),
 ('edit', [('_Undo', '<<undo>>'),
   ('_Redo', '<<redo>>'),
   None,
   ('Cu_t', '<<cut>>'),
   ('_Copy', '<<copy>>'),
   ('_Paste', '<<paste>>'),
   ('Select _All', '<<select-all>>'),
   None,
   ('_Find...', '<<find>>'),
   ('Find A_gain', '<<find-again>>'),
   ('Find _Selection', '<<find-selection>>'),
   ('Find in Files...', '<<find-in-files>>'),
   ('R_eplace...', '<<replace>>'),
   ('Go to _Line', '<<goto-line>>')]),
 ('format', [('_Indent Region', '<<indent-region>>'),
   ('_Dedent Region', '<<dedent-region>>'),
   ('Comment _Out Region', '<<comment-region>>'),
   ('U_ncomment Region', '<<uncomment-region>>'),
   ('Tabify Region', '<<tabify-region>>'),
   ('Untabify Region', '<<untabify-region>>'),
   ('Toggle Tabs', '<<toggle-tabs>>'),
   ('New Indent Width', '<<change-indentwidth>>')]),
 ('run', [('Python Shell', '<<open-python-shell>>')]),
 ('shell', [('_View Last Restart', '<<view-restart>>'), ('_Restart Shell', '<<restart-shell>>')]),
 ('debug', [('_Go to File/Line', '<<goto-file-line>>'),
   ('!_Debugger', '<<toggle-debugger>>'),
   ('_Stack Viewer', '<<open-stack-viewer>>'),
   ('!_Auto-open Stack Viewer', '<<toggle-jit-stack-viewer>>')]),
 ('options', [('_Configure IDLE...', '<<open-config-dialog>>'), None]),
 ('help', [('_About IDLE', '<<about-idle>>'),
   None,
   ('_IDLE Help', '<<help>>'),
   ('Python _Docs', '<<python-docs>>')])]
default_keydefs = idleConf.GetCurrentKeySet()
# okay decompyling c:\Users\PC\wotsources\files\originals\res_bw\scripts\common\lib\idlelib\bindings.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.02.14 12:48:19 St�edn� Evropa (b�n� �as)
