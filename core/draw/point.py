# -*- coding: utf-8 -*-
from .modules import *

class New_point(QDialog, point_Dialog):
    def __init__(self, parent=None):
        super(New_point, self).__init__(parent)
        self.setupUi(self)
