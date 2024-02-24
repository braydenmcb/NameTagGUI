""" NAME TAG GENERATOR

- using tkiner and ctkinter, make a small app thing that takes inpout for an emboriderred name tag
- take name (text), font (drop-down menu hopefully), text-color (dropdown menu), background-color (dropdown menu), border-color (dropdown menu)  
- display a live (hopefully) visual of what it would look like
- if possible, convert the output to an emboridery file

"""
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
import customtkinter as ctk

app = ctk.CTk()
app.title("Embroiderred Name Tag Previewer")
app.geometry("500x500")

name = ctk.StringVar(value="Brayden")

name_font = tk.StringVar(app)
name_font.set('Comic Sans MS')

name_color = tk.StringVar(app)
name_color.set('Black')

background_color = tk.StringVar(app)
background_color.set('White')

border_color = tk.StringVar(app)
border_color.set('Blue')



label = ttk.Label(app, text='Generate Your Own Name Tag', font=("helvetica", 30))
label.pack()

frame = ttk.Frame(app, height=300, width =300)
frame.pack(pady=10)

''' ############### INPUT VALUES #############'''
fonts = ['Arial', 'Comic Sans MS', 'Helvetica', 'Times New Roman']
colors = ['Red', 'Yellow', 'Orange', 'Green', 'Blue', 'Purple', 'Pink', "White", 'Brown', 'Black', 'Gray']


name_text = ttk.Label(frame, text='Name:', font=('Helvetica', 20))
name_text.grid(row=0, column=0, sticky='w')
name_entry = ttk.Entry(frame, textvariable=name, )
name_entry.grid(row=0, column=1, padx=3)

name_font_text = ttk.Label(frame, text='Font:', font=('Helvetica', 20))
name_font_text.grid(row=1, column=0, sticky='w')
name_font_entry = ttk.OptionMenu(frame, name_font, *fonts)
name_font_entry.grid(row=1, column=1, padx=3)

font_color = ttk.Label(frame, text='Name color:', font=('Helvetica', 20))
font_color.grid(row=2, column=0, sticky='w')
font_color_entry = ttk.OptionMenu(frame, name_color, *colors)
font_color_entry.grid(row=2, column=1, padx=3)

background_color_text = ttk.Label(frame, text='Background Color:', font=('Helvetica', 20))
background_color_text.grid(row=3, column=0, sticky='w')
background_color_entry = ttk.OptionMenu(frame, background_color, *colors)
background_color_entry.grid(row=3, column=1, padx=3)

border_color_text = ttk.Label(frame, text='Border Color:', font=('Helvetica', 20))
border_color_text.grid(row=4, column=0, sticky='w')
border_color_entry = ttk.OptionMenu(frame, border_color, *colors)
border_color_entry.grid(row=4, column=1, padx=3)

''' ############### PREVIEW ##################'''
name_tag = tk.Canvas(app, width=400, height=200, bg=background_color.get(),
                     highlightthickness=15, highlightbackground=border_color.get())
name_tag.pack()

def update_preview():
    name_tag.config(bg=background_color.get(), highlightbackground=border_color.get())
    name_tag.delete('all')
    name_tag.create_text(215, 115, text=name.get(), font=(name_font.get(), 40), fill=name_color.get())

update_preview()

''' ############### FUNCTIONS ################'''
def on_change(*args):
    update_preview()

name.trace_add("write", on_change)
name_font.trace_add("write", on_change)
name_color.trace_add("write", on_change)
background_color.trace_add("write", on_change)
border_color.trace_add("write", on_change)


app.mainloop()
