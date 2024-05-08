import unittest
import os
import encrypt_decrypt as ed
import readwrite
import keys


class TestEncryptDecrypt(unittest.TestCase):
    def setUp(self):
        """
        Create temp directory for test files.
        """
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)

    def TearDown(self):
        """
        Remove temp directory and contents after testing.
        """
        if os.path.exists(self.test_dir):
            for file in os.listdir(self.test_dir):
                file_path = os.path.join(self.test_dir, file)
                os.remove(file_path)
            os.rmdir(self.test_dir)

    def test_encrypt_decrypt(self):
        # create test file with content
        test_filename = os.path.join(self.test_dir, "test.txt")
        test_content = b"This is a test."
        readwrite.write(test_filename, test_content)

        # generate key and IV
        key = keys.generate_key()
        iv = keys.generate_iv()

        # encrypt test file
        encrypted_filename = ed.encrypt(test_filename, "cbc", key, iv)
        # decrypt encrypted file
        decrypted_filename = ed.decrypt(encrypted_filename, "cbc", key, iv)

        # read decrypted content and verify that it matches the original content
        decrypted_content = readwrite.read(decrypted_filename)
        self.assertEqual(decrypted_content, test_content)


if __name__ == "__main__":
    unittest.main()
