class TooRequests(Exception):
    def __init__(self, status: str = None, dev_message: str = None):
        super().__init__(status, dev_message)

        self.status = status
        self.dev_message = dev_message
    
    def __str__(self):
        return (
            "Rubika API Exception: "
            "status: {} | dev-message: {}".format(self.status, self.dev_message)
        )