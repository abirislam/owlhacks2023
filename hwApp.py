import customtkinter
from bs4 import BeautifulSoup

class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Tabs
        self.add("Connector")
        self.add("Messages")
        self.add("Profile")
        self.add("Settings")

        # 'Connector' Widgets
        s1 = customtkinter.StringVar(value="Connector homepage")
        self.label = customtkinter.CTkLabel(master=self.tab("Connector"), textvariable=s1, width=650, height=370)
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # 'Messages' Widgets
        messageDisplay = customtkinter.StringVar(value="Messages display")
        self.label = customtkinter.CTkLabel(master=self.tab("Messages"), textvariable=messageDisplay, width=650, height=370)
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # 'Profile' Widgets
        s2 = customtkinter.StringVar(value="Profile display")
        self.label = customtkinter.CTkLabel(master=self.tab("Profile"), textvariable=s2, width=650, height=370)
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # 'Settings' Widgets
        categoryLabel = customtkinter.StringVar(value="Local Settings")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=categoryLabel)
        self.label.grid(row=0, column=0, padx=20)

        # 'Settings' - Language Selector
        language = customtkinter.StringVar(value="Language Selection")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=language)
        self.label.grid(row=1, column=0, padx=20)

        langugage_selector = customtkinter.StringVar(value="English")
        def language_callback(choice):
            return choice
        language_box = customtkinter.CTkComboBox(master=self.tab("Settings"),
        values=["English", "Spanish", "German", "French"],
            command=language_callback,
            variable=langugage_selector)
        language_box.grid(row=1, column=1)


        maxDistance = customtkinter.StringVar(value="Max Distance")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=maxDistance)
        self.label.grid(row=2, column=0, padx=20, pady=10)

        # Distance Drop-down
        combobox_var = customtkinter.StringVar(value="25 miles")
        def combobox_callback(choice):
            return choice

        combobox = customtkinter.CTkComboBox(master=self.tab("Settings"),
            values=["25 miles", "50 miles", "75 miles", "100 miles"],
            command=combobox_callback,
            variable=combobox_var)
        combobox.grid(row=2, column=1, pady=10)


        # 'Settings' Doctor Options
        doctorLabel = customtkinter.StringVar(value="Doctor Preferences")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=doctorLabel)
        self.label.grid(row=0, column=3, padx=20)

        # Doctor Language Preference

class App(customtkinter.CTk):
    # Setup
    def __init__(self):
        super().__init__()
        self.geometry("1300x740")
        self.title("Clinical Trial Connector")

        # Tab View Setup
        self.tab_view = TabView(master=self, width=1280, height=720)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)

    
app = App()
app.mainloop()
