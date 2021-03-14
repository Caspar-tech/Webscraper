import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_excel_file():
    filepath = askopenfilename(
        filetypes=[("Excel", "*.xlsx"), ("All files", "*.*")]
    )
    print(filepath)

    label_rows["text"] = filepath

    if not filepath:
        return

window = tk.Tk()
window.title("Big-checker")

window.columnconfigure([0], minsize=20)
window.rowconfigure([0, 1, 2, 3], minsize=20)

label_start = tk.Label(text="Dit is een BIG-checker. Selecteer een Excel file. let op:\n"
                            "- De BIG-nummers staan in de eerste kolom \n"
                            "- De bijbehorende achternamen staat in de tweede kolom \n"
                            "- De excel file is gesloten voordat je hem upload",
                       justify="left")
button_open = tk.Button(text="Open file", width=20, command=open_excel_file)

label_start.grid(row=0, column=0, sticky="w", padx=5, pady=5)
button_open.grid(row=1, column=0, padx=5, pady=5)

window.mainloop()
