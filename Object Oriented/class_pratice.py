class snake():
    def __init__(self,name):
        self.name=name
    def change_name(self,change_name):
        self.change_name=change_name
a1=snake("Nilesh")
print(a1.name)
a2=snake("Bartakke")
print(a2.name)
a2.change_name="Hi friend"
print(a2.change_name)