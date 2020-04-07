from unittest import TestCase
from scripts import skel
import argparse
import os

class TestSkelCL(TestCase):
    def test_simple(self):
        modelfile = "{0}/input/test_model.json:test,{0}/input/test_model2.json:test2".format(os.path.dirname(os.path.abspath(__file__)))
        templatefile = "{}/input/test_template_multiple.tmpl".format(os.path.dirname(os.path.abspath(__file__)))
        skel.main(['skel', 'template', '--model', modelfile, '--outfile', 'test_out.txt', templatefile])
        with open('test_out.txt', 'r') as test_out:
            content = test_out.read()
            self.assertEqual(content, 'ABCDEF')

