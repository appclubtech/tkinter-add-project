from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class AddNumApp:

    def __init__(self, master):

        # window title
        master.title("Add Numbers")
        # disable resize of window in all directions
        master.resizable(False, False)

        # style object
        self.style = ttk.Style()
        # use default theme
        self.style.theme_use('default')

        # create label widget which shows the result
        self.result = ttk.Label(master, text="0", justify=CENTER, background="#FFFFFF")
        self.result.grid(row=1, column=0, padx=10, pady=22, columnspan=2)

        # create entry widget where user inputs the first value
        self.first_value = ttk.Entry(master, width=10)
        self.first_value.grid(row=2, column=0, padx=10, pady=10)

        # create entry widget where user inputs the second value
        self.second_value = ttk.Entry(master, width=10)
        self.second_value.grid(row=2, column=1, padx=10, pady=10)

        # create button widget which adds first and second value
        self.add_button = ttk.Button(master, width=8, text="Add", command=self.add)
        self.add_button.grid(row=3, column=0, padx=10, pady=5)

        # create button widget which clears input
        self.add_button = ttk.Button(master, width=8, text="Clear", command=self.clear)
        self.add_button.grid(row=3, column=1, padx=10, pady=12)

    def add(self):
        try:
            # get first value
            first_value = self.first_value.get()
            # get second value
            second_value = self.second_value.get()

            # validate first value is not empty
            if first_value == "":
                messagebox.showerror("Value Error", "Enter first value")
                return

            # validate second value is not empty
            if second_value == "":
                messagebox.showerror("Value Error", "Enter second value")
                return

            # getting addition result by adding first and second value
            result = self.add_num(float(first_value), float(second_value))

            # setting result value to label widget
            self.result.configure(text='{} + {} = {}'.format(str(first_value),
                                                             str(second_value),
                                                             str(result)))
        except ValueError:
            # displaying error message box
            messagebox.showerror("Invalid input", "Invalid input detected. Numbers are only supported")
            # clearing input
            self.clear()

    # returns a number by adding first and second
    @staticmethod
    def add_num(first, second):
        return first + second

    # clears input in entry widget and sets 0 in label widget
    def clear(self):
        self.first_value.delete(0, 'end')
        self.second_value.delete(0, 'end')
        self.result.configure(text='0')


def main():
    master = Tk()
    AddNumApp(master)
    master.mainloop()


if __name__ == '__main__':
    main()
