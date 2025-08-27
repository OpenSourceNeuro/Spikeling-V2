# -*- mode: python ; coding: utf-8 -*-
import sys
from PySide6 import QtCore
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

# Dynamically find Qt plugin path
qt_plugins = os.path.join(QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.PluginsPath))

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Spikeling.icns', '.'), (qt_plugins, 'PySide6/Qt/plugins')],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
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
    icon='Spikeling.icns',
)
