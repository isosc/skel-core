from unittest import TestCase
from scripts import skel
import argparse
import os

class TestSkelCL(TestCase):
    def test_simple(self):
        modelfile = "{}/input/test_model.json:test".format(os.path.dirname(os.path.abspath(__file__)))
        templatefile = "{}/input/test_template.tmpl".format(os.path.dirname(os.path.abspath(__file__)))
        skel.main(['skel', 'template', '--model', modelfile, '--outfile', 'test_out.txt', templatefile])
        with open('test_out.txt', 'r') as test_out:
            content = test_out.read()
            self.assertEqual(content, 'ABC')

