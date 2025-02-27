# -*- coding: utf-8 -*-

"""Compile source code files from UI files. PyQt5 required."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2021"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from os import walk
from os.path import join
from re import sub

try:
    from PyQt5.uic import compileUi
except ImportError:
    try:
        from PyQt6.uic import compileUi
    except ImportError:
        raise ModuleNotFoundError("no compiler found")


def gen_ui():
    """Compile GUIs."""
    count = 0
    for root, _, files in walk("pyslvs_ui"):
        for file in files:
            if not file.endswith('.ui'):
                continue
            target_name = sub(r"([\w ]+)\.ui", r"\1_ui.py", file)
            with open(join(root, target_name), 'w+', encoding='utf-8') as f:
                compileUi(
                    join(root, file).replace('\\', '/'),
                    f,
                    from_imports='pyslvs_ui',
                    import_from='pyslvs_ui'
                )
                f.seek(0)
                script_new = sub(r"from [\w.]+ import [\w]+_rc\n", "",
                                 f.read()
                                 .replace("from PyQt5", "from pyslvs_ui.qt")
                                 .replace("from PyQt6", "from pyslvs_ui.qt")
                                 .replace(root + "/", ""))
                f.seek(0)
                f.truncate()
                f.write(script_new)
            count += 1
    print(f"Compiled {count} UI file(s)")


if __name__ == '__main__':
    gen_ui()
