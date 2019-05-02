# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/Arthaey/anki-global-css
#
# Also available for Anki at https://ankiweb.net/shared/info/1659096147

import codecs
import os

from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QAction
from anki.hooks import addHook
from aqt import mw
from aqt.utils import showInfo

STYLESHEET_FILENAME = "_global.css"

SHOW_ALERT = True


def replaceCssForAllModels(manuallyTrigger=False):
    mediaDir = mw.col.media.dir()
    filename = unicode(os.path.join(mediaDir, STYLESHEET_FILENAME))

    with codecs.open(filename, "r", "utf-8") as file:
        css = file.read()
        updated = False

        for model in mw.col.models.all():
            oldCss = model["css"]
            if oldCss != css:
                model["css"] = css
                model["usn"] = -1
                updated = True

        if updated:
            mw.col.save("Global CSS Updated")
            mw.col.reset()
            msg = "Global CSS updated."
        elif manuallyTrigger:
            msg = "Global CSS is already up-to-date."

        if SHOW_ALERT:
            showInfo(msg)


def _manuallyReplaceCssForAllModels():
    replaceCssForAllModels(manuallyTrigger=True)


addHook("profileLoaded", replaceCssForAllModels)

action = QAction("Update global CSS", mw)
mw.connect(action, SIGNAL("triggered()"), _manuallyReplaceCssForAllModels)
mw.form.menuTools.addSeparator()
mw.form.menuTools.addAction(action)
