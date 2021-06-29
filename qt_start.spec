# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import sys
sys.setrecursionlimit(5000)
a = Analysis(['qt_start.py'],
             pathex=['.\\mainwindow.py', '.\\polya.py', '.\\hexahedro.jpg', '.\\octahedro.jpg', '.\\tetrahedro.jpg', 'D:\\software\\pycharm\\pycharm_code\\class_work\\polya'],
             binaries=[],
             datas=[('.\\picture','.\\picture')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='qt_start',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
