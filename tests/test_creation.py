# Modules
import os
import sys
import inspect

# move directory to parent 
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from metlink import metlink

def test_creation():
    """ Tests the main class object is instantiable """
    metlink_obj = metlink()
    assert metlink_obj