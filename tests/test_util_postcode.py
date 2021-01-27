import unittest
import re

from app import util

class TestUtilPostcodeParseRegex(unittest.TestCase):
    def test_parses_regex(self):
        t_input = 'ABC XY1'
        output = util.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)
    
    def test_parses_regex_1(self):
        t_input = 'ABCXY1'
        output = util.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)
    
    def test_parses_regex_2(self):
        t_input = 'ABC-XY1'
        output = util.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)
    
    def test_parses_regex_3(self):
        t_input = 'ABC_XY1'
        output = util.parse_regex(t_input)

        self.assertIsInstance(output, re.Pattern)

    # bad inputs
    
    def test_handles_weird_characters(self):
        t_input = '^[&?-:]*$'
        output = util.parse_regex(t_input)

        self.assertIsNone(output)

    def test_ignores_bad_input(self):
        t_input = 'ABC XY1 UUA'
        output = util.parse_regex(t_input)

        self.assertIsNone(output)
    
    def test_ignores_bad_input_2(self):
        t_input = ''
        output = util.parse_regex(t_input)

        self.assertIsNone(output)

    def test_ignores_bad_input_3(self):
        t_input = '   '
        output = util.parse_regex(t_input)

        self.assertIsNone(output)


class TestUtilPostcodeMatch(unittest.TestCase):
    def test_matches_basic_postcode(self):
        matcher = util.parse_regex('abc 123')
        output = util.postcode_match(matcher, 'abc 123')
        self.assertIs(output, True)

    def test_matches_basic_postcode_2(self):
        matcher = util.parse_regex('abc123')
        output = util.postcode_match(matcher, 'abc 123')
        self.assertIs(output, True)
    
    def test_matches_basic_postcode_3(self):
        matcher = util.parse_regex('abc')
        output = util.postcode_match(matcher, 'abc 123')
        self.assertIs(output, True)
    
    def test_misses_non_match(self):
        matcher = util.parse_regex('xyz 123')
        output = util.postcode_match(matcher, 'abc 123')
        self.assertIs(output, False)


