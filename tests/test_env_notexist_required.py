import os, sys, pytest

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_notexist_required():
    os.environ['APP_ENV'] = 'notexist'

    with pytest.raises(Exception) as exinfo:
        import dotenv_switch as ds
        ds.load(required=True)

    # This is a little unconventional - normal way to check the exception type
    # would be inside the pytest.raises() directly, but to load that type into this
    # scope means we would need to import it, and that messes up the execution environment
    # setup by importing dotenv_switch as part of the process that has to throw
    # the exception we test. Maybe there's a better way.
    from dotenv_switch.exceptions import DotenvSwitchFileNotFoundError
    assert exinfo.type == DotenvSwitchFileNotFoundError
