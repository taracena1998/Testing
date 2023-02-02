import main


class TestFloats:
    def setup(self):
        print('\nthis is setup')

    def teardown(self):
        print('\nthis is teardown')
    def setup_class(cls):
        print('\tthis is setup class')

    def teardown_class(cls):
        print('\tthis is teardown class')

    def test_rounds_down(self):
        result = main.str_to_int('1.99')
        assert result == 1

    def test_float_round_lesser_half(self):
        result = main.str_to_int('1.2')
        assert result == 1
