import pytest

def not_negitive_number (a:float):
    if a > 0:
        return True
    else:
        return False

@pytest.mark.parametrize("a, expected_result", [(-0.01 , False),
                                                   (0, False),
                                                (0.01, True)])
def test_not_negitive_number(a, expected_result):
    assert not_negitive_number(a) == expected_result

@pytest.mark.parametrize("a, expected_result", [("2" , TypeError)])

def test_type_error_for_not_negative_number(a, expected_result):
    with pytest.raises(expected_result):
        assert not_negitive_number(a)

def list_addition (list1:list, list2:list):
    return list1 + list2

@pytest.mark.parametrize("list1, list2, expected_result", [(["one", "two"] , ["three"], ["one", "two", "three"]),
                                                           (["one"] , ["two", "three"], ["one", "two", "three"])])

def test_list_addition(list1, list2, expected_result):
    assert list_addition(list1, list2) == expected_result


@pytest.mark.parametrize("list1, list2, expected_result", [(["one", "two", "three"] , 1, TypeError),
                                                   (1, ["one", "two", "three"], TypeError)
                                                ])
def test_type_error_for_list_addition(list1, list2, expected_result):
    with pytest.raises(expected_result):
        assert list_addition(list1, list2)

def an_association_tuple(tuple1:tuple, tuple2:tuple):
    return tuple1 + tuple2

@pytest.mark.parametrize("tuple1, tuple2, expected_result", [((1, 2) , (3, 4), (1, 2, 3, 4))])

def test_an_association_tuple(tuple1, tuple2, expected_result):
    assert an_association_tuple(tuple1, tuple2) == expected_result

@pytest.mark.parametrize("tuple1, tuple2, expected_result", [((1, 2) , 3, TypeError),
                                                             (3, (1, 2), TypeError)])

def test_type_error_for_an_association_tuple(tuple1, tuple2, expected_result):
    with pytest.raises(expected_result):
        assert an_association_tuple(tuple1, tuple2)

