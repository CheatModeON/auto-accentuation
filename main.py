#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyboard

    
keyboard.add_abbreviation('aa', 'ά'.decode('utf-8'))
keyboard.add_abbreviation('ee', 'έ'.decode('utf-8'))
keyboard.add_abbreviation('hh', 'ή'.decode('utf-8'))
keyboard.add_abbreviation('ii', 'ί'.decode('utf-8'))
keyboard.add_abbreviation('oo', 'ό'.decode('utf-8'))
keyboard.add_abbreviation('yy', 'ύ'.decode('utf-8'))
keyboard.add_abbreviation('vv', 'ώ'.decode('utf-8'))


keyboard.add_abbreviation('iii', 'ϊ'.decode('utf-8'))
keyboard.add_abbreviation('yyy', 'ϋ'.decode('utf-8'))


keyboard.add_abbreviation('iiii', 'ΐ'.decode('utf-8'))
keyboard.add_abbreviation('yyyy', 'ΰ'.decode('utf-8'))


# Block forever, like `while True`.
keyboard.wait()

