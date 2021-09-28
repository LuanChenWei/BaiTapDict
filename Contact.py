

class Contact:
    def __init__(self, name="", phones=[], emails=[], address="", note="", tags=[]):
        self.name = name
        self.phones = phones
        self.emails = emails
        self.address = address
        self.note = note
        self.tags = tags

    def set_name(self, name):
        self.name = name
    def set_phones(self, phones):
        self.phones = phones
    def set_emails(self, emails):
        self.emails = emails
    def set_address(self, address):
        self.address = address
    def set_note(self, note):
        self.note = note
    def set_tags(self, tags):
        self.tags = tags

    def get_info(self):
        

