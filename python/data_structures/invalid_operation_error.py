class InvalidOperationError(Exception):
    """Raised when the user tries to perform an invalid operation on an empty stack."""
    def __init__(self, value="Method not allowed on empty collection"):
        self.value = value

    def __str__(self):
        return self.value
