import unittest
import bcrypt
class TestPassword(unittest.TestCase):

    def test_password_bcrypt(self):
        password = "hej"
        byte_password = str.encode(password)
        hashed_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())

        self.assertTrue( checkPasswordBcrypt(str.encode("hej"), hashed_password) )
        self.assertFalse( checkPasswordBcrypt(str.encode("hejsan"), hashed_password) )

def checkPasswordBcrypt(psw, hashed_psw):
    if bcrypt.checkpw(psw, hashed_psw):
        return True
    else:
        return False
if __name__ == '__main__':
    unittest.main()
