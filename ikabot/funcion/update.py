#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import gettext
import sys
from ikabot.helpers.pedirInfo import read
from ikabot.helpers.process import run
from ikabot.helpers.gui import *
from ikabot.config import *

t = gettext.translation('update', 
                        localedir, 
                        languages=idiomas,
                        fallback=True)
_ = t.gettext

def update(s,e,fd):
	sys.stdin = os.fdopen(fd)
	print(_('Para actualizar ikabot correr:'))
	print('python3 -m pip install --user --upgrade ikabot')
	read()
	e.set()
