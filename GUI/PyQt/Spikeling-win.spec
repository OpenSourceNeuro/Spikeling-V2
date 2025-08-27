# -*- mode: python ; coding: utf-8 -*-
import sys
from PySide6 import QtCore
import os

block_cipher = None

# Dynamically find Qt plugin path (for PySide6)
qt_plugins = os.path.join(QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Spikeling.ico', '.'), (qt_plugins, 'PySide6/Qt/plugins')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['PySide6.QtQml',
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
    'PySide6.QtTest'],
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
    upx=True,
    runtime_tmpdir=None,
    console=False,
    icon='Spikeling.ico',
)
