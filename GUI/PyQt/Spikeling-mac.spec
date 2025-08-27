# -*- mode: python ; coding: utf-8 -*-
import sys
from PySide6 import QtCore
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

# Qt plugins: only include essential types (platforms + imageformats)
qt_plugins = []
plugin_path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath)

for plugin_type in ['platforms', 'imageformats']:
    src = os.path.join(plugin_path, plugin_type)
    if os.path.exists(src):
        qt_plugins.append((src, os.path.join('PySide6/Qt/plugins', plugin_type)))

# Collect essential PySide6 hidden imports
hidden_imports = collect_submodules('PySide6')

a = Analysis(
    ['main.py'],
    pathex=[os.path.abspath('.')],  # explicit path to reduce scanning
    binaries=[],
    datas=[('Spikeling.icns', '.')] + qt_plugins,
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
    noupx=True,                 # explicitly disable UPX for safety
    runtime_tmpdir=None,
    console=False,
    icon='Spikeling.icns',
)
