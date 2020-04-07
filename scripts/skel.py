#!/usr/bin/env python3

# The skel program provides a simple, general-purpose
# generative programming mechanism
# Note: this code has itself been generated

from Cheetah.Template import Template
import json
#import sys


def generate(config):

  models = {}
  instantiated_templates = {}

  if config.subcommand == "template":

    modelargs = config.modelfile  
    for argpair in modelargs.split(','):
      with open (argpair.split(':')[0], "r") as clfile:   
        models[argpair.split(':')[1]] = json.load(clfile) 

    # Process the  template
    t = Template(file=config.template)
    t.models = models
    t.instantiated_templates = instantiated_templates

    # Instantiate template
    instantiated_templates[config.outfile] = str(t)

    with open (config.outfile, 'w') as outfile:
      outfile.write(instantiated_templates[config.outfile])

import argparse

def commandline (argv):
  parser = argparse.ArgumentParser(prog='skel')
  subparsers = parser.add_subparsers(help='sub help', dest="subcommand")

  _parser_template = subparsers.add_parser('template', help="todo: add subparser help")
  _parser_template.add_argument('template')
  _parser_template.add_argument('--model', dest="modelfile", required="true")
  _parser_template.add_argument('--outfile', dest="outfile", required="true")

  return (parser.parse_args(argv[1:])) # Skip the program name, and pass the rest to the parser

def main(argv):
    config = commandline(argv)
    print (config)
    generate(config)


