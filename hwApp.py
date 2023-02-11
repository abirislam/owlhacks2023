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
        s3 = customtkinter.StringVar(value="Settings page")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=s3, width=650, height=370)
        self.label.grid(row=0, column=0, padx=20, pady=10)

        # Distance Drop-down
        combobox_var = customtkinter.StringVar(value="Max Distance")
        def combobox_callback(choice):
            return choice

        # combobox = customtkinter.CTkComboBox(master=self.tab("Settings"),
        # value=)

class App(customtkinter.CTk):
    # Setup
    def __init__(self):
        super().__init__()
        self.geometry("720x480")
        self.title("Clinical Trial Connector")

        # Tab View Setup
        self.tab_view = TabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=10, pady=10)

    
app = App()
app.mainloop()
