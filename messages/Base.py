class Base:

    instance = None

    def set_payload(self, payload):
        self.instance.ParseFromString(payload)
    
    def user(self):
        return self.instance.user

    def __str__(self):
        pass

