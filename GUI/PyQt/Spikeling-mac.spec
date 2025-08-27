# -*- mode: python ; coding: utf-8 -*-
import os
from PySide6 import QtCore
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

# Only include essential Qt plugins: platforms + imageformats
qt_plugins = []
plugin_path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath)
for plugin_type in ['platforms', 'imageformats']:
    src = os.path.join(plugin_path, plugin_type)
    if os.path.exists(src):
        qt_plugins.append((src, os.path.join('PySide6/Qt/plugins', plugin_type)))

# Collect only PySide6 data files (excluding Python source)
pyside6_data = collect_data_files('PySide6', include_py_files=False)

# Minimal hidden imports based on actual usage
hidden_imports = [
    'PySide6.QtCore',
    'PySide6.QtGui',
    'PySide6.QtWidgets'
]

a = Analysis(
    ['main.py'],
    pathex=[os.path.abspath('.')],  # project root
    binaries=[],
    datas=[('Spikeling.icns', '.')] + qt_plugins + pyside6_data,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'PySide6.QtQml',
        'PySide6.QtQuick',
        'PySide6.QtQuickControls2',
        'PySide6.QtQmlModels',
        'PySide6.QtWebEngine',
        'PySide6.QtWebEngineCore',
        'PySide6.QtWebEngineWidgets',
        'PySide6.QtBluetooth',
        'PySide6.QtLocation',
        'PySide6.QtPositioning',
        'PySide6.QtMultimedia',
        'PySide6.QtMultimediaWidgets',
        'PySide6.QtSensors',
        'PySide6.QtSql',
        'PySide6.QtSvg',
        'PySide6.QtUiTools',
        'PySide6.QtWebSockets',
        'PySide6.QtXml',
        'PySide6.QtXmlPatterns',
        'PySide6.QtTest'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Spikeling',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    noupx=True,                 # Disable UPX for PySide6 binaries
    runtime_tmpdir=None,
    console=False,
    icon='Spikeling.icns',
)
