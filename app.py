import tkinter as tk
import csv

CSV_FILE_PATH = 'data.csv'


def write_to_csv():
    data = [
        entry_date.get(),
        entry_day.get(),
        entry_time.get(),
        entry_price.get()
    ]
    with open(CSV_FILE_PATH, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    # Clearing the fields after writing
    entry_date.delete(0, tk.END)
    entry_day.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_price.delete(0, tk.END)


def view_last_session():
    pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('SessionTracker')

    def add_session():
        add_frame.pack()
        view_frame.pack_forget()

    def view_session():
        view_frame.pack()
        add_frame.pack_forget()

    # Frame for adding a session
    add_frame = tk.Frame(root)
    label_date = tk.Label(add_frame, text='Date:')
    label_date.pack()
    entry_date = tk.Entry(add_frame)
    entry_date.pack()

    label_day = tk.Label(add_frame, text='Day:')
    label_day.pack()
    entry_day = tk.Entry(add_frame)
    entry_day.pack()

    label_time = tk.Label(add_frame, text='Time:')
    label_time.pack()
    entry_time = tk.Entry(add_frame)
    entry_time.pack()

    label_price = tk.Label(add_frame, text='Price:')
    label_price.pack()
    entry_price = tk.Entry(add_frame)
    entry_price.pack()

    save_button = tk.Button(add_frame, text='Save', command=write_to_csv)
    save_button.pack()

    # Frame for viewing the last session
    view_frame = tk.Frame(root)
    # Add elements here for viewing the last session

    # Creating buttons for action selection
    add_button = tk.Button(root, text='Add Session', command=add_session)
    add_button.pack()

    view_button = tk.Button(root, text='View Last Session', command=view_session)
    view_button.pack()

    root.mainloop()
