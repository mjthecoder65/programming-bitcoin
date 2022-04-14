from field_element import FieldElement


class TestFieldElement():
    def test_field_element_equality_return_false(self):
        field_element1 = FieldElement(7, 13)
        field_element2 = FieldElement(6, 13)

        assert (field_element1 == field_element2) == False

    def test_field_element_equality_return_true(self):
        field_element1 = FieldElement(7, 13)
        field_element2 = FieldElement(7, 13)
        assert (field_element1 == field_element2) == True

    def test_field_element_addition_return_true(self):
        field_element1 = FieldElement(7, 13)
        field_element2 = FieldElement(7, 13)
        expected = FieldElement(1, 13)

        assert (field_element1 + field_element2) == expected

    def test_field_element_substraction_return_true(self):
        field_element1 = FieldElement(10, 13)
        field_element2 = FieldElement(7, 13)
        expected = FieldElement(3, 13)
        assert (field_element1 - field_element2) == expected

    def test_field_element_multiplication(self):
        field_element1 = FieldElement(10, 13)
        field_element2 = FieldElement(7, 13)
        expected = FieldElement(5, 13)
        assert (field_element1 * field_element2) == expected

    def test_field_element_exponention(self):
        field_element = FieldElement(3, 13)
        res =  (field_element ** 3)
        expected = FieldElement(1, 13)
        assert res == expected


    


