#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...
    def test_constructor(self):
    	self.assertRaises(TypeError, textproc.__init__, 5)

    def test_count(self):
    	self.assertEqual(textproc.Processor("123").count(), 3)

    def test_count_alpha(self):
    	self.assertEqual(textproc.Processor("123abc").count_alpha(),3)	

    def test_count_numeric(self):
    	self.assertEqual(textproc.Processor("1234abc").count_numeric(),4)

    def test_count_vowels(self):
    	self.assertEqual(textproc.Processor("abcde").count_vowels(),2)

    def test_is_phonenumber(self):
    	self.assertTrue(textproc.Processor("303-303-3030").is_phonenumber(), True)
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
