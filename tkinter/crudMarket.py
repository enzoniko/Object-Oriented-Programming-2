# Deboráh Raquel Bussolo Ferreira e Enzo Nicolás Spotorno Bieger
# Simple CRUD supermarket application with tkinter
import itertools
from tkinter import *
class Market:
    def __init__(self, master):
        self.master = master
        master.title("Supermarket")
        master.geometry("680x200")
        master.resizable(1, 1)
        self.grid = []
        self.products = {}
        self.table = {}
        self.create_widgets()
        
      
    def create_widgets(self):
        self.label = Label(self.master, text="Supermarket")
        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E+N+S)

        self.label = Label(self.master, text="Product")
        self.label.grid(row=1, column=0, sticky=W+E+N+S)

        self.product = Entry(self.master)
        self.product.grid(row=1, column=1, sticky=W+E+N+S)

        self.label = Label(self.master, text="Price")
        self.label.grid(row=2, column=0, sticky=W+E+N+S)

        self.price = Entry(self.master)
        self.price.grid(row=2, column=1, sticky=W+E+N+S)

        self.label = Label(self.master, text="Quantity")
        self.label.grid(row=3, column=0, sticky=W+E+N+S)

        self.quantity = Entry(self.master)
        self.quantity.grid(row=3, column=1, sticky=W+E+N+S)

        self.button = Button(self.master, text="Create", command=self.create)
        self.button.grid(row=4, column=0, sticky=W+E+N+S)

        self.button = Button(self.master, text="Update", command=self.update)
        self.button.grid(row=4, column=1, sticky=W+E+N+S)

        self.button = Button(self.master, text="Close", command=self.close)
        self.button.grid(row=5, column=0, columnspan=2, sticky=W+E+N+S)
 
        self.update_table()
    def update_table(self):
        for e in self.grid:
            e.destroy()
        for i, j in itertools.product(range(1, 10 - len(self.products)), range(4)):
            e = Entry(self.master)
            e.grid(row=len(self.products)+ i, column=2 + j, sticky=W+E+N+S)
            e.config(state=DISABLED)
            self.grid.append(e)
        
        if len(self.products) > 0:

            self.label.grid_forget()
            print(self.products)
            print("Antes",self.table)
            for i, produto in enumerate(self.products):
                self.table[produto] = [Entry(self.master)]
                self.table[produto][0].grid(row=i + 1, column=2, sticky=W+E+N+S)
                self.table[produto][0].insert(0, produto)
                for j, valor in enumerate(self.products[produto]):
                    value = Entry(self.master)
                    value.grid(row=i + 1, column=3 + j, sticky=W+E+N+S)
                    value.insert(0, valor)
                    value.config(state=DISABLED)
                    self.table[produto].append(value)
                delete = Button(self.master, text="Delete", command=self.delete_row(produto))
                delete.grid(row=i + 1, column=5, sticky=W+E+N+S)   
                self.table[produto].append(delete)
            print("Depois", self.table)
        else:


            self.product_label = Label(self.master, text="Product")
            self.product_label.grid(row=0, column=2, sticky=W+E+N+S)
            self.price_label = Label(self.master, text="Price")
            self.price_label.grid(row=0, column=3, sticky=W+E+N+S)
            self.quantity_label = Label(self.master, text="Quantity")
            self.quantity_label.grid(row=0, column=4, sticky=W+E+N+S)
            self.label = Label(self.master, text="No products")
            self.label.grid(row=7, column=0, columnspan=2, sticky=W+E+N+S)

            
    def delete_row(self, product):
        def delete():
            del self.products[product]
            for element in self.table:
                for object in self.table[element]:
                    object.destroy()
            self.table.clear()
            self.update_table()
        return delete

    def create(self):
        self.products[self.product.get()] = [self.price.get(), self.quantity.get()]
        self.update_table()

    def update(self):
       
        if self.product.get() in self.products:
            if self.product.get() != self.table[self.product.get()][0].get():
                self.products[self.table[self.product.get()][0].get()] = [self.price.get(), self.quantity.get()]
                del self.products[self.product.get()]
                self.table[self.table[self.product.get()][0].get()] = self.table[self.product.get()]
                del self.table[self.product.get()]
            else:
                self.products[self.product.get()] = [self.price.get(), self.quantity.get()]
            self.update_table()
        else:
            print("Product not found")

    def close(self):
        self.master.destroy()
    
root = Tk()
my_gui = Market(root)
root.mainloop()

