# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re


def elide_text(string, max):
    if len(string) <= max - 1:
        return string

    p = re.compile(
        r'^((?:[\ud800-\udbff][\udc00-\udfff]|.){' + str(max - 1) + '}).',
        re.UNICODE
    )

    m = p.match(string)
    if not m:
        return string

    return re.sub(r'…*$', r'…', m.group(1))
