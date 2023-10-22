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

modelid = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtypes=torch.float16, auth_token=auth_token, device="cuda")

# Create generate function
def generate():
    pass


# Create button
button = ctk.CTkButton(height=30, width=130, text="Submit", fg_color="green", master=app, command=generate) # (Green is a placeholder colour)
# Configure button
button.configure(text="Generate")
# Place button
button.place(x=235, y=65)

# Create main
lmain = ctk.CTkLabel(height=480, width=580, fg_color="blue", master=app) # (Blue is a placeholder colour)
# Place main
lmain.place(x=10, y=100)


app.mainloop()
                      
