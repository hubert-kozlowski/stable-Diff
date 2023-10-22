# TK imports
import tkinter as tk
import customtkinter as ctk
# Other imports
from PIL import ImageTk, Image
from authtoken import auth_token
# PyTorch imports
import torch
from torch import autocast
# Diffuser imports
from diffusers import StableDiffusionPipeline

# Create app
app = tk.Tk()
app.geometry("600x600")
app.title("Stable Diffusion Demo")
app.resizable(False, False)

# Create prompt box
prompt = ctk.CTkEntry(height=50, width=580, text_color="black", fg_color="white", master=app)
# Place prompt box
prompt.place(x=10, y=10)

# Create main
lmain = ctk.CTkLabel(height=500, width=580, fg_color="blue", master=app) # (Blue is a placeholder colour)
# Place main
lmain.place(x=10, y=60)

# Create button
button = ctk.CTkButton(height=30, width=130, text="Submit", master=app)
# Place button
button.place(x=235, y=570)

app.mainloop()
                      
