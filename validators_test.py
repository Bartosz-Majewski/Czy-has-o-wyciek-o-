import pytest
from validators import (
    HasNumberValidator,
    HasSpecialCharactersValidator,
    HasUpperCharacterValidator,
    HasLowerCharacterValidator,
    LengthValidator,
    HaveIbeenPwndValidator,
    ValidationError,
    PasswordValidator
)

#  nie sprawdzamy w testach czy pojawil się false, tylko czy pojawil sie wyjątek

# pokazany sposob testowania z wykorzytsaniem tej flaszki w menu  w okolo 15 minucie


def test_if_has_number_validator_positive():
    # given
    validator = HasNumberValidator('a1bc')

    # when
    result = validator.is_valid()

    # then
    #  użycie is zamiast == sprawi, że 1 czy inna liczba != 0  lub 0 nie bedą odpowiednią True / False
    #  True będzie tylko wtedy gdy result = True
    assert result is True


def test_if_has_number_validator_negative():
    # given
    validator = HasNumberValidator('abc')

    # # when
    # result = validator.is_valid()

    # # then
    # assert result is False

    # when
    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain number!' in str(error.value)


def test_if_has_special_characters_validator_positive():
    # given
    validator = HasSpecialCharactersValidator('a!b#c')

    # when
    result = validator.is_valid()

    # then
    #  użycie is zamiast == sprawi, że 1 czy inna liczba != 0  lub 0 nie bedą odpowiednią True / False
    #  True będzie tylko wtedy gdy result = True
    assert result is True


def test_if_has_special_characters_validator_negative():
    # given
    validator = HasSpecialCharactersValidator('abc')

    # # when
    # result = validator.is_valid()

    # # then
    # assert result is False

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain special character!!' in str(error.value)


def test_if_has_upper_characters_validator_positive():
    # given
    validator = HasUpperCharacterValidator('aBc')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_if_has_upper_characters_validator_negative():
    # given
    validator = HasUpperCharacterValidator('abc')

    # # when
    # result = validator.is_valid()

    # # then
    # assert result is False

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain upper letter!!' in str(error.value)


def test_if_has_lower_characters_validator_positive():
    # given
    validator = HasLowerCharacterValidator('aBc')

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_if_has_lower_characters_validator_negative():
    # given
    validator = HasLowerCharacterValidator('ABC')

    # # when
    # result = validator.is_valid()

    # # then
    # assert result is False

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain lower letter!!' in str(error.value)


def test_if_length_validator_positive():
    # given
    validator = LengthValidator('12345678')

    # when
    result = validator.is_valid()

    # then
    assert result is True

    # given
    # deklaracja ze może mięc 3 znaki
    validator = LengthValidator('123', 3)

    # when
    result = validator.is_valid()

    # then
    assert result is True


def test_if_length_validator_negative():
    # given
    validator = LengthValidator('123')

    # # when
    # result = validator.is_valid()

    # # then
    # assert result is False

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text is too short!!' in str(error.value)

    # given
    # deklaracja ze może mięc 9 znaki
    validator = LengthValidator('12345678', 9)

    # # when
    # result = validator.is_valid()

    # # then
    # assert result is False

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text is too short!!' in str(error.value)


def test_have_i_been_pwnd_validator_positive(requests_mock):
    data = '2006F18D02A96FED3C2C766394D515CCB10:10\r\n054B3304560352BB17B35CF2D3FF89FD8FB:4'
    requests_mock.get('https://api.pwnedpasswords.com/range/ED5E3', text=data)
    validator = HaveIbeenPwndValidator('kacper123')
    assert validator.is_valid() is True


def test_have_i_been_pwnd_validator_negative(requests_mock):
    # text : kacper123
    # hash: ED5E32116F18D02A96FED3C2C766394D515CCB10
    data = '2116F18D02A96FED3C2C766394D515CCB10:10\r\n054B3304560352BB17B35CF2D3FF89FD8FB:4'

    # request mock sluży do przechwycenia zapytania do serwera i stworzenia wlasnej odpowiedzi
    # request.mock.get('adres,ktory ma przechwycic', text = 'to co ma zwrocic')
    # odpowiada responsem wiec text responsa musi byc usatwiony na data
    requests_mock.get('https://api.pwnedpasswords.com/range/ED5E3', text=data)
    validator = HaveIbeenPwndValidator('kacper123')
    # assert validator.is_valid() is False

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'This password is a leaked password! Choose another one!' in str(
            error.value)


def test_password_validator_negative():
    validator = PasswordValidator('adam8899#')

    with pytest.raises(ValidationError) as error:
        validator.is_valid()
        assert 'Text must contain upper letter!!' in str(error.value)


def test_password_validator_positive():
    validator = PasswordValidator('adam8899#A')
    assert validator.is_valid() is True
