"""aaa"""
import os
import secrets


class SecretKeyGenerator:
    """The class checks if secret token already exists, otherwise is created.

    Parameters
    ----------
    secret_file_path: str, default '.'
        Path used to save the file with the secret key
    secret_key_file: str, default '.service_secret_key'
        Secret key file name
    secret_key_length: int, default 16
        Secret key length
    """

    def __init__(
        self,
        secret_file_path: str = ".",
        secret_key_file: str = ".service_secret_key",
        secret_key_length: int = 16,
    ):
        """The init method is involved to populate the required objects"""
        self.secret_file_path = secret_file_path
        self.secret_key_file = secret_key_file
        self.secret_key_length = secret_key_length
        self.secret_key_filename = os.path.join(self.secret_file_path, self.secret_key_file)

    def __str__(self):
        """The __str__ method return the class description"""
        class_doc = """The class checks if secret token already exists, otherwise is created.

        Parameters
        ----------
        secret_file_path: str, default '.'
            Path used to save the file with the secret key
        secret_key_file: str, default '.service_secret_key'
            Secret key file name
        secret_key_length: int, default 16
            Secret key length
        """
        return class_doc

    def create_secret_key(self) -> str:
        """The method generate a secret key

        Returns
        -------
        secret_key : str
            The secret key with the required length
        """
        return secrets.token_hex(self.secret_key_length)

    def check_secret_key(self) -> bool:
        """The method check if a secret key file exists

        Returns
        -------
        secret_key_check : bool
            True if a secret file exists, False otherwise
        """
        secret_key_check = os.path.isfile(self.secret_key_filename)
        if secret_key_check:
            with open(self.secret_key_filename, encoding="utf-8") as f:
                secret_key_check = len(f.readline()) > 0
        return secret_key_check

    def write_secret_key(self, secret_key: str):
        """The method write a secret key file"""
        with open(self.secret_key_filename, "w", encoding="utf-8") as f:
            f.write(secret_key)

    def get_secret_key(self):
        """The method check get the secret key from the file

        Returns
        -------
        secret_key : str
            The secret key retrieved from the file
        """
        with open(self.secret_key_filename, encoding="utf-8") as f:
            secret_key = f.readline()
        return secret_key

    def main(self):
        """The method is involved to executes all the following methods:

        1. Verify if a secret key file exists.
        2. If exists, return the file secret key.
        3. Otherwise:
            a. Create a secret key
            b. Write a file with the created secret key
            c. Return  the created secret key

        Returns
        -------
        secret_key : str
            The secret key retrieved from the file
        """
        if not self.check_secret_key():
            secret_key = self.create_secret_key()
            self.write_secret_key(secret_key)
        else:
            secret_key = self.get_secret_key()
        return secret_key


if __name__ == "__main__":
    # The SecretKeyGenerator class is initialized
    secret_key_generator = SecretKeyGenerator()

    # The main method is called
    print(secret_key_generator.main())
