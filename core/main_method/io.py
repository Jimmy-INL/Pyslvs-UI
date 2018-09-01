# -*- coding: utf-8 -*-

"""This module contain the functions that main window needed."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    Tuple,
    List,
    Dict,
    Callable,
    Iterator,
    Union,
)
from pygments.lexers import Python3Lexer
from core.QtModules import (
    Qt,
    QApplication,
    QWidget,
    QMessageBox,
    QDesktopServices,
    QUrl,
    QInputDialog,
    QFileInfo,
    QFileDialog,
    QProgressDialog,
    QSpinBox,
    QDoubleSpinBox,
    QComboBox,
    QCheckBox,
    QLineEdit,
)
from core.info import (
    __version__,
    ARGUMENTS,
    PyslvsAbout,
    check_update,
)
_major, _minor, _build, _label = __version__
from core.io import (
    ScriptDialog,
    slvs_process_script,
    AddTable,
    EditPointTable,
    SlvsParser,
    SlvsOutputDialog,
    DxfOutputDialog,
    QTIMAGES,
    strbetween,
)
from core.libs import (
    kernel_list,
    parse_params,
    PMKSLexer,
)


def _open_url(url: str):
    """Use to open link."""
    QDesktopServices.openUrl(QUrl(url))


def _v_to_slvs(self) -> Callable[[], Tuple[Tuple[int, int]]]:
    """Solvespace edges."""
    
    def v_to_slvs() -> Iterator[Tuple[int, int]]:
        for vlink in self.EntitiesLink.data():
            if vlink.name == 'ground':
                continue
            for i, p in enumerate(vlink.points):
                if i == 0:
                    continue
                yield (vlink.points[0], p)
                if i > 1:
                    yield (vlink.points[i-1], p)
    
    return v_to_slvs


def _readSlvs(self, file_name: str):
    """Read slvs format.
    
    + Choose a group.
    + Read the entities of the group.
    """
    parser = SlvsParser(file_name)
    if not parser.isValid():
        QMessageBox.warning(self,
            "Format error",
            "The format is not support."
        )
        return
    groups = parser.getGroups()
    if not groups:
        QMessageBox.warning(self,
            "Format error",
            "The model file is empty."
        )
        return
    group, ok = QInputDialog.getItem(self,
        "Solvespace groups",
        "Choose a group:\n"
        "(Please know that the group must contain a sketch only.)",
        ["@".join(g) for g in groups],
        0,
        False
    )
    if not ok:
        return
    self.clear()
    self.FileWidget.reset()
    print(f"Read from group: {group}")
    expr = parser.parse(group.split('@')[0])
    self.parseExpression(expr)


def _settings(self) -> Tuple[Tuple[QWidget, Union[int, float, bool]]]:
    """Give the settings of all option widgets."""
    return (
        (self.linewidth_option, 3),
        (self.fontsize_option, 14),
        (self.pathwidth_option, 3),
        (self.scalefactor_option, 10),
        (self.selectionradius_option, 10),
        (self.linktrans_option, 0),
        (self.marginfactor_option, 5),
        (self.jointsize_option, 3),
        (self.zoomby_option, 0),
        (self.snap_option, 1),
        (self.background_option, ""),
        (self.background_opacity_option, 1),
        (self.background_scale_option, 1),
        (self.background_offset_x_option, 0),
        (self.background_offset_y_option, 0),
        (self.undolimit_option, 32),
        (self.planarsolver_option, 0),
        (self.pathpreview_option, 0),
        (self.titlefullpath_option, False),
        (self.consoleerror_option, False),
        # "Do not save the settings" by default.
        (self.dontsave_option, True),
    )


def dragEnterEvent(self, event):
    """Drag file in to our window."""
    mimeData = event.mimeData()
    if not mimeData.hasUrls():
        return
    for url in mimeData.urls():
        file_name = url.toLocalFile()
        if QFileInfo(file_name).suffix() in ('pyslvs', 'slvs'):
            event.acceptProposedAction()


def dropEvent(self, event):
    """Drop file in to our window."""
    file_name = event.mimeData().urls()[-1].toLocalFile()
    suffix = QFileInfo(file_name).suffix()
    if suffix == 'pyslvs':
        self.FileWidget.read(file_name)
    elif suffix == 'slvs':
        _readSlvs(self, file_name)
    event.acceptProposedAction()


def workbookNoSave(self):
    """Workbook not saved signal."""
    self.FileWidget.changed = True
    not_yet_saved = " (not yet saved)"
    self.setWindowTitle(
        self.windowTitle().replace(not_yet_saved, '') +
        not_yet_saved
    )


def workbookSaved(self):
    """Workbook saved signal."""
    self.FileWidget.changed = False
    self.setWindowTitleFullpath()


def setWindowTitleFullpath(self):
    """Set the option 'window title will show the fullpath'."""
    file_name = self.FileWidget.file_name
    if self.titlefullpath_option.isChecked():
        title = file_name.absoluteFilePath()
    else:
        title = file_name.fileName()
    saved_text = " (not yet saved)" if self.FileWidget.changed else ''
    self.setWindowTitle(f"Pyslvs - {title}{saved_text}")


def showHelp(self):
    """Open website: mde.tw"""
    _open_url("http://mde.tw")


def showDotCOM(self):
    """Open website: pyslvs.com"""
    _open_url("http://www.pyslvs.com/blog/index.html")


def showGithub(self):
    """Open website: Github repository."""
    _open_url("https://github.com/KmolYuan/Pyslvs-PyQt5")


def about(self):
    """Open Pyslvs about."""
    dlg = PyslvsAbout(self)
    dlg.show()
    dlg.exec_()


def showConsole(self):
    """Open GUI console."""
    self.OptionTab.setCurrentIndex(2)
    self.History_tab.setCurrentIndex(1)


def loadExample(self):
    """Load examples from 'FileWidget'.
    Return true if successed.
    """
    if self.FileWidget.loadExample():
        self.showExpr()
        self.MainCanvas.zoomToFit()


def importExample(self):
    """Import a example and merge it to canvas."""
    self.FileWidget.loadExample(isImport = True)


def newWorkbook(self):
    """Create (Clean) a new workbook."""
    if self.checkFileChanged():
        return
    self.clear()
    self.FileWidget.reset()
    print("Created a new workbook.")


def clear(self):
    """Clear to create commit stage."""
    self.freemode_disable.trigger()
    self.mechanism_storage_name_tag.clear()
    self.mechanism_storage.clear()
    self.CollectionTabPage.clear()
    self.StructureSynthesis.clear()
    self.InputsWidget.clear()
    self.DimensionalSynthesis.clear()
    self.EntitiesPoint.clear()
    self.EntitiesLink.clear()
    self.EntitiesExpr.clear()
    self.solve()


def importPmksURL(self):
    """Load PMKS URL and turn it to expression."""
    URL, ok = QInputDialog.getText(self,
        "PMKS URL input",
        "Please input link string:"
    )
    if not ok:
        return
    if not URL:
        QMessageBox.warning(self,
            "Loading failed",
            "Your link is in an incorrect format."
        )
        return
    try:
        for s in URL.split('?')[-1].split('&'):
            if 'mech=' in s:
                expr = s.replace('mech=', '').split('|')
                break
        text_list = [s for s in expr if s not in ('', " ", '\n')]
        expr.clear()
        while text_list:
            item = text_list.pop(0).split(',')[:-1]
            for i, e in enumerate(reversed(item)):
                if e in ['R', 'P', 'RP']:
                    t = -(i + 1)
                    break
            links = item[:t]
            item = item[t:]
            type_text = f"{item[0]}:{item[-1]}" if item[0] != 'R' else 'R'
            links_text = ", ".join(links)
            expr.append(f"J[{type_text}, P[{item[1]}, {item[2]}], L[{links_text}]]")
        expr = f'M[{", ".join(expr)}]'
    except:
        QMessageBox.warning(self,
            "Loading failed",
            "Your link is in an incorrect format."
        )
    else:
        self.parseExpression(expr)


def parseExpression(self, expr: str):
    """Parse expression."""
    try:
        args_list = parse_params(expr)
    except Exception as e:
        QMessageBox.warning(self,
            "Loading failed",
            "Your expression is in an incorrect format.\n" + str(e)
        )
    else:
        for args in args_list:
            linkNames = tuple(
                vlink.name for vlink in self.EntitiesLink.data()
            )
            links = args[0].split(',')
            for linkName in links:
                # If link name not exist.
                if linkName not in linkNames:
                    self.addLink(linkName, 'Blue')
            row_count = self.EntitiesPoint.rowCount()
            self.CommandStack.beginMacro(f"Add {{Point{row_count}}}")
            self.CommandStack.push(AddTable(self.EntitiesPoint))
            self.CommandStack.push(EditPointTable(
                row_count,
                self.EntitiesPoint,
                self.EntitiesLink,
                args
            ))
            self.CommandStack.endMacro()


def addEmptyLinks(self, linkcolor: Dict[str, str]):
    """Use to add empty link when loading database."""
    for name, color in linkcolor.items():
        if name != 'ground':
            self.addLink(name, color)


def loadFile(self):
    """Load workbook."""
    if self.checkFileChanged():
        return
    file_name = self.inputFrom(
        "Workbook database",
        ["Pyslvs workbook (*.pyslvs)",
        "Solvespace module (*.slvs)"]
    )
    if not file_name:
        return
    suffix = QFileInfo(file_name).suffix()
    if suffix == 'pyslvs':
        self.FileWidget.read(file_name)
    elif suffix == 'slvs':
        _readSlvs(self, file_name)
    self.MainCanvas.zoomToFit()


def importWorkbook(self):
    """Import from workbook."""
    if self.checkFileChanged():
        return
    file_name = self.inputFrom(
        "Workbook database (Import)",
        ["Pyslvs workbook (*.pyslvs)"]
    )
    if not file_name:
        return
    self.FileWidget.importMechanism(file_name)


def save(self, isBranch: bool):
    """Save action."""
    file_name = self.FileWidget.file_name.absoluteFilePath()
    if self.FileWidget.file_name.suffix() == 'pyslvs':
        self.FileWidget.save(file_name, isBranch)
    else:
        self.saveAs(isBranch)


def saveAs(self, isBranch: bool):
    """Save as action."""
    file_name = self.outputTo("workbook", ["Pyslvs workbook (*.pyslvs)"])
    if file_name:
        self.FileWidget.save(file_name, isBranch)
        self.saveReplyBox("Workbook", file_name)


def saveSlvs(self):
    """Solvespace 2d save function."""
    dlg = SlvsOutputDialog(
        self.env,
        self.FileWidget.file_name.baseName(),
        self.EntitiesPoint.dataTuple(),
        _v_to_slvs(self),
        self
    )
    dlg.show()
    if dlg.exec_():
        path = dlg.path_edit.text() or dlg.path_edit.placeholderText()
        self.setLocate(path)
        self.saveReplyBox("Solvespace sketch", path)


def saveDXF(self):
    """DXF 2d save function."""
    dlg = DxfOutputDialog(
        self.env,
        self.FileWidget.file_name.baseName(),
        self.EntitiesPoint.dataTuple(),
        _v_to_slvs(self),
        self
    )
    dlg.show()
    if dlg.exec_():
        path = dlg.path_edit.text() or dlg.path_edit.placeholderText()
        self.setLocate(path)
        self.saveReplyBox("Drawing Exchange Format", path)


def savePicture(self):
    """Picture save function."""
    file_name = self.outputTo("picture", QTIMAGES)
    if not file_name:
        return
    pixmap = self.MainCanvas.grab()
    pixmap.save(file_name, format=QFileInfo(file_name).suffix())
    self.saveReplyBox("Picture", file_name)


def outputTo(self, format_name: str, format_choose: List[str]) -> str:
    """Simple to support mutiple format."""
    suffix0 = strbetween(format_choose[0], '(', ')').split('*')[-1]
    file_name, suffix = QFileDialog.getSaveFileName(
        self,
        f"Save to {format_name}...",
        self.env + '/' + self.FileWidget.file_name.baseName() + suffix0,
        ';;'.join(format_choose)
    )
    if file_name:
        suffix = strbetween(suffix, '(', ')').split('*')[-1]
        print(f"Format: {suffix}")
        if QFileInfo(file_name).suffix() != suffix[1:]:
            file_name += suffix
        self.setLocate(QFileInfo(file_name).absolutePath())
    return file_name


def saveReplyBox(self, title: str, file_name: str):
    """Show message when successfully saved."""
    size = QFileInfo(file_name).size()
    print("Size: {}" + (
        f"{size / 1024 / 1024:.02f} MB"
        if size / 1024 // 1024 else
        "{size / 1024:.02f} KB"
    ))
    QMessageBox.information(self,
        f"Initial Saved: {title}",
        f"Successfully saved:\n{file_name}"
    )
    print(f"Initial saved: [\"{file_name}\"]")


def inputFrom(self,
    format_name: str,
    format_choose: List[str],
    multiple: bool = False
) -> str:
    """Get file name(s)."""
    args = (
        f"Open {format_name} file{'s' if multiple else ''}...",
        self.env,
        ';;'.join(format_choose)
    )
    if multiple:
        file_name_s, suffix = QFileDialog.getOpenFileNames(self, *args)
    else:
        file_name_s, suffix = QFileDialog.getOpenFileName(self, *args)
    if file_name_s:
        suffix = strbetween(suffix, '(', ')').split('*')[-1]
        print(f"Format: {suffix}")
        if type(file_name_s) == str:
            self.setLocate(QFileInfo(file_name_s).absolutePath())
        else:
            self.setLocate(QFileInfo(file_name_s[0]).absolutePath())
    return file_name_s


def savePMKS(self):
    """Output to PMKS as URL."""
    url = "http://designengrlab.github.io/PMKS/pmks.html?mech="
    urlTable = []
    for row in range(self.EntitiesPoint.rowCount()):
        TypeAndAngle = self.EntitiesPoint.item(row, 2).text().split(':')
        pointData = [
            self.EntitiesPoint.item(row, 1).text(),
            TypeAndAngle[0],
            self.EntitiesPoint.item(row, 4).text(),
            self.EntitiesPoint.item(row, 5).text(),
        ]
        if len(TypeAndAngle)==2:
            pointData.append(TypeAndAngle[1])
        pointData.append('tfff')
        urlTable.append(','.join(pointData))
    url += '|'.join(urlTable)+'|'
    text = '\n'.join((
        "Copy and past this link to web browser:\n",
        url + '\n',
        "If you have installed Microsoft Silverlight in "
        "Internet Explorer as default browser, "
        "just click \"Open\" button to open it in PMKS website."
    ))
    reply = QMessageBox.information(self,
        "PMKS web server",
        text,
        (QMessageBox.Save | QMessageBox.Open | QMessageBox.Close),
        QMessageBox.Save
    )
    if reply == QMessageBox.Open:
        _open_url(url)
    elif reply == QMessageBox.Save:
        QApplication.clipboard().setText(url)


def savePictureClipboard(self):
    """Capture the canvas image to clipboard."""
    QApplication.clipboard().setPixmap(self.MainCanvas.grab())
    QMessageBox.information(self,
        "Captured!",
        "Canvas widget picture is copy to clipboard."
    )


def showExpr(self):
    """Output as expression."""
    context = ",\n".join(" " * 4 + vpoint.expr for vpoint in self.EntitiesPoint.data())
    dlg = ScriptDialog(
        f"# Generate by Pyslvs v{_major}.{_minor}.{_build} ({_label})\n"
        f"# Project \"{self.FileWidget.file_name.baseName()}\"\n" +
        (f"M[\n{context}\n]" if context else "M[]"),
        PMKSLexer(),
        "Pyslvs expression",
        ["Text file (*.txt)"],
        self
    )
    dlg.show()
    dlg.exec_()


def showPyScript(self):
    """Output to Python script for Jupyter notebook."""
    dlg = ScriptDialog(
        f"# Generate by Pyslvs v{_major}.{_minor}.{_build} ({_label})\n"
        f"# Project \"{self.FileWidget.file_name.baseName()}\"\n" +
        slvs_process_script(
            tuple(vpoint.expr for vpoint in self.EntitiesPoint.data()),
            tuple((b, d) for b, d, a in self.InputsWidget.inputPair())
        ),
        Python3Lexer(),
        "Python script",
        ["Python3 Script (*.py)"],
        self
    )
    dlg.show()
    dlg.exec_()


def checkUpdate(self):
    """Check for update."""
    progdlg = QProgressDialog("Checking update ...", "Cancel", 0, 3, self)
    progdlg.setAttribute(Qt.WA_DeleteOnClose, True)
    progdlg.setWindowTitle("Check for update")
    progdlg.resize(400, progdlg.height())
    progdlg.setModal(True)
    progdlg.show()
    url = check_update(progdlg)
    if not url:
        QMessageBox.information(self,
            "Pyslvs is up to date",
            "You are using the latest version of Pyslvs."
        )
        return
    reply = QMessageBox.question(
        self,
        "Pyslvs has update",
        "Do you want to get it from Github?",
        (QMessageBox.Ok | QMessageBox.Cancel),
        QMessageBox.Ok
    )
    if reply == QMessageBox.Ok:
        _open_url(url)


def checkFileChanged(self) -> bool:
    """If the user has not saved the change.
    
    Return True if user want to "discard" the operation.
    """
    if not self.FileWidget.changed:
        return False
    reply = QMessageBox.question(
        self,
        "Message",
        "Are you sure to quit?\nAny changes won't be saved.",
        (QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel),
        QMessageBox.Save
    )
    if reply == QMessageBox.Save:
        self.save()
        return self.FileWidget.changed
    elif reply == QMessageBox.Discard:
        return False
    return True


def restoreSettings(self):
    """Restore Pyslvs settings."""
    for widget, value in _settings(self):
        name = widget.objectName()
        widget_type = type(widget)
        if widget_type == QSpinBox:
            widget.setValue(self.settings.value(name, value, type=int))
        elif widget_type == QDoubleSpinBox:
            widget.setValue(self.settings.value(name, value, type=float))
        elif widget_type == QComboBox:
            widget.setCurrentIndex(self.settings.value(name, value, type=int))
        elif widget_type == QCheckBox:
            widget.setChecked(self.settings.value(name, value, type=bool))
        elif widget_type == QLineEdit:
            widget.setText(self.settings.value(name, value, type=str))
    # Specified solver setting.
    if ARGUMENTS.kernel:
        if ARGUMENTS.kernel == "pyslvs":
            kernel_name = kernel_list[0]
        elif ARGUMENTS.kernel == "python_solvespace":
            kernel_name = kernel_list[1]
        elif ARGUMENTS.kernel == "sketch_solve":
            kernel_name = kernel_list[2]
        self.planarsolver_option.setCurrentText(kernel_name)
        self.pathpreview_option.setCurrentText(kernel_name)


def saveSettings(self):
    """Save Pyslvs settings (auto save when close event)."""
    if self.dontsave_option.isChecked():
        self.settings.clear()
        return
    for widget, value in _settings(self):
        name = widget.objectName()
        widget_type = type(widget)
        if widget_type in (QSpinBox, QDoubleSpinBox):
            self.settings.setValue(name, widget.value())
        elif widget_type == QComboBox:
            self.settings.setValue(name, widget.currentIndex())
        elif widget_type == QCheckBox:
            self.settings.setValue(name, widget.isChecked())
        elif widget_type == QLineEdit:
            self.settings.setValue(name, widget.text())


def resetOptions(self):
    """Reset options with default value."""
    for widget, value in _settings(self):
        widget_type = type(widget)
        if widget_type in (QSpinBox, QDoubleSpinBox):
            widget.setValue(value)
        elif widget_type == QComboBox:
            widget.setCurrentIndex(value)
        elif widget_type == QCheckBox:
            widget.setChecked(value)
        elif widget_type == QLineEdit:
            widget.setText(value)


def readFromArgs(self):
    if not ARGUMENTS.file:
        return
    suffix = QFileInfo(ARGUMENTS.file).suffix()
    if suffix == 'pyslvs':
        self.FileWidget.read(ARGUMENTS.file)
    elif suffix == 'slvs':
        _readSlvs(self, ARGUMENTS.file)
    else:
        print("Unsupported format has been ignore when startup.")
