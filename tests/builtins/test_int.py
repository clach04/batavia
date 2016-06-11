from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class IntTests(TranspileTestCase):
    pass


class BuiltinIntFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["int"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_complex',
        'test_dict',
        'test_frozenset',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_set',
        'test_tuple',
    ]
