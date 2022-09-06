from ..main import Metlink


def test_creation():
    """ Tests the main class object is instantiable """
    metlink_obj = Metlink('abnaisfubas')
    assert metlink_obj is not None
