#!/usr/bin/env python3

# The skel program provides a simple, general-purpose
# generative programming mechanism
# Note: this code has itself been generated

from Cheetah.Template import Template
import json
#import sys



#used by make_instance
def expand (field_type, schema):
#    print ("Expand@@@")
#    print (field_type)
    if field_type == "int":
        return 123
    elif field_type == "string":
        return "abc"
    # Handle other primitives here
    else: # Assume this type is in the schema definition
        type = schema['types'][field_type] # Lookup type in the schema
        #probably need some error checking for that last one
        if type['type'] == "dict":
            rv = {}
            for field in type['fields']:
                rv[field['name']] = expand (field['type'], schema)
            return rv
        elif type['type'] == "list":
            rv = []
            for i in range(3):
                rv.append(expand(type['element_type'], schema))
            return rv
        else:
            print ("Unknown object type {}".format(type['type']) )
            quit()

def process(config):

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

    if config.arg:
        name, value = config.arg.split(':')
        t.arg = {}
        t.arg[name] = value

    t.instantiated_templates = instantiated_templates

    # Instantiate template
    instantiated_templates[config.outfile] = str(t)

    with open (config.outfile, 'w') as outfile:
      outfile.write(instantiated_templates[config.outfile])
    return

  if config.subcommand =="make_instance":
      out_dict = {}
      with open (config.schemafile, 'r') as schema_in:
          schema = json.load(schema_in)
#          print (schema)
          for field in schema["fields"]:
              out_dict[field['name']] = expand (field['type'], schema)
#          print (out_dict)
          with open (config.outfile, 'w') as instance_out:
              json.dump(out_dict, instance_out, indent=4)

import argparse

def commandline (argv):
  parser = argparse.ArgumentParser(prog='skel')
  subparsers = parser.add_subparsers(help='sub help', dest="subcommand")

  _parser_template = subparsers.add_parser('template', help="Instantiate a template using one or more named models")
  _parser_template.add_argument('template')
  _parser_template.add_argument('--model', dest="modelfile", required="true")
  _parser_template.add_argument('--outfile', dest="outfile", required="true")
  _parser_template.add_argument('--arg', dest="arg", required=False)

  _parser_template = subparsers.add_parser('make_instance', help="Create an instance of a given schema suitable for testing")
  _parser_template.add_argument('--schema', dest="schemafile", required="true")
  _parser_template.add_argument('--outfile', dest="outfile", required="true")

  return (parser.parse_args(argv[1:])) # Skip the program name, and pass the rest to the parser

def main(argv):
    config = commandline(argv)
    print (config)
    process(config)


