import socket_client
import RSA
from tkinter import *
import tkinter as gui


def send_button_processing():
    encryption_message = RSA.Encryption(messageEntry.get(1.0, END),
                                        int(publicKeyEntry.get()), int(n_Value_of_public_entry.get()),
                                        int(privateKeyEntry.get()), int(n_Value_of_private_entry.get()))
    print(encryption_message)
    socket_client.send(encryption_message)
    statusLabel['text'] = "Message sent successfully"


HEIGHT = 400
WIDTH = 600

root = gui.Tk()

# ---widgets--- #

# to set a default size of windows
canvas = gui.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# main frame
encryptionFrame = gui.LabelFrame(root, text="Encryption")
encryptionFrame.place(relx=0.025, rely=0.025, relheight=0.9, relwidth=0.9)

# publicKey entry label
publicKeyLabel = gui.Label(encryptionFrame, text="Public key:")
publicKeyLabel.place(relx=0.01, rely=0.1, relheight=0.1, relwidth=0.2)
# publicKey entry field
publicKeyEntry = gui.Entry(encryptionFrame)
publicKeyEntry.place(relx=0.21, rely=0.1, relheight=0.08, relwidth=0.3)
# N value label
n_Value_of_public_label = gui.Label(encryptionFrame, text="N:")
n_Value_of_public_label.place(relx=0.52, rely=0.1, relheight=0.1, relwidth=0.1)
# N value entry
n_Value_of_public_entry = gui.Entry(encryptionFrame)
n_Value_of_public_entry.place(relx=0.61, rely=0.1, relheight=0.08, relwidth=0.35)

# signature label
signatureLabel = gui.Label(encryptionFrame, text="Signature:")
signatureLabel.place(relx=0.01, rely=0.25, relheight=0.1, relwidth=0.2)

# publicKey entry label
privateKeyLabel = gui.Label(encryptionFrame, text="Private key:")
privateKeyLabel.place(relx=0.01, rely=0.35, relheight=0.1, relwidth=0.2)
# publicKey entry field
privateKeyEntry = gui.Entry(encryptionFrame)
privateKeyEntry.place(relx=0.21, rely=0.35, relheight=0.08, relwidth=0.3)
# N value label
n_Value_of_private_label = gui.Label(encryptionFrame, text="N:")
n_Value_of_private_label.place(relx=0.52, rely=0.35, relheight=0.1, relwidth=0.1)
# N value entry
n_Value_of_private_entry = gui.Entry(encryptionFrame)
n_Value_of_private_entry.place(relx=0.61, rely=0.35, relheight=0.08, relwidth=0.35)

# message label
messageLabel = gui.Label(encryptionFrame, text="Message:")
messageLabel.place(relx=0.01, rely=0.5, relheight=0.1, relwidth=0.2)
# message text field
messageEntry = gui.Text(encryptionFrame)
messageEntry.place(relx=0.21, rely=0.5, relheight=0.25, relwidth=0.75)

# button
sendButton = gui.Button(encryptionFrame, text="Send", command=lambda: send_button_processing())
sendButton.place(relx=0.5, rely=0.8)

# status label
statusLabel = gui.Label(encryptionFrame)
statusLabel.place(relx=0.3, rely=0.9)

root.mainloop()
