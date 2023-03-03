"""Password validator """

from abc import ABC, abstractmethod
from hashlib import sha1
from requests import get


class ValidationError(Exception):
    """Exception for validation error"""


class Validator(ABC):
    """Interface for validators"""
    @abstractmethod
    def __init__(self, text) -> None:
        """Force to implement __init__ method"""
    @abstractmethod
    def is_valid(self):
        """Force to implement is_valid method"""


class LengthValidator(Validator):
    """Validator that checks if password is long enough"""

    def __init__(self, text, min_length=8) -> None:
        self.text = text
        self.min_length = min_length

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: text is not valid because there it is too short

        Returns:
            bool: text is long enough
        """

        if len(self.text) >= self.min_length:
            return True

        raise ValidationError('Text is too short!!')


class HasNumberValidator(Validator):
    """Validator that checks if number appears in text"""

    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: text is not valid because there is no number in text

        Returns:
            bool: has number in text
        """
        for number in range(0, 10):
            if str(number) in self.text:
                return True

        raise ValidationError('Text must contain number!')


class HasSpecialCharactersValidator(Validator):
    """Validator that checks if special char appears in text"""

    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: text is not valid because there is no special char in text

        Returns:
            bool: has special char in text
        """
        if any([not character.isalnum() for character in self.text]):
            return True

        raise ValidationError('Text must contain special character!!')


class HasUpperCharacterValidator(Validator):
    """Validator that checks if upper letter appears in text"""

    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: text is not valid because there is no upper letter in text

        Returns:
            bool: has upper letter in text
        """
        if any([character.isupper() for character in self.text]):
            return True
        raise ValidationError('Text must contain upper letter!!')


class HasLowerCharacterValidator(Validator):
    """Validator that checks if lower letter appears in text"""

    def __init__(self, text) -> None:
        self.text = text

    def is_valid(self):
        """Checks if text is valid

        Raises:
            ValidationError: text is not valid because there is no lower letter in text

        Returns:
            bool: has lower letter in text
        """
        if any([character.islower() for character in self.text]):
            return True
        raise ValidationError('Text must contain lower letter!!')


class HaveIbeenPwndValidator(Validator):
    """Validator that checks if password is safe"""

    def __init__(self, password) -> None:
        self.password = password

    def is_valid(self):
        """Checks if password is valid

        Raises:
            ValidationError: password is not valid because there it is present in some leak

        Returns:
            bool: password is safe
        """
        list_with_hash = []
        hash_of_password = sha1(
            self.password.encode('utf-8')).hexdigest().upper()
        list_with_hash.append(hash_of_password[5:])
        response = get('https://api.pwnedpasswords.com/range/' +
                       hash_of_password[:5])

        list_with_download_hash = []
        for line in response.text.splitlines():
            # print(line)
            found_hash, _ = line.split(':')
            list_with_download_hash.append(found_hash)

        for n in list_with_hash:
            for m in list_with_download_hash:
                if n == m:
                    raise ValidationError(
                        'This password is a leaked password! Choose another one!')


class PasswordValidator:
    """Password Validator
    """

    def __init__(self, password) -> None:
        self.password = password
        self.validators = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharactersValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HaveIbeenPwndValidator
        ]

    def is_valid(self):
        """Checks if password is valid

        Returns:
            bool: return true if password passed all requirements
        """
        for class_name in self.validators:
            validator = class_name(self.password)
            if validator.is_valid() is False:
                return False

        return True


with open('passwords.txt') as input_file, open('bezpieczne.txt', 'w') as output_file:
    for password in input_file:
        try:
            strip_password = password.strip()
            validator = PasswordValidator(strip_password)
            if validator.is_valid() is True:
                output_file.write(strip_password + '\n')
        except ValidationError as error:
            print(error)
