#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            _�g��5�rA�/������`�o92v@5�����̊��������j�)���5��qǕv�!��<��$�f����&����/�Z���G��Pe�� �bP�ȸѮN��I�"��d�u�g�"""
from hashlib import sha256
print sha256(blob).hexdigest()