class Book:
    def __init__(self, author, title):
        self.author = author

    def display(self):
        print(f"The book Author is {self.author}")


if __name__ == "__main__":
    print("This is assignment 1 part 2")
    print("More Changes")

    a = Book("Thorpe", "Beat the Dealer")
    a.display()
