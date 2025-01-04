class Bread:
    def __init__(self):
        self.bread = None
        self.toast = None
        self.butter = None
        self.texture = None
    def bread_flavor(self, option):
        if option == "1":
            self.bread = "Whole Wheat Bread"
        elif option == "2":
            self.bread = "Italian Bread"
        else:
            raise Exception("Please select a valid option")
    def toasted(self, option):
        if option == "1":
            self.toast = f"Toast the {self.bread}"
        elif option == "2":
            self.toast = f"Don't toast the {self.bread}"
        else:
            raise Exception("Please select a valid option")
    def buttered(self, option):
        if option == "1":
            self.butter = f"Butter the {self.bread}"
        elif option == "2":
            self.butter = f"Don't butter the {self.bread}"
        else:
            raise Exception("Please select a valid option")  
    def textures(self, option):
        if option == "1":
            self.texture = f"Make the {self.bread}, fluffy"
        elif option == "2":
            self.texture = f"Make the {self.bread}, flat"
        else:
            raise Exception("Please select a valid option")  
    def __str__(self):
        return f"{self.bread}\n{self.toast}\n{self.butter}\n{self.texture}"
run = Bread()
run.bread_flavor("1")
run.toasted("1")
run.buttered("1")
run.textures("1")
print(run)