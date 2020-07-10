# skel-core
Contains the core skel libraries and skel command line tool. Skel has been greatly simplified from previous versions, and I/O specific modules have been moved to a [separate area](https://github.com/isosc/skel-io).


## Installing skel
Skel is arranged as an installable python package. Simply clone the github repository, navigate to the top-level directory, and use ```pip install .```

## Using skel
Most uses of skel will involve the skel template command:

```usage: skel template [-h] --model MODELFILE:MODELNAME[,MODELFILE:MODELNAME] --outfile OUTFILE template```

Skel will instantiate the given template using specified model(s) to produce OUTFILE. Note that models must be named, as in the following example:
  
```skel template --model mymodel.json:mymodel --outfile generated_code.c code_template.tmpl```
  
