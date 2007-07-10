# -*- coding: utf-8 -*-
# pytils - simple processing for russian strings
# Copyright (C) 2006-2007  Yury Yurevich
#
# http://www.pyobject.ru/projects/pytils/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, version 2
# of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
"""
Unit tests for pytils' dt templatetags for Django web framework
"""

__id__ = __revision__ = "$Id$"
__url__ = "$URL$"

import datetime
from pytils.test.templatetags import helpers

class DtDefaultTestCase(helpers.TemplateTagTestCase):
    
    def setUp(self):
        self.date = datetime.datetime(2007, 1, 26, 15, 50)
        self.date_before = datetime.datetime.now() - datetime.timedelta(1, 2000)
    
    def testLoad(self):
        self.check_template_tag('load_tag', '{% load pytils_dt %}', {}, '')
    
    def testRuStrftimeFilter(self):
        self.check_template_tag('ru_strftime_filter', 
            '{% load pytils_dt %}{{ val|ru_strftime:"%d %B %Y, %A" }}', 
            {'val': self.date},
            '26 января 2007, пятница')
    
    def testRuStrftimeInflectedFilter(self):
        self.check_template_tag('ru_strftime_inflected_filter', 
            '{% load pytils_dt %}{{ val|ru_strftime_inflected:"в %A, %d %B %Y" }}', 
            {'val': self.date},
            'в пятницу, 26 января 2007')
    
    def testRuStrftimePrepositionFilter(self):
        self.check_template_tag('ru_strftime_preposition_filter', 
            '{% load pytils_dt %}{{ val|ru_strftime_preposition:"%A, %d %B %Y" }}', 
            {'val': self.date},
            'в\xc2\xa0пятницу, 26 января 2007')
    
    def testDistanceFilter(self):
        self.check_template_tag('distance_filter', 
            '{% load pytils_dt %}{{ val|distance_of_time }}', 
            {'val': self.date_before},
            'вчера')
        
        self.check_template_tag('distance_filter', 
            '{% load pytils_dt %}{{ val|distance_of_time:3 }}', 
            {'val': self.date_before},
            '1 день 0 часов 33 минуты назад')
    
    # без отладки, если ошибка -- по умолчанию пустая строка
    def testRuStrftimeError(self):
        self.check_template_tag('ru_strftime_error', 
            '{% load pytils_dt %}{{ val|ru_strftime:"%d %B %Y" }}', 
            {'val': 1}, 
            '')


if __name__ == '__main__':
    import unittest
    unittest.main()
