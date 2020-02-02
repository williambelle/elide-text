# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from elidetext import elide_text


def test_elide_text():
    assert elide_text('TS', 5) == 'TS'
    assert elide_text('tretrwetre', 5) == 'tret…'
    assert elide_text('🚲🚙💵👩💧🐟🕘', 5) == '🚲🚙💵👩…'
