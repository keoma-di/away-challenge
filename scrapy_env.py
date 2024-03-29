#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022-08-25 neo_nguyen
#

from __future__ import print_function

import difflib


def compare(str1, str2):
    a = str1.splitlines()
    b = str2.splitlines()
    d = difflib.Differ()
    diff = d.compare(a, b)
    print('\n'.join(diff))
