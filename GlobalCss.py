# -*- coding: utf-8 -*-
# See github page to report issues or to contribute:
# https://github.com/Arthaey/anki-global-css
#
# Also available for Anki at https://ankiweb.net/shared/info/ FIXME

import os
from anki.hooks import addHook
from aqt import mw

STYLESHEET_FILENAME = "_global.css"

def replaceCssForAllModels():
    mediaDir = mw.col.media.dir()
    filename = unicode(os.path.join(mediaDir, STYLESHEET_FILENAME))
    with open(filename, "r") as file:
        css = file.read()
        for model in mw.col.models.all():
            model["css"] = css
            model["usn"] = -1
        mw.col.models.flush()


addHook("profileLoaded", replaceCssForAllModels)
