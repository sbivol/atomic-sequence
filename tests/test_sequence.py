from assertpy import assert_that

from atomic import Sequence


def test_get_set():
    sequence = Sequence(0)

    sequence.set(10)

    assert_that(sequence.get()).is_equal_to(10)


def test_increment_and_get():
    sequence = Sequence(0)

    new_value = sequence.increment_and_get(10)

    assert_that(new_value).is_equal_to(10)


def test_get_and_increment():
    sequence = Sequence(0)

    old_value = sequence.get_and_increment(10)
    new_value = sequence.get()

    assert_that(old_value).is_equal_to(0)
    assert_that(new_value).is_equal_to(10)
