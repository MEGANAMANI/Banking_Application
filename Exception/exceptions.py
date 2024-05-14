class InsufficientFundException(Exception):
    def __init__(self):
        super().__init__("Insufficient Funds")


class InvalidAccountException(Exception):
    def __init__(self):
        super().__init__("Invalid Account information")


class OverDraftLimitExcededException(Exception):
    def __init__(self):
        super().__init__("OverDraft Limit Exceeded")

class CustomerNotFoundException(Exception):
    def __init__(self):
        super().__init__("No customer found")