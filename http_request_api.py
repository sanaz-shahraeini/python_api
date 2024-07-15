from tkinter.font import Font
import requests
import tkinter as tk
from PIL import Image, ImageTk
import io

root = tk.Tk()
root.title("User Information")
root.resizable(False, False)
my_font = Font(family="Arial", size=14, weight="bold")
images = []
names = []
emails = []

url = "https://reqres.in/api/users"
response = requests.get(url)
user_data = response.json()["data"]


images = []
names = []
emails = []

for user in user_data:
    image_url = user['avatar']
    response = requests.get(image_url)
    image_data = response.content

    image = Image.open(io.BytesIO(image_data))
    image = image.convert("RGB")
    image = ImageTk.PhotoImage(image)
    images.append(image)

    info_name = user['first_name']
    info_email = user['email']
    names.append(info_name)
    emails.append(info_email)


header_label = tk.Label(text="Hello ReqRes Users!", font=my_font)
header_label.grid(row=0, column=1, pady=10)

label1 = tk.Label(text=f"{names[0]} \n {emails[0]}")
label1.grid(row=1, column=0, padx=12, pady=15)

label2 = tk.Label(text=f"{names[1]} \n {emails[1]}")
label2.grid(row=1, column=1, padx=12, pady=15)

label3 = tk.Label(text=f"{names[2]} \n {emails[2]}")
label3.grid(row=1, column=2, padx=12, pady=15)

label4 = tk.Label(text=f"{names[3]} \n {emails[3]}")
label4.grid(row=3, column=0, padx=12, pady=10)

label5 = tk.Label(text=f"{names[4]} \n {emails[4]}")
label5.grid(row=3, column=1, padx=12, pady=10)

label6 = tk.Label(text=f"{names[5]} \n {emails[5]}")
label6.grid(row=3, column=2, padx=12, pady=10)

img1 = tk.Label(image=images[0])
img1.grid(row=2, column=0, padx=12)

img2 = tk.Label(image=images[1])
img2.grid(row=2, column=1, padx=12)

img3 = tk.Label(image=images[2])
img3.grid(row=2, column=2, padx=12)

img4 = tk.Label(image=images[3])
img4.grid(row=4, column=0, padx=12, pady=7)

img5 = tk.Label(image=images[4])
img5.grid(row=4, column=1, padx=12)

img6 = tk.Label(image=images[5])
img6.grid(row=4, column=2, padx=12)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.mainloop()
