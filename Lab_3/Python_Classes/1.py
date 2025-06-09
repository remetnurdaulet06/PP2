class OutLine:
    def __init__(self):
        self.line = ""
    def get_str(self):
        self.line = input("Enter a string: ")
    def prin_tstr(self):
        return self.line.upper()
asd = OutLine()
asd.get_str()
print("Upper str:", asd.prin_tstr())