# -*- mode: python -*-
a = Analysis(['spiderVer0.11.py'],
             pathex=['H:\\Python\\PyInstaller-2.1\\spiderVer0.11'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='spiderVer0.11.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='spider.ico')
