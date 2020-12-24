class customer:
    def __int__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
        print("customer created")


c = customer("caleb", "gold")
print(c.name, c.membership_type)

