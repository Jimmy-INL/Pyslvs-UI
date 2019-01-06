# -*- coding: utf-8 -*-

"""This module contain the functions that main window needed."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    Tuple,
    Sequence,
    Dict,
    Callable,
    Iterator,
    Union,
)
from abc import abstractmethod
from pygments.lexers.python import Python3Lexer
from lark.exceptions import LarkError
from core.QtModules import (
    pyqtSlot,
    qt_image_format,
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
    QAbcMeta,
)
from core.info import (
    __version__,
    ARGUMENTS,
    PyslvsAbout,
    check_update,
)
from core.io import (
    ScriptDialog,
    slvs_process_script,
    SlvsParser,
    SlvsOutputDialog,
    DxfOutputDialog,
    str_between,
)
from core.widgets import AddTable, EditPointTable
from core.libs import (
    kernel_list,
    parse_params,
    PMKSLexer,
)
from .actions import ActionMethodInterface
_major, _minor, _build, _label = __version__
Settings: type = Union[int, float, bool, str]


def _open_url(url: str):
    """Use to open link."""
    QDesktopServices.openUrl(QUrl(url))


class IOMethodInterface(ActionMethodInterface, metaclass=QAbcMeta):

    """Abstract class for action methods."""

    def __init__(self):
        super(IOMethodInterface, self).__init__()

    def __v_to_slvs(self) -> Callable[[], Iterator[Tuple[int, int]]]:
        """Solvespace edges."""

        def func() -> Iterator[Tuple[int, int]]:
            for vlink in self.EntitiesLink.data():
                if vlink.name == 'ground':
                    continue
                for i, p in enumerate(vlink.points):
                    if i == 0:
                        continue
                    yield (vlink.points[0], p)
                    if i > 1:
                        yield (vlink.points[i-1], p)

        return func

    def __read_slvs(self, file_name: str):
        """Read slvs format.

        + Choose a group.
        + Read the entities of the group.
        """
        parser = SlvsParser(file_name)
        if not parser.isValid():
            QMessageBox.warning(
                self,
                "Format error",
                "The format is not support."
            )
            return
        groups = parser.getGroups()
        if not groups:
            QMessageBox.warning(
                self,
                "Format error",
                "The model file is empty."
            )
            return
        group, ok = QInputDialog.getItem(
            self,
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
        self.DatabaseWidget.reset()
        print(f"Read from group: {group}")
        self.parseExpression(parser.parse(group.split('@')[0]))

    def __settings(self) -> Tuple[Tuple[QWidget, Settings], ...]:
        """Give the settings of all option widgets."""
        return (
            (self.linewidth_option, 3),
            (self.fontsize_option, 14),
            (self.pathwidth_option, 3),
            (self.scalefactor_option, 10),
            (self.selectionradius_option, 10),
            (self.linktrans_option, 0),
            (self.marginfactor_option, 5),
            (self.jointsize_option, 5),
            (self.zoomby_option, 0),
            (self.snap_option, 1),
            (self.background_option, ""),
            (self.background_opacity_option, 1),
            (self.background_scale_option, 1),
            (self.background_offset_x_option, 0),
            (self.background_offset_y_option, 0),
            (self.undolimit_option, 32),
            (self.planarsolver_option, 0),
            (self.pathpreview_option, self.pathpreview_option.count() - 1),
            (self.titlefullpath_option, False),
            (self.consoleerror_option, False),
            # "Do not save the settings" by default.
            (self.dontsave_option, True),
        )

    def dragEnterEvent(self, event):
        """Drag file in to our window."""
        mime_data = event.mimeData()
        if not mime_data.hasUrls():
            return
        for url in mime_data.urls():
            suffix = QFileInfo(url.toLocalFile()).completeSuffix()
            if suffix in {'pyslvs.yml', 'pyslvs', 'slvs'}:
                event.acceptProposedAction()

    def dropEvent(self, event):
        """Drop file in to our window."""
        file_name = event.mimeData().urls()[-1].toLocalFile()
        self.__load_file(file_name)
        event.acceptProposedAction()

    def workbookNoSave(self):
        """Workbook not saved signal."""
        self.DatabaseWidget.changed = True
        not_yet_saved = " (not yet saved)"
        self.setWindowTitle(
            self.windowTitle().replace(not_yet_saved, '') + not_yet_saved
        )

    def workbookSaved(self):
        """Workbook saved signal."""
        self.DatabaseWidget.changed = False
        self.setWindowTitleFullpath()

    @pyqtSlot(name='on_windowTitle_fullpath_clicked')
    def setWindowTitleFullpath(self):
        """Set the option 'window title will show the fullpath'."""
        file_name = self.DatabaseWidget.file_name
        if self.titlefullpath_option.isChecked():
            title = file_name.absoluteFilePath()
        else:
            title = file_name.fileName()
        saved_text = " (not yet saved)" if self.DatabaseWidget.changed else ''
        self.setWindowTitle(f"Pyslvs - {title}{saved_text}")

    @pyqtSlot(name='on_action_mde_tw_triggered')
    def showHelp(self):
        """Open website: mde.tw"""
        _open_url("http://mde.tw")
        self.showMinimized()

    @pyqtSlot(name='on_action_pyslvs_com_triggered')
    def showDotCOM(self):
        """Open website: pyslvs.com"""
        _open_url("http://www.pyslvs.com/blog/index.html")
        self.showMinimized()

    @pyqtSlot(name='on_action_github_repository_triggered')
    def showGithub(self):
        """Open website: Github repository."""
        _open_url("https://github.com/KmolYuan/Pyslvs-PyQt5")
        self.showMinimized()

    @pyqtSlot(name='on_action_about_triggered')
    def about(self):
        """Open Pyslvs about."""
        dlg = PyslvsAbout(self)
        dlg.show()
        dlg.exec_()

    @pyqtSlot(name='on_action_Console_triggered')
    def showConsole(self):
        """Open GUI console."""
        self.OptionTab.setCurrentIndex(2)
        self.History_tab.setCurrentIndex(1)

    @pyqtSlot(name='on_action_example_triggered')
    def loadExample(self):
        """Load examples from 'DatabaseWidget'. Return true if succeeded."""
        if self.DatabaseWidget.loadExample():
            self.showExpr()
            self.MainCanvas.zoomToFit()

    @pyqtSlot(name='on_action_import_example_triggered')
    def importExample(self):
        """Import a example and merge it to canvas."""
        self.DatabaseWidget.loadExample(is_import=True)

    @pyqtSlot(name='on_action_new_workbook_triggered')
    def newWorkbook(self):
        """Create (Clean) a new workbook."""
        if self.checkFileChanged():
            return
        self.clear()
        self.DatabaseWidget.reset()
        print("Created a new workbook.")

    def clear(self):
        """Clear to create commit stage."""
        self.free_move_disable.trigger()
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

    @pyqtSlot(name='on_action_import_pmks_url_triggered')
    def importPmksURL(self):
        """Load PMKS URL and turn it to expression."""
        url, ok = QInputDialog.getText(
            self,
            "PMKS URL input",
            "Please input link string:"
        )
        if not ok:
            return
        if not url:
            QMessageBox.warning(
                self,
                "Loading failed",
                "Your link is in an incorrect format."
            )
            return
        try:
            for s in url.split('?')[-1].split('&'):
                if 'mech=' in s:
                    expr = s.replace('mech=', '').split('|')
                    break
            else:
                raise ValueError
            text_list = [s for s in expr if s not in ('', " ", '\n')]
            expr.clear()
            while text_list:
                item = text_list.pop(0).split(',')[:-1]
                for i, e in enumerate(reversed(item)):
                    if e in {'R', 'P', 'RP'}:
                        t = -(i + 1)
                        break
                else:
                    raise ValueError
                links = item[:t]
                item = item[t:]
                type_text = f"{item[0]}:{item[-1]}" if item[0] != 'R' else 'R'
                links_text = ", ".join(links)
                expr.append(f"J[{type_text}, P[{item[1]}, {item[2]}], L[{links_text}]]")
            expr = f'M[{", ".join(expr)}]'
        except (ValueError, IndexError):
            QMessageBox.warning(
                self,
                "Loading failed",
                "Your link is in an incorrect format."
            )
        else:
            self.parseExpression(expr)

    def parseExpression(self, expr: str):
        """Parse expression."""
        try:
            args_list = parse_params(expr)
        except LarkError:
            QMessageBox.warning(
                self,
                "Loading failed",
                f"Your expression is in an incorrect format."
            )
        else:
            for args in args_list:
                links = args[0].split(',')
                link_names = {
                    vlink.name for vlink in self.EntitiesLink.data()
                }
                for link_name in links:
                    # If link name not exist.
                    if link_name not in link_names:
                        self.addLink(link_name, 'Blue')
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

    def addEmptyLinks(self, link_color: Dict[str, str]):
        """Use to add empty link when loading database."""
        for name, color in link_color.items():
            if name != 'ground':
                self.addLink(name, color)

    @pyqtSlot(name='on_action_load_file_triggered')
    def __load_file(self, file_name: str = ""):
        """Load a supported format in Pyslvs."""
        if self.checkFileChanged():
            return

        if not file_name:
            file_name = self.inputFrom("Workbook database", [
                "Pyslvs YAML file (*.pyslvs.yml)",
                "Pyslvs workbook (*.pyslvs)",
                "Solvespace module (*.slvs)",
            ])
            if not file_name:
                return

        suffix = QFileInfo(file_name).completeSuffix()
        if suffix == 'pyslvs.yml':
            self.YamlEditor.load(file_name)
        elif suffix == 'pyslvs':
            self.DatabaseWidget.read(file_name)
        elif suffix == 'slvs':
            self.__read_slvs(file_name)

        self.MainCanvas.zoomToFit()

    @pyqtSlot(name='on_action_import_database_triggered')
    def __import_database(self):
        """Import from workbook."""
        if self.checkFileChanged():
            return
        file_name = self.inputFrom(
            "Workbook database (Import)",
            ["Pyslvs workbook (*.pyslvs)"]
        )
        if not file_name:
            return
        self.DatabaseWidget.importMechanism(file_name)

    @pyqtSlot(name='on_action_save_triggered')
    def save(self):
        """Save action. (YAML)"""
        if self.DatabaseWidget.file_name.completeSuffix() == 'pyslvs.yml':
            self.YamlEditor.save()
        else:
            self.__save_as()

    @pyqtSlot(name='on_action_save_as_triggered')
    def __save_as(self):
        """Save as action. (YAML)"""
        file_name = self.outputTo("YAML profile", ["Pyslvs YAML file (*.pyslvs.yml)"])
        if file_name:
            self.YamlEditor.save(file_name)
            self.saveReplyBox("YAML Profile", file_name)

    @pyqtSlot(name='on_action_commit_triggered')
    def commit(self, is_branch: bool = False):
        """Save action. (Database)"""
        file_name = self.DatabaseWidget.file_name.absoluteFilePath()
        if self.DatabaseWidget.file_name.suffix() == 'pyslvs':
            self.DatabaseWidget.save(file_name, is_branch)
        else:
            self.__commit_as(is_branch)

    @pyqtSlot(name='on_action_commit_as_triggered')
    def __commit_as(self, is_branch: bool = False):
        """Save as action. (Database)"""
        file_name = self.outputTo("workbook", ["Pyslvs workbook (*.pyslvs)"])
        if file_name:
            self.DatabaseWidget.save(file_name, is_branch)
            self.saveReplyBox("Workbook", file_name)

    @pyqtSlot(name='on_action_export_slvs_triggered')
    def __export_slvs(self):
        """Solvespace 2d save function."""
        dlg = SlvsOutputDialog(
            self.env,
            self.DatabaseWidget.file_name.baseName(),
            self.EntitiesPoint.dataTuple(),
            self.__v_to_slvs(),
            self
        )
        dlg.show()
        if dlg.exec_():
            path = dlg.path_edit.text() or dlg.path_edit.placeholderText()
            self.setLocate(path)
            self.saveReplyBox("Solvespace sketch", path)

    @pyqtSlot(name='on_action_export_dxf_triggered')
    def __export_dxf(self):
        """DXF 2d save function."""
        dlg = DxfOutputDialog(
            self.env,
            self.DatabaseWidget.file_name.baseName(),
            self.EntitiesPoint.dataTuple(),
            self.__v_to_slvs(),
            self
        )
        dlg.show()
        if dlg.exec_():
            path = dlg.path_edit.text() or dlg.path_edit.placeholderText()
            self.setLocate(path)
            self.saveReplyBox("Drawing Exchange Format", path)

    @pyqtSlot(name='on_action_export_image_triggered')
    def __export_image(self):
        """Picture save function."""
        file_name = self.outputTo("picture", qt_image_format)
        if not file_name:
            return
        pixmap = self.MainCanvas.grab()
        pixmap.save(file_name)
        self.saveReplyBox("Picture", file_name)

    def outputTo(self, format_name: str, format_choose: Sequence[str]) -> str:
        """Simple to support multiple format."""
        file_name, suffix = QFileDialog.getSaveFileName(
            self,
            f"Save to {format_name}...",
            self.env + '/' + self.DatabaseWidget.file_name.baseName(),
            ';;'.join(format_choose)
        )
        if file_name:
            suffix = str_between(suffix, '(', ')').split('*')[-1]
            print(f"Format: {suffix}")
            if QFileInfo(file_name).completeSuffix() != suffix[1:]:
                file_name += suffix
            self.setLocate(QFileInfo(file_name).absolutePath())
        return file_name

    def saveReplyBox(self, title: str, file_name: str):
        """Show message when successfully saved."""
        size = QFileInfo(file_name).size()
        print("Size: " + (
            f"{size / 1024 / 1024:.02f} MB"
            if size / 1024 // 1024 else
            f"{size / 1024:.02f} KB"
        ))
        QMessageBox.information(
            self,
            f"Initial Saved: {title}",
            f"Successfully saved:\n{file_name}"
        )
        print(f"Initial saved: [\"{file_name}\"]")

    def inputFrom(
        self,
        format_name: str,
        format_choose: Sequence[str],
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
            suffix = str_between(suffix, '(', ')').split('*')[-1]
            print(f"Format: {suffix}")
            if type(file_name_s) == str:
                self.setLocate(QFileInfo(file_name_s).absolutePath())
            else:
                self.setLocate(QFileInfo(file_name_s[0]).absolutePath())
        return file_name_s

    @pyqtSlot(name='on_action_export_pmks_url_triggered')
    def savePMKS(self):
        """Output to PMKS as URL."""
        url = "http://designengrlab.github.io/PMKS/pmks.html?mech="
        url_table = []
        for row in range(self.EntitiesPoint.rowCount()):
            type_and_angle = self.EntitiesPoint.item(row, 2).text().split(':')
            point_data = [
                self.EntitiesPoint.item(row, 1).text(),
                type_and_angle[0],
                self.EntitiesPoint.item(row, 4).text(),
                self.EntitiesPoint.item(row, 5).text(),
            ]
            if len(type_and_angle) == 2:
                point_data.append(type_and_angle[1])
            point_data.append('tfff')
            url_table.append(','.join(point_data))
        url += '|'.join(url_table) + '|'
        text = '\n'.join((
            "Copy and past this link to web browser:\n",
            url + '\n',
            "If you have installed Microsoft Silverlight in "
            "Internet Explorer as default browser, "
            "just click \"Open\" button to open it in PMKS website."
        ))
        reply = QMessageBox.information(
            self,
            "PMKS web server",
            text,
            (QMessageBox.Save | QMessageBox.Open | QMessageBox.Close),
            QMessageBox.Save
        )
        if reply == QMessageBox.Open:
            _open_url(url)
        elif reply == QMessageBox.Save:
            QApplication.clipboard().setText(url)

    @pyqtSlot(name='on_action_export_image_clipboard_triggered')
    def savePictureClipboard(self):
        """Capture the canvas image to clipboard."""
        QApplication.clipboard().setPixmap(self.MainCanvas.grab())
        QMessageBox.information(
            self,
            "Captured!",
            "Canvas widget picture is copy to clipboard."
        )

    @pyqtSlot(name='on_action_exprsion_triggered')
    def showExpr(self):
        """Output as expression."""
        context = ",\n".join(" " * 4 + vpoint.expr for vpoint in self.EntitiesPoint.data())
        dlg = ScriptDialog(
            f"# Generate by Pyslvs v{_major}.{_minor}.{_build} ({_label})\n"
            f"# Project \"{self.DatabaseWidget.file_name.baseName()}\"\n" +
            (f"M[\n{context}\n]" if context else "M[]"),
            PMKSLexer(),
            "Pyslvs expression",
            ["Text file (*.txt)"],
            self
        )
        dlg.show()
        dlg.exec_()

    @pyqtSlot(name='on_action_python_script_triggered')
    def showPyScript(self):
        """Output to Python script for Jupyter notebook."""
        dlg = ScriptDialog(
            f"# Generate by Pyslvs v{_major}.{_minor}.{_build} ({_label})\n"
            f"# Project \"{self.DatabaseWidget.file_name.baseName()}\"\n" +
            slvs_process_script(
                tuple(vpoint.expr for vpoint in self.EntitiesPoint.data()),
                tuple((b, d) for b, d, a in self.InputsWidget.inputPairs())
            ),
            Python3Lexer(),
            "Python script",
            ["Python3 Script (*.py)"],
            self
        )
        dlg.show()
        dlg.exec_()

    @pyqtSlot(name='on_action_check_update_triggered')
    def checkUpdate(self):
        """Check for update."""
        progress_dlg = QProgressDialog("Checking update ...", "Cancel", 0, 3, self)
        progress_dlg.setAttribute(Qt.WA_DeleteOnClose)
        progress_dlg.setWindowTitle("Check for update")
        progress_dlg.resize(400, progress_dlg.height())
        progress_dlg.setModal(True)
        progress_dlg.show()
        url = check_update(progress_dlg)
        if not url:
            QMessageBox.information(
                self,
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
        if not self.DatabaseWidget.changed:
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
            return self.DatabaseWidget.changed
        elif reply == QMessageBox.Discard:
            return False
        return True

    def restoreSettings(self):
        """Restore Pyslvs settings."""
        for widget, value in self.__settings():
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
            if ARGUMENTS.kernel == "python_solvespace":
                kernel_name = kernel_list[1]
            elif ARGUMENTS.kernel == "sketch_solve":
                kernel_name = kernel_list[2]
            else:
                # pyslvs
                kernel_name = kernel_list[0]
            self.planarsolver_option.setCurrentText(kernel_name)
            self.pathpreview_option.setCurrentText(kernel_name)

    def saveSettings(self):
        """Save Pyslvs settings (auto save when close event)."""
        if self.dontsave_option.isChecked():
            self.settings.clear()
            return
        for widget, value in self.__settings():
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
        for widget, value in self.__settings():
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
            self.DatabaseWidget.read(ARGUMENTS.file)
        elif suffix == 'slvs':
            self.__read_slvs(ARGUMENTS.file)
        else:
            print("Unsupported format has been ignore when startup.")

    @abstractmethod
    def commandReload(self, index: int) -> None:
        ...

    @abstractmethod
    def addTargetPoint(self) -> None:
        ...

    @abstractmethod
    def commit_branch(self) -> None:
        ...

    @abstractmethod
    def customizeZoom(self) -> None:
        ...
