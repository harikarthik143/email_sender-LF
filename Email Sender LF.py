import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox
import time
import threading

def main_gui():
    root = Tk()
    root.title("Automated Email Sender")

    # Configure the size of the main window
    root.geometry("517x345")  # Width: 500px, Height: 400px
    # Set the background color of the root window
    root.configure(bg='#f7d794')  # Light gray background

    # Define a custom font
    custom_font = ('Eras Bold ITC', 12 )
    label_bg = '#f7d794'  # Same as root background color
    entry_bg = '#FFFFFF'  # White background for entry fields

    # GUI elements with custom font and background color
    Label(root, text="Sender's Email", font=custom_font, bg=label_bg).grid(row=0, column=0, sticky="e", padx=10, pady=5)
    sender_entry = Entry(root, width=30, font=custom_font, bg=entry_bg)
    sender_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)

    Label(root, text="Password", font=custom_font, bg=label_bg).grid(row=1, column=0, sticky="e", padx=10, pady=5)
    password_entry = Entry(root, show="*", width=30, font=custom_font, bg=entry_bg)
    password_entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    Label(root, text="Recipient's Email", font=custom_font, bg=label_bg).grid(row=2, column=0, sticky="e", padx=10, pady=5)
    recipient_entry = Entry(root, width=30, font=custom_font, bg=entry_bg)
    recipient_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    Label(root, text="Subject", font=custom_font, bg=label_bg).grid(row=3, column=0, sticky="e", padx=10, pady=5)
    subject_entry = Entry(root, width=30, font=custom_font, bg=entry_bg)
    subject_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    Label(root, text="Message", font=custom_font, bg=label_bg).grid(row=4, column=0, sticky="e", padx=10, pady=5)
    message_entry = Text(root, width=30, height=5, font=custom_font, bg=entry_bg)
    message_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)

    Label(root, text="Send after (seconds)", font=custom_font, bg=label_bg).grid(row=5, column=0, sticky="e", padx=10, pady=5)
    delay_entry = Entry(root, width=30, font=custom_font, bg=entry_bg)
    delay_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)

    def send_email():
        sender = sender_entry.get()
        password = password_entry.get()  # Use your App Password here
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        message = message_entry.get("1.0", END)
        delay = int(delay_entry.get())

        threading.Thread(target=schedule_email, args=(sender, password, recipient, subject, message, delay)).start()

    send_button = Button(root, text="Send Email", font=custom_font, bg="#f3f4f8")
    send_button.grid(row=6, column=1, sticky="w,e", padx=10, pady=5)

    root.mainloop()

def schedule_email(sender, password, recipient, subject, message, delay):
    time.sleep(delay)
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    main_gui()
