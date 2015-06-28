
from nose.tools import *
import logfind

def setup():
    pass

def teardown():
    pass

def test_read_important_files_from_dotlogfind():
    # arrange
    lf = logfind.Logfind()

    # act
    patterns = lf.read_dot_logfind()

    # assert
    assert_equal(2, len(patterns))

def test_return_files_based_on_important_files_from_dotlogfind():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()

    # act
    log_files = lf.get_log_files(patterns)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))

def test_can_return_logfiles_that_contain_text():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()
    log_files = lf.get_log_files(patterns)
    text = 'important'

    # act
    matches = lf.read_log_files(log_files, text)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))
    assert_equal(1, len(matches))

def test_returns_logfiles_that_contain_all_text():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()
    log_files = lf.get_log_files(patterns)
    text = 'some important text'

    # act
    matches = lf.read_log_files(log_files, text)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))
    assert_equal(1, len(matches))

def test_does_not_return_logfiles_that_do_not_contain_all_text():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()
    log_files = lf.get_log_files(patterns)
    text = 'important files'

    # act
    matches = lf.read_log_files(log_files, text)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))
    assert_equal(0, len(matches))

def test_returns_logfiles_when_treating_text_separation_as_or():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()
    log_files = lf.get_log_files(patterns)
    text = 'important files'

    # act
    matches = lf.read_log_files(log_files, text, treat_as_or=True)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))
    assert_equal(2, len(matches))


def test_returns_logfiles_when_passing_in_regex():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()
    log_files = lf.get_log_files(patterns)
    text = r'.*?\bimportant\b.*? file'

    # act
    matches = lf.read_log_files(log_files, text, treat_as_or=True)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))
    assert_equal(1, len(matches))

def test_returns_logfile_when_passing_in_text_using_and_logic():
    # arrange
    lf = logfind.Logfind()
    patterns = lf.read_dot_logfind()
    log_files = lf.get_log_files(patterns)
    text = r'very long files'

    # act
    matches = lf.read_log_files(log_files, text)

    # assert
    assert_equal(2, len(patterns))
    assert_equal(2, len(log_files))
    assert_equal(1, len(matches))