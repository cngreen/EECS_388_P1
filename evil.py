#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��|���J��=h�D��"O� �4�|U���O���H�K���H���*Fov�}�=_J�'���>o���g/xea��2�Qt�֍Ƙ1�.��Zn���mFe>��҈jh7x����V�~��>��V"""

from hashlib import sha256

if sha256(blob).hexdigest() == "78dc5a283968d554fa72e6722f9ff99ea378543709c2bc7b6e56e2ca8f657d41":
	print "I come in peace."
else:
	print "Prepare to be destroyed!"
