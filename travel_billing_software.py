import tkinter as tk
from tkinter import ttk
import random
from datetime import date
from tkinter import messagebox


class BillingSoftware:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing Software")

        # Banner
        banner_frame = tk.Frame(self.root, bg="#A569BD", bd=10)
        banner_frame.pack(fill=tk.X)

        # Banner Label
        banner_label = tk.Label(banner_frame, text="Billing System", font=("Arial Black", 20), bg="#A569BD",
                                fg="white")
        banner_label.pack(pady=10)

        # Customer Details
        customer_frame = tk.LabelFrame(self.root, text="", font=("Arial Black", 12),
                                       bg="#E5B4F3", fg="#6C3483", relief=tk.GROOVE, bd=10)
        customer_frame.pack(fill=tk.BOTH, padx=10, pady=10)

        # Number
        number_label = tk.Label(customer_frame, text="Name:", font=("Arial", 12), bg="#E5B4F3", fg="#6C3483")
        number_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.number_entry = tk.Entry(customer_frame, font=("Arial", 12))
        self.number_entry.grid(row=0, column=1, padx=5, pady=5)

        # Phone Number
        phone_label = tk.Label(customer_frame, text="Phone Number:", font=("Arial", 12), bg="#E5B4F3", fg="#6C3483")
        phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.phone_entry = tk.Entry(customer_frame, font=("Arial", 12))
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        # Billing Number
        billi_label = tk.Label(customer_frame, text="Billing Number:", font=("Arial", 12), bg="#E5B4F3", fg="#6C3483")
        billi_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.billi_entry = tk.Entry(customer_frame, font=("Arial", 12))
        self.billi_entry.insert(0, str(random.randint(1, 1000)))  # Randomly generate and insert a value
        self.billi_entry.config(state="readonly")  # Make the field read-only
        self.billi_entry.grid(row=0, column=3, padx=5, pady=5)

        # Payment Mode
        payment_mode_label = tk.Label(customer_frame, text="Payment Mode:", font=("Arial", 12), bg="#E5B4F3",
                                      fg="#6C3483")
        payment_mode_label.grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.payment_mode_combobox = ttk.Combobox(customer_frame, values=["UPI", "Cash", "Cards"],
                                                  font=("Arial", 12), state="readonly")
        self.payment_mode_combobox.grid(row=1, column=3, padx=5, pady=5)

        # Ticket Details
        ticket_frame = tk.LabelFrame(self.root, text="Ticket", font=("Arial Black", 12),
                                     bg="#E5B4F3", fg="#6C3483", relief=tk.GROOVE, bd=10)
        ticket_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        # Ticket Details Labels and Entries
        ticket_labels = ["Source:", "Destination:", "Date of Travel:", "Booking Date:",
                         "Ticket Price:", "Passengers:", "PNR:", "Type:"]
        self.ticket_entries = []
        for i, label_text in enumerate(ticket_labels):
            label = tk.Label(ticket_frame, text=label_text, font=("Arial", 12), bg="#E5B4F3", fg="#6C3483")
            if i < 4:
                label.grid(row=0, column=i, padx=5, pady=5, sticky="e")
            else:
                label.grid(row=1, column=i-4, padx=5, pady=5, sticky="e")

            if label_text == "Booking Date:":
                entry_value = str(date.today())  # Set current date as default for Booking Date
            else:
                entry_value = ""

            if label_text == "Type:":
                entry = ttk.Combobox(ticket_frame, values=["Bus", "Train", "Flight"], font=("Arial", 12), state="readonly")
            else:
                entry = tk.Entry(ticket_frame, font=("Arial", 12))
            entry.insert(0, entry_value)

            if i < 4:
                entry.grid(row=0, column=i+1, padx=5, pady=5, sticky="w")
            else:
                entry.grid(row=1, column=i-3, padx=5, pady=5, sticky="w")

            self.ticket_entries.append(entry)

        # Ticket Total Button
        ticket_total_button = tk.Button(ticket_frame, text="Ticket Total", font=("Arial", 12), bg="#A569BD", fg="white", command=self.calculate_ticket_total)
        ticket_total_button.grid(row=1, column=len(ticket_labels)-2, padx=5, pady=5, sticky="w")

        # Visa Details
        visa_frame = tk.LabelFrame(self.root, text="Visa", font=("Arial Black", 12),
                                   bg="#E5B4F3", fg="#6C3483", relief=tk.GROOVE, bd=10)
        visa_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        # Visa Details Labels and Entries
        visa_labels = ["Visa Number:", "Booking Date:", "Country:", "Mode:", "Price:"]
        self.visa_entries = []
        for i, label_text in enumerate(visa_labels):
            label = tk.Label(visa_frame, text=label_text, font=("Arial", 12), bg="#E5B4F3", fg="#6C3483")
            label.grid(row=i // 2, column=i % 2 * 2, padx=5, pady=5, sticky="e")
            entry = tk.Entry(visa_frame, font=("Arial", 12))
            entry.grid(row=i // 2, column=i % 2 * 2 + 1, padx=5, pady=5, sticky="w")

            if label_text == "Booking Date:":
                entry.insert(0, str(date.today()))  # Set today's date as default for Booking Date

            if label_text == "Mode:":
                entry = ttk.Combobox(visa_frame, values=["Short Term", "Long Term", "Business"],
                                     font=("Arial", 12), state="readonly")
                entry.grid(row=i // 2, column=i % 2 * 2 + 1, padx=5, pady=5, sticky="w")

            if label_text == "Price:":
                entry = tk.Entry(visa_frame, font=("Arial", 12))
                entry.grid(row=i // 2, column=i % 2 * 2 + 1, padx=5, pady=5, sticky="w")

            self.visa_entries.append(entry)

        # Button in Visa Label
        visa_button = tk.Button(visa_frame, text="Visa Total", font=("Arial", 12), bg="#A569BD", fg="white", command=self.calculate_visa_total)
        visa_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Certificate Details
        certificate_frame = tk.LabelFrame(self.root, text="Certificate", font=("Arial Black", 12),
                                          bg="#E5B4F3", fg="#6C3483", relief=tk.GROOVE, bd=10)
        certificate_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

        # Certificate Details Labels and Entries
        certificate_labels = ["Number:", "Country:", "Type:", "Price:"]
        self.certificate_entries = []
        for i, label_text in enumerate(certificate_labels):
            label = tk.Label(certificate_frame, text=label_text, font=("Arial", 12), bg="#E5B4F3", fg="#6C3483")
            label.grid(row=i // 2, column=i % 2 * 2, padx=5, pady=5, sticky="e")
            entry = tk.Entry(certificate_frame, font=("Arial", 12))
            entry.grid(row=i // 2, column=i % 2 * 2 + 1, padx=5, pady=5, sticky="w")

            if label_text == "Price:":
                entry = tk.Entry(certificate_frame, font=("Arial", 12))
                entry.grid(row=i // 2, column=i % 2 * 2 + 1, padx=5, pady=5, sticky="w")

            self.certificate_entries.append(entry)

        # Button in Certificate Label
        certificate_button = tk.Button(certificate_frame, text="Certificate Total", font=("Arial", 12), bg="#A569BD", fg="white", command=self.calculate_certificate_total)
        certificate_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    def calculate_ticket_total(self):
        ticket_price = self.ticket_entries[4].get()
        passengers = self.ticket_entries[5].get()
        if ticket_price.isdigit() and passengers.isdigit():
            total = int(ticket_price) * int(passengers)
            self.save_to_file("Ticket", total)
        else:
            print("Invalid value")

    def calculate_visa_total(self):
        visa_price = self.visa_entries[4].get()
        visa_number = self.visa_entries[0].get()
        if visa_price.isdigit() and visa_number.isdigit():
            total = int(visa_price) * int(visa_number)
            self.save_to_file("Visa", total)
        else:
            print("Invalid value")

    def calculate_certificate_total(self):
        certificate_price = self.certificate_entries[3].get()
        if certificate_price.isdigit():
            total = int(certificate_price)
            self.save_to_file("Certificate", total)
        else:
            print("Invalid value")

    def save_to_file(self, category, total):
        customer_number = self.number_entry.get()
        customer_phone = self.phone_entry.get()
        billing_number = self.billi_entry.get()
        payment_mode = self.payment_mode_combobox.get()

        ticket_source = self.ticket_entries[0].get()
        ticket_destination = self.ticket_entries[1].get()
        ticket_travel_date = self.ticket_entries[2].get()
        ticket_booking_date = self.ticket_entries[3].get()
        ticket_price = self.ticket_entries[4].get()
        ticket_passengers = self.ticket_entries[5].get()
        ticket_pnr = self.ticket_entries[6].get()
        ticket_type = self.ticket_entries[7].get()

        visa_number = self.visa_entries[0].get()
        visa_booking_date = self.visa_entries[1].get()
        visa_country = self.visa_entries[2].get()
        visa_mode = self.visa_entries[3].get()
        visa_price = self.visa_entries[4].get()

        certificate_number = self.certificate_entries[0].get()
        certificate_country = self.certificate_entries[1].get()
        certificate_type = self.certificate_entries[2].get()
        certificate_price = self.certificate_entries[3].get()

        # Create file name with category, customer number, and current date
        file_name = f"{category}_{customer_number}_{date.today().strftime('%Y%m%d')}.txt"

        with open(file_name, "w") as file:
            file.write("Welcom to Our Shop\n")
            file.write("====================================\n")
            file.write(f"Category: {category}\n")
            file.write("====================================\n")
            file.write(f"Customer Number: {customer_number}\n")
            file.write(f"Customer Phone: {customer_phone}\n")
            file.write(f"Billing Number: {billing_number}\n")
            file.write(f"Payment Mode: {payment_mode}\n")
            file.write(f"\n")
            file.write("====================================\n")
            file.write(f"Ticket Details:\n")
            file.write(f"Source: {ticket_source}\n")
            file.write(f"Destination: {ticket_destination}\n")
            file.write(f"Date of Travel: {ticket_travel_date}\n")
            file.write(f"Booking Date: {ticket_booking_date}\n")
            file.write(f"Ticket Price: {ticket_price}\n")
            file.write(f"Passengers: {ticket_passengers}\n")
            file.write(f"PNR: {ticket_pnr}\n")
            file.write(f"Type: {ticket_type}\n")
            file.write("====================================\n")
            file.write(f"\n")
            file.write(f"Visa Details:\n")
            file.write(f"Visa Number: {visa_number}\n")
            file.write(f"Booking Date: {visa_booking_date}\n")
            file.write(f"Country: {visa_country}\n")
            file.write(f"Mode: {visa_mode}\n")
            file.write(f"Price: {visa_price}\n")
            file.write(f"\n")
            file.write("====================================\n")
            file.write(f"Certificate Details:\n")
            file.write(f"Number: {certificate_number}\n")
            file.write(f"Country: {certificate_country}\n")
            file.write(f"Type: {certificate_type}\n")
            file.write(f"Price: {certificate_price}\n")
            file.write(f"\n")
            file.write("====================================\n")
            file.write(f"Total: {total}")
            file.write(f"\n")
            file.write("Thank you shopping with us\n")

        print("File saved successfully!")
        # Display dialog box
        messagebox.showinfo("File Saved", "Invoice Generated successfully!")

root = tk.Tk()
billing_software = BillingSoftware(root)
root.mainloop()
