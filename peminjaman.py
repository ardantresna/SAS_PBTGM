from datetime import datetime

class Item:
    def __init__(self, item_id, name, available=True):
        self.item_id = item_id
        self.name = name
        self.available = available

    def __str__(self):
        return f"{self.name} (ID: {self.item_id}) - {'Available' if self.available else 'Not Available'}"


class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name

    def __str__(self):
        return f"{self.name} (ID: {self.borrower_id})"


class LoanManager:
    def __init__(self):
        self.items = []
        self.borrowers = []
        self.loans = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item.name}' added.")

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)
        print(f"Borrower '{borrower.name}' added.")

    def borrow_item(self, item_id, borrower_id):
        item = next((i for i in self.items if i.item_id == item_id and i.available), None)
        borrower = next((b for b in self.borrowers if b.borrower_id == borrower_id), None)
        
        if item and borrower:
            item.available = False
            loan = {
                'item': item,
                'borrower': borrower,
                'borrowed_date': datetime.now()
            }
            self.loans.append(loan)
            print(f"Item '{item.name}' borrowed by '{borrower.name}' on {loan['borrowed_date']}.")
        else:
            print("Borrowing failed: Item might not be available or borrower not found.")

    def return_item(self, item_id):
        loan = next((l for l in self.loans if l['item'].item_id == item_id), None)
        
        if loan:
            loan['item'].available = True
            self.loans.remove(loan)
            print(f"Item '{loan['item'].name}' returned by '{loan['borrower'].name}'.")
        else:
            print("Return failed: Loan record not found.")

    def show_available_items(self):
        print("Available items:")
        for item in self.items:
            if item.available:
                print(item)

    def show_loans(self):
        print("Current loans:")
        for loan in self.loans:
            print(f"Item: {loan['item'].name}, Borrower: {loan['borrower'].name}, Date: {loan['borrowed_date']}")

# Menu interaktif untuk pengguna
def main():
    manager = LoanManager()

    while True:
        print("\n=== Sistem Peminjaman Barang ===")
        print("1. Tambah Barang")
        print("2. Tambah Peminjam")
        print("3. Pinjam Barang")
        print("4. Kembalikan Barang")
        print("5. Tampilkan Barang yang Tersedia")
        print("6. Tampilkan Daftar Peminjaman")
        print("0. Keluar")

        choice = input("Pilih opsi: ")

        if choice == "1":
            item_id = int(input("Masukkan ID Barang: "))
            name = input("Masukkan Nama Barang: ")
            manager.add_item(Item(item_id, name))

        elif choice == "2":
            borrower_id = int(input("Masukkan ID Peminjam: "))
            name = input("Masukkan Nama Peminjam: ")
            manager.add_borrower(Borrower(borrower_id, name))

        elif choice == "3":
            item_id = int(input("Masukkan ID Barang yang Dipinjam: "))
            borrower_id = int(input("Masukkan ID Peminjam: "))
            manager.borrow_item(item_id, borrower_id)

        elif choice == "4":
            item_id = int(input("Masukkan ID Barang yang Dikembalikan: "))
            manager.return_item(item_id)

        elif choice == "5":
            manager.show_available_items()

        elif choice == "6":
            manager.show_loans()

        elif choice == "0":
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
