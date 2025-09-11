def display_image(self, img_path):
    try:
        img = tk.PhotoImage(file=img_path)
        if self.image_label:
            self.image_label.destroy()
        self.image_label = tk.Label(self.master, image=img)
        self.image_label.image = img
        self.image_label.place(x=750, y=280)
    except Exception:
        messagebox.showinfo("Error", "Image not found.")


import tkinter as tk
from travel_app import TravelGuideApp, get_initial_data, get_image_dict  # Adjust as per your module

def run_app():
    root = tk.Tk()
    root.geometry("1100x850")

    data = get_initial_data()         # Your function or static data to provide initial city info
    images = get_image_dict()         # Dictionary mapping city names to image paths

    app = TravelGuideApp(root, data, images)
    root.mainloop()


import auth_gui

# In your TravelGuideApp __init__ or setup_ui method:
login_button = tk.Button(self.master, text="Login", command=self.login_user)
login_button.place(x=50, y=50)

signup_button = tk.Button(self.master, text="Signup", command=self.signup_user)
signup_button.place(x=150, y=50)

# Add these methods in your TravelGuideApp class:

def login_user(self):
    user = auth_gui.show_login(self.master)
    if user:
        self.current_user = user
        # Optionally update UI to show logged-in user info or enable itinerary features

def signup_user(self):
    success = auth_gui.show_signup(self.master)
    if success:
        # Optionally auto-login or prompt user to log in
        pass



from data_manager import fetch_place
from api_integrations import get_weather
from tkinter import messagebox

def search_place(self):
    place_name = self.entry.get().strip().lower()
    if not place_name:
        messagebox.showwarning("Input Required", "Please enter a place name.")
        return

    result = fetch_place(place_name)
    if not result:
        self.info_text.delete(1.0, tk.END)
        if self.image_label:
            self.image_label.destroy()
        messagebox.showinfo("Not Found", "Place not found in database.")
        return

    # result format: (id, name, state, famous_places, hotels, details, image_path)
    _, name, state, famous_places, hotels, details, image_path = result

    output_text = (f"Place: {name}\n\nState: {state}\n\n"
                   f"Famous Places: {famous_places}\n\nHotels: {hotels}\n\nDetails: {details}\n\n")
    # Get real-time weather
    weather_info = get_weather(name)
    output_text += f"Current Weather: {weather_info}"

    self.info_text.delete(1.0, tk.END)
    self.info_text.insert(tk.END, output_text)

    # Display image
    if self.image_label:
        self.image_label.destroy()
    if image_path:
        try:
            img = tk.PhotoImage(file=image_path)
            self.image_label = tk.Label(self.master, image=img)
            self.image_label.image = img  # prevent GC
            self.image_label.place(x=750, y=280)
        except Exception:
            # If image load fails, silently ignore or show default image
            pass
