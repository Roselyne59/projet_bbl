import tkinter as tk


def create_user_form():
    # Create the main window
    root = tk.Tk()
    root.title("Create User")

    # Labels and entry fields
    firstname_label = tk.Label(root, text="Firstname:")
    firstname_label.pack(pady=5)

    firstname_entry = tk.Entry(root)
    firstname_entry.pack(pady=5)

    lastname_label = tk.Label(root, text="Lastname:")
    lastname_label.pack(pady=5)

    lastname_entry = tk.Entry(root)
    lastname_entry.pack(pady=5)

    birthdate_label = tk.Label(root, text="Birthdate (YYYY-MM-DD):")
    birthdate_label.pack(pady=5)

    birthdate_entry = tk.Entry(root)
    birthdate_entry.pack(pady=5)

    email_label = tk.Label(root, text="Email:")
    email_label.pack(pady=5)

    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    address_label = tk.Label(root, text="Address:")
    address_label.pack(pady=5)

    address_entry = tk.Text(root, width=40, height=5)
    address_entry.pack(pady=5)

    # Checkbox for admin status
    is_admin_var = tk.IntVar()  # Integer variable to store admin state (checked/unchecked)
    is_admin_checkbox = tk.Checkbutton(root, text="Is Admin", variable=is_admin_var)
    is_admin_checkbox.pack(pady=5)

    # Button to submit the form
    def submit_form():
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        birthdate = birthdate_entry.get()
        email = email_entry.get()
        address = address_entry.get("1.0", tk.END)
        is_admin = is_admin_var.get()

       #Data validation

        # Create user object
        user = User(
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
            email=email,
            address=address,
            is_admin=is_admin,
        )

        # Process user object (e.g., save to database)
        
        print(f"Created user: {user.firstname} {user.lastname}")

     
    submit_button = tk.Button(root, text="Add user", command=submit_form)
    submit_button.pack(pady=10)

    
    root.mainloop()


# Run the function to create the form
create_user_form()