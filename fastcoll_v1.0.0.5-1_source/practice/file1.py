#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            _�g��5�rA�/��������o92v@5�����̊������C�j�)���5��qG�v�!��<��$�f����&��b�/�Z���G��Pe�� �bP��8ҮN��I�"��d�u=g�"""
from hashlib import sha256
print sha256(blob).hexdigest()