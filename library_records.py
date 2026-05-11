class Lib:
    def __init__(self, t, a, y):
        self.t = t
        self.a = a
        self.y = y

    def show(self):
        print(f"Title: {self.t}, Author: {self.a}, Year: {self.y}")

lst = []

b1 = Lib("The Great Gatsby", "F. Scott Fitzgerald", 1925)
b2 = Lib("The Hobbit", "J.R.R. Tolkien", 1937)
b3 = Lib("1984", "George Orwell", 1949)

lst.append(b1)
lst.append(b2)
lst.append(b3)

for b in lst:
    b.show()