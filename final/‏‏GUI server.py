import socket_server
import RSA
import tkinter as gui

encrypted_data = socket_server.receive()


def button_processing():
    # print(encrypted_data)
    # print("public key:", publicKeyEntry.get())
    # print("N of public key", n_Value_of_public_entry.get())
    # print("private key:", privateKeyEntry.get())
    # print("N of private key", n_Value_of_private_entry.get())
    dictionary = RSA.Decryption(encrypted_data, int(privateKeyEntry.get()), int(n_Value_of_private_entry.get()),
                                int(publicKeyEntry.get()), int(n_Value_of_public_entry.get()))

    messageLabel.place(relx=0.01, rely=0.5, relheight=0.1, relwidth=0.2)

    messageEntry.insert(1.0, 'alter validation: ' + str(dictionary['alter validation']) + '\t' +
                        'entity validation: ' + str(dictionary['entity validation']) + '\n' +
                        'message:\n' + dictionary['message'])

    messageEntry['state'] = 'disabled'
    messageEntry.place(relx=0.21, rely=0.5, relheight=0.25, relwidth=0.75)


HEIGHT = 400
WIDTH = 600

root = gui.Tk()

# ---widgets--- #

# to set a default size of windows
canvas = gui.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# main frame
decryptionFrame = gui.LabelFrame(root, text="decryption")
decryptionFrame.place(relx=0.025, rely=0.025, relheight=0.9, relwidth=0.9)

# publicKey entry label
publicKeyLabel = gui.Label(decryptionFrame, text="Public key:")
publicKeyLabel.place(relx=0.01, rely=0.1, relheight=0.1, relwidth=0.2)
# publicKey entry field
publicKeyEntry = gui.Entry(decryptionFrame)
publicKeyEntry.place(relx=0.21, rely=0.1, relheight=0.08, relwidth=0.3)

# N value label
n_Value_of_public_label = gui.Label(decryptionFrame, text="N:")
n_Value_of_public_label.place(relx=0.54, rely=0.1, relheight=0.1, relwidth=0.1)
# N value entry
n_Value_of_public_entry = gui.Entry(decryptionFrame)
n_Value_of_public_entry.place(relx=0.61, rely=0.1, relheight=0.08, relwidth=0.35)

# privateKey entry label
privateKeyLabel = gui.Label(decryptionFrame, text="Private key:")
privateKeyLabel.place(relx=0.01, rely=0.2, relheight=0.1, relwidth=0.2)
# privateKey entry field
privateKeyEntry = gui.Entry(decryptionFrame)
privateKeyEntry.place(relx=0.21, rely=0.2, relheight=0.08, relwidth=0.3)

# N value label
n_Value_of_private_label = gui.Label(decryptionFrame, text="N:")
n_Value_of_private_label.place(relx=0.54, rely=0.2, relheight=0.1, relwidth=0.1)
# N value entry
n_Value_of_private_entry = gui.Entry(decryptionFrame)
n_Value_of_private_entry.place(relx=0.61, rely=0.2, relheight=0.08, relwidth=0.35)

# button
sendButton = gui.Button(decryptionFrame, text="decrypt message", command=lambda: button_processing())
sendButton.place(relx=0.45, rely=0.3)

# message label
messageLabel = gui.Label(decryptionFrame, text="Message:")

# message text field
messageEntry = gui.Text(decryptionFrame)

root.mainloop()
