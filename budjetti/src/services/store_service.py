from entities.store import Store

class UserInputError(Exception):
    pass


class StoreService:
    def __init__(self):
        self.user = None


    def register(self, storenumber, password, password_confirmation, login = True):

        """Rekisteröi uuden myymälän."""

        self.validate(storenumber, password, password_confirmation)

        store = self._store_repository.create(
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
        

    def login(self, strorenumber, password):
        pass

    def logout(self):
        self._store = None

store_service = StoreService()