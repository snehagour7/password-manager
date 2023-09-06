#!/usr/bin/env python
# coding: utf-8

# In[ ]:






# In[2]:


import tkinter as tk
from tkinter import messagebox

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if website and username and password:
        # Code to save the password to a file or database
        messagebox.showinfo("Success", "Password saved!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Create the GUI window
window = tk.Tk()
window.title("Password Manager")

# Create labels and entry fields
website_label = tk.Label(window, text="Website:")
website_label.pack()
website_entry = tk.Entry(window)
website_entry.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create a button to save the password
save_button = tk.Button(window, text="Save Password", command=save_password)
save_button.pack()

# Start the GUI event loop
window.mainloop()



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




