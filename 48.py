class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print("Status: Checked Out" if self.checked_out else "Status: Available")

    def check_out(self):
        if not self.checked_out:
            print(f"Checking out {self.title}")
            self.checked_out = True
        else:
            print(f"{self.title} is already checked out")

    def check_in(self):
        if self.checked_out:
            print(f"Checking in {self.title}")
            self.checked_out = False
        else:
            print(f"{self.title} is already checked in")


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        print("Book Information:")
        super().display_info()
        print(f"Author: {self.author}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director):
        super().__init__(title, item_id)
        self.director = director

    def display_info(self):
        print("DVD Information:")
        super().display_info()
        print(f"Director: {self.director}")


class Journal(LibraryItem):
    def __init__(self, title, item_id, volume):
        super().__init__(title, item_id)
        self.volume = volume

    def display_info(self):
        print("Journal Information:")
        super().display_info()
        print(f"Volume: {self.volume}")


def main():
    book = Book("The Great Gatsby", 1, "F. Scott Fitzgerald")
    dvd = DVD("Inception", 2, "Christopher Nolan")
    journal = Journal("Scientific American", 3, 2022)

    print("Library Catalog System:")
    book.display_info()
    book.check_out()
    book.check_in()

    dvd.display_info()
    dvd.check_out()
    dvd.check_in()

    journal.display_info()
    journal.check_out()
    journal.check_in()


if __name__ == "__main__":
    main()
