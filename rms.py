import tkinter
from tkinter import messagebox,ttk
root=tkinter.Tk()
root.title("MOHAMMED'S HOTEL")
root.geometry("600x400")
root.configure(bg="grey")

MENU_PRICES={
    "Coffee":30.00,
    "Tea":20.00,
    "Chicken Biryani":150.00,
    "Biryani Rice":60.00,
    "Chicken Kabab":100.00,
    "Chapathi":30.00,
    "Parota":40.00
}
new_window = None
right_frame = None
left_frame = None
ph_no = None
dish_textbox = None
quantity_dropdown = None
bill_display = None   
def onclick_submit():
    global new_window,right_frame,left_frame
    global ph_no,dish_textbox,quantity_dropdown,bill_display
    username=username_textbox.get()
    password=password_textbox.get()
    if username=="kaamran" and password=="1234":
        new_window=tkinter.Toplevel(root)
        new_window.title("CUSTOMER INFO")
        new_window.geometry("600x500")
        new_window.configure(bg="grey")
        right_frame=tkinter.Frame(new_window,bg="grey")
        right_frame.pack(side=tkinter.RIGHT,fill=tkinter.BOTH,expand=True,padx=20,pady=20)
        left_frame=tkinter.Frame(new_window,bg="white")
        left_frame.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=True,padx=20,pady=20)
        
        
        
        ph_label=tkinter.Label(left_frame,text="Enter phone number")
        ph_label.pack(anchor=tkinter.W,fill=tkinter.X,pady=2)
        ph_no=tkinter.Entry(left_frame)
        ph_no.pack(anchor=tkinter.W,fill=tkinter.X,pady=5)
        dish_label=tkinter.Label(left_frame,text="Enter dish name")
        dish_label.pack(anchor=tkinter.W,fill=tkinter.X,pady=2)
        dish_textbox=tkinter.Entry(left_frame)
        dish_textbox.pack(anchor=tkinter.W,fill=tkinter.X,pady=5)
        choices=[1,2,3,4,5]
        quantity_label=tkinter.Label(left_frame,text="Enter quantity")
        quantity_label.pack(anchor=tkinter.W,pady=2)
        quantity_dropdown=ttk.Combobox(left_frame,values=choices)
        quantity_dropdown.pack(anchor=tkinter.W,pady=5)
        
        bill_label=tkinter.Label(right_frame,text="TOTAL BILL",bg="light blue",font=("Arial",10,"bold"))
        bill_label.pack(anchor=tkinter.W,pady=2)
        
        bill_display=tkinter.Text(right_frame,width=35,height=12,font=("courier",10))
        bill_display.pack(fill=tkinter.BOTH,expand=True,pady=5)
        save_button=tkinter.Button(left_frame,text="Save Bill",command=generate_bill,bg="black",fg="white",font=("Arial",10,"bold"))
        save_button.pack(anchor=tkinter.W,fill=tkinter.X,pady=15) 
    else:
        messagebox.showinfo("warning","Please fill details correctly")
def generate_bill():
    global bill_display,dish_textbox,quantity_dropdown,ph_no
    phone_number=ph_no.get().strip()
    dish=dish_textbox.get().strip().title()
    quantity=quantity_dropdown.get().strip()
    
    
    if not phone_number or not dish or not quantity:
        messagebox.showerror("ERROR","Please fill all the details")
        return
    
    quantityy=int(quantity)
    price_per_item=MENU_PRICES.get(dish,0.00)
    price=price_per_item*quantityy
    
    bill_receipt=(
        "============================\n"
        "      MOHAMMED'S HOTEL      \n"
        "============================\n"
        "Customer Ph:{}\n"
        "Item name:{}\n"    
        "Quantity:{}\n"                    
        "Price:Rs. {:.2f}\n"
        "----------------------------\n"
        "TOTAL BILL:Rs. {:.2f}\n"
        "============================\n"               
    ).format(phone_number,dish,quantityy,price_per_item,price)
    bill_display.delete("1.0",tkinter.END)
    bill_display.insert(tkinter.END,bill_receipt)
    try:
        with open("bills.txt","a") as file:
            file.write(bill_receipt+"\n\n")
        messagebox.showinfo("success","bill saved")
    except Exception as e:
        error_msg="Could not save the bill: {}".format(e)
        messagebox.showerror("File Error",error_msg) 
username_label=tkinter.Label(root,text="Enter Username")
username_label.pack()
username_textbox=tkinter.Entry(root)
username_textbox.pack()

password_label=tkinter.Label(root,text="Enter Password")
password_label.pack()
password_textbox=tkinter.Entry(root)
password_textbox.pack() 
submit_button=tkinter.Button(root,text="submit",command=onclick_submit)
submit_button.pack()

            
root.mainloop()