import unittest
import re

import app.lib.postcode as postcode

class TestUtilPostcodeParseRegex(unittest.TestCase):
    def test_parses_regex(self):
        t_input = 'ABC XY1'
        output = postcode.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)
    
    def test_parses_regex_1(self):
        t_input = 'ABCXY1'
        output = postcode.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)
    
    def test_parses_regex_2(self):
        t_input = 'ABC-XY1'
        output = postcode.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)
    
    def test_parses_regex_3(self):
        t_input = 'ABC_XY1'
        output = postcode.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)

    # bad inputs
    
    def test_handles_weird_characters(self):
        t_input = '^[&?-:]*$'
        output = postcode.parse_regex(t_input)

        self.assertIsNone(output)

    def test_ignores_bad_input(self):
        t_input = 'ABC XY1 UUA'
        output = postcode.parse_regex(t_input)

        self.assertIsNone(output)
    
    def test_ignores_bad_input_2(self):
        t_input = ''
        output = postcode.parse_regex(t_input)

        self.assertIsNone(output)

    def test_ignores_bad_input_3(self):
        t_input = '   '
        output = postcode.parse_regex(t_input)

        self.assertIsNone(output)


class TestUtilPostcodeMatch(unittest.TestCase):
    def test_matches_basic_postcode(self):
        matcher = postcode.parse_regex('abc 123')
        output = postcode.postcode_match(matcher, 'abc 123')
        self.assertIs(output, True)

    def test_matches_basic_postcode_2(self):
        matcher = postcode.parse_regex('abc123')
        output = postcode.postcode_match(matcher, 'abc 123')
        self.assertIs(output, True)
    
    def test_matches_basic_postcode_3(self):
        matcher = postcode.parse_regex('abc')
        output = postcode.postcode_match(matcher, 'abc 123')
        self.assertIs(output, True)
    
    def test_misses_non_match(self):
        matcher = postcode.parse_regex('xyz 123')
        output = postcode.postcode_match(matcher, 'abc 123')
        self.assertIs(output, False)


