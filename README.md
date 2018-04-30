# Key Value Encoding

`kvencoder` is a very flexible key value encoding mechanism
that you can use to serialize any of your classes.

### Creating the class schema

The class schema is a YAML file, that describes which 
attributes to encode and how. It is a very flexible way
of writing structured data.

### Install

`pip install kvencoder/` - sorry, no PyPi yet.

### Use cases

`kvencoder` is being used in the biomolecular simulation package
BAC2 to encode classes to _very_ specific configuration 
file formats used by high performace MD engines like NAMD, 
Gromacs, Amber or OpenMM.
