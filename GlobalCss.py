# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/Arthaey/anki-global-css
#
# Also available for Anki at https://ankiweb.net/shared/info/ FIXME

import os
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QAction
from anki.hooks import addHook
from aqt import mw
from aqt.utils import showInfo

STYLESHEET_FILENAME = "_global.css"

def replaceCssForAllModels():
    mediaDir = mw.col.media.dir()
    filename = unicode(os.path.join(mediaDir, STYLESHEET_FILENAME))
    with open(filename, "r") as file:
        css = file.read()
        for model in mw.col.models.all():
            # TODO: check whether it's changed
            model["css"] = css
            model["usn"] = -1
        mw.col.save("Global CSS Updated")
        mw.col.reset()
    showInfo("Global CSS updated.")


addHook("profileLoaded", replaceCssForAllModels)

action = QAction("Update global CSS", mw)
mw.connect(action, SIGNAL("triggered()"), replaceCssForAllModels)
mw.form.menuTools.addAction(action)
