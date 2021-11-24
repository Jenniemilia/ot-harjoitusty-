from entities.store import Store

from repositories.store_repository import store_repository

class UserInputError(Exception):
    pass


class StoreService:
    def __init__(self, store_repository):
        self._user = None
        self._store_repository = store_repository


    def register(self, storenumber, password, password_confirmation, login = True):

        """Rekisteröi uuden myymälän."""

        self.validate(storenumber, password, password_confirmation)

        store = self._store_repository.create_new(
            Store(storenumber, password)
        )

        if login:
            self._store = store

        return store

    def validate(self, storenumber, password, password_confirmation):
        if not storenumber or not password:
            raise UserInputError("You need to insert valid storenumber and password")

        if len(password) < 8:
            raise UserInputError("Password too short")

        if password != password_confirmation:
            raise UserInputError("Passwords don't match")
            
        if storenumber == ('^[0-9]+$'):
            raise UserInputError("Storenumber can only contain numbers 0-9")

        if password == ('[^a-z]'):
            raise UserInputError("Password should not contain only characters a-z")       
        

    def login(self, storenumber, password):

        self._storenumber = storenumber

        return storenumber

    def logout(self):
        self._store = None

store_service = StoreService(store_repository)