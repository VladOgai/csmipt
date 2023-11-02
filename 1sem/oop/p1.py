class Bibaboba:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        self.output()

    def output(self):
        if type(self.in1) == type(self.in2):
            print(self.in1 + self.in2)
        else:
            print('Input types mismatch')