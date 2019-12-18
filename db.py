import os
import hashlib
import binascii
from pymongo import MongoClient
from bson.objectid import ObjectId


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'),
                                  salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


class Users:
    """A class for storing Project related information"""
    def __init__(self, user_id=None, fname=None, email=None, password=None):
        if user_id is None:
            self._id = ObjectId()
        else:
            self._id = user_id
        self.fname = fname
        self.email = email
        self.password = hash_password(password)

    def get_as_json(self):
        """ Method returns the JSON representation of the Project object, which can be saved to MongoDB """
        return self.__dict__

    @staticmethod
    def build_from_json(json_data):
        """ Method used to build Project objects from JSON data returned from MongoDB """
        if json_data is not None:
            try:
                return Users(json_data.get('_id', None), json_data['fname'], json_data['email'], json_data['password'])
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e))
        else:
            raise Exception("No data to create Project from!")


class MainDataB:
    client = MongoClient(host='localhost', port=27000)
    database = client['users']

    def update(self, user):
        if user is not None:
            self.database.users.save(user.get_as_json())
        else:
            raise Exception("Nothing to update, because user parameter is None")

    def delete(self, user):
        if user is not None:
            self.database.users.remove(user.get_as_json())
        else:
            raise Exception("Nothing to delete, because user parameter is None")
