from tkinter.font import names
from typing import List


class Name:
    names = ["Benny", "Charlotte", "Freddy", "Ane", "Emil", "Bob", "Emilie", "Dorte", "Emilia", "Bo"]

    def sort_and_count_letters(self):
        # Sort by length and alphabetically
        sorted_names = sorted(self.names, key=lambda x: (len(x), x))

        # Dictionary to store letter counts for each word
        letter_count_table = {}

        # Iterate through each sorted name
        for name in sorted_names:
            # Create a dictionary to count letters for the current name
            letter_count = {}

            # Count each letter in the name
            for char in name:
                if char in letter_count:
                    letter_count[char] += 1
                else:
                    letter_count[char] = 1

            # Add this letter count dictionary to the hash table, with the name as the key
            letter_count_table[name] = letter_count

        # Print each name and its letter count dictionary
        for name, count in letter_count_table.items():
            print(f"{name}: {count}")

    def main(self):
        print("Hello World!")
        self.sort_and_count_letters()  # Call the method to sort and count letters


if __name__ == "__main__":
    Name().main()
