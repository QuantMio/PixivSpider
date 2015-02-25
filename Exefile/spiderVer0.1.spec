# -*- mode: python -*-
a = Analysis(['spiderVer0.1.py'],
             pathex=['H:\\Python\\PyInstaller-2.1\\PyInstaller-2.1\\spiderVer0.1'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='spiderVer0.1.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='spider.ico')
