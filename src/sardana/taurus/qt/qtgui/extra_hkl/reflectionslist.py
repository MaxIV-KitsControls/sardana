#!/usr/bin/env python

# Code implementation generated from reading ui file 'reflectionslist.ui'
#
# Created: Tue Jul 30 13:24:35 2013
#      by: Taurus UI code generator 3.0.1
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from taurus.qt.qtgui.container import TaurusWidget
from taurus.qt.qtgui.util.ui import UILoadable


@UILoadable(with_ui="_ui")
class ReflectionsList(TaurusWidget):

    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)

        self.loadUi(filename="reflectionslist.ui")

    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'reflectionslist'
        ret['group'] = 'Taurus Containers'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = True
        return ret


def main():
    app = Qt.QApplication(sys.argv)
    w = ReflectionsList()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
