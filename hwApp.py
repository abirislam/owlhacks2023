import customtkinter
from mapbox import Geocoder
from mapbox import Static
from PIL import Image, ImageTk
import mysql.connector

class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        def button_event():
            geocoder = Geocoder(access_token="pk.eyJ1IjoibmlhemJhaGFydWRlZW4iLCJhIjoiY2xlMGU2bjM3MWE2dTN1cHJkM3BscXp6aiJ9.K-YtZmHEZGjepLN68F9OZA")
            service = Static(access_token="pk.eyJ1IjoibmlhemJhaGFydWRlZW4iLCJhIjoiY2xlMGU2bjM3MWE2dTN1cHJkM3BscXp6aiJ9.K-YtZmHEZGjepLN68F9OZA")
            address = self.address_entry.get()
            response = geocoder.forward(address)
            # print(response.url)
            longlat = response.geojson()['features'][0]
            long = longlat['center'][0]
            lat = longlat['center'][1]

            map_image = service.image('mapbox.satellite', lon=long, lat=lat, z=15)
            map_image.headers['Content-Type']

            with open('./map.png', 'wb') as output:
                mapimage = output.write(map_image.content)

            static_map = Image.open("./map.png")
            my_img = customtkinter.CTkImage(dark_image = static_map, size=(700,400))    
            button = customtkinter.CTkButton(master=self.tab("Connector"), image=my_img, text="")
            button.grid(row=2, column=0)


        # Tabs
        self.add("Connector")
        self.add("Profile")
        self.add("Settings")

        # 'Connector' Widgets

        address_bar = customtkinter.StringVar(value="Address:")
        self.label = customtkinter.CTkLabel(master=self.tab("Connector"), textvariable=address_bar)
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.address_entry = customtkinter.CTkEntry(master=self.tab("Connector"), width=120, height=25, corner_radius=1)
        self.address_entry.grid(row=0, column=1, padx=0, pady=0)
        self.address = customtkinter.StringVar(value="")
        self.button = customtkinter.CTkButton(master=self.tab("Connector"), width=25, height=25, border_width=0, corner_radius=8, text=">", command=button_event)
        self.button.grid(row=0, column=2, padx=0, pady=0)

        # 'Profile' Widgets
        # 'Profile' Login Form
        usernameLabel = customtkinter.StringVar(value="Username: ")
        self.label = customtkinter.CTkLabel(master=self.tab("Profile"), textvariable=usernameLabel)
        self.label.grid(row=0, column=0, padx=20, pady=10)
        usernameEntry = customtkinter.CTkEntry(master=self.tab("Profile"), placeholder_text="Username here")
        usernameEntry.grid(row=0, column=1)
        passwordLabel = customtkinter.StringVar(value="Password: ")
        self.label = customtkinter.CTkLabel(master=self.tab("Profile"), textvariable=passwordLabel)
        self.label.grid(row=1, column=0, padx=20, pady=10)
        passwordEntry = customtkinter.CTkEntry(master=self.tab("Profile"), placeholder_text="Password here", show="*")
        passwordEntry.grid(row=1, column=1)

        # 'Profile' Login
        def login_button():
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='T_T',
                port='3306',
                database='owlhacks2023'
            )

            c = connection.cursor()
            search = "SELECT * FROM userdata WHERE username ='" + usernameEntry.get() + "' " + "AND password ='" + passwordEntry.get() + "'"
            c.execute(search)
            george = self.label1 = customtkinter.CTkLabel(master=self.tab("Profile"), text="")
            george.grid(row=3, column=1, padx=20, pady=20)
            personalInfo = self.label = customtkinter.CTkLabel(master=self.tab("Profile"), text="")
            personalInfo.grid(row=4, column=1)

            if(c.fetchall()):
                print("login success")
                george.configure(text="Login Success!")
                personalInfo.configure(text="Here are the clinical trials you are currently looking for:")
            else:
                print("login failed")
                george.configure(text="Invalid Credentials")

            
        button = customtkinter.CTkButton(master=self.tab("Profile"), text="Login", command=login_button)
        button.grid(row=2, column=1, pady=10)

        


        # 'Settings' Widgets
        categoryLabel = customtkinter.StringVar(value="Local Settings")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=categoryLabel)
        self.label.grid(row=0, column=0, padx=20)

        # 'Settings' - Language Selector
        language = customtkinter.StringVar(value="App Language")
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

        # 'Settings' - Distance Selector
        maxDistance = customtkinter.StringVar(value="Max Distance")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=maxDistance)
        self.label.grid(row=2, column=0, padx=20, pady=10)

        combobox_var = customtkinter.StringVar(value="25 miles")
        def combobox_callback(choice):
            return choice
        combobox = customtkinter.CTkComboBox(master=self.tab("Settings"),
            values=["25 miles", "50 miles", "75 miles", "100 miles"],
            command=combobox_callback,
            variable=combobox_var)
        combobox.grid(row=2, column=1, pady=10)

        # 'Settings' - Toll Switch
        toll_title = customtkinter.StringVar(value="Toll-free")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=toll_title)
        self.label.grid(row=3, column=0, padx=20, pady=10)

        tollSwitch = customtkinter.StringVar(value="on")
        def tollSwitchEvent():
            return tollSwitch.get()
        tollSwitchOption = customtkinter.CTkSwitch(master=self.tab("Settings"), text="",
            command=tollSwitchEvent, 
            variable=tollSwitch, onvalue="on", offvalue="off")
        tollSwitchOption.grid(row=3, column=1)


        # 'Settings' Doctor Options
        doctorLabel = customtkinter.StringVar(value="Doctor Preferences")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=doctorLabel)
        self.label.grid(row=0, column=3, padx=20)

        # Doctor Language Preference
        doctorLanguageLabel = customtkinter.StringVar(value="Language")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=doctorLanguageLabel)
        self.label.grid(row=1, column=3, padx=20)


        doctor_langugage_selector = customtkinter.StringVar(value="English")
        def doctor_language_callback(choice):
            return choice
        doctor_language_box = customtkinter.CTkComboBox(master=self.tab("Settings"),
        values=["English", "Spanish", "German", "French"],
            command=doctor_language_callback,
            variable=doctor_langugage_selector)
        doctor_language_box.grid(row=1, column=4)

        # Doctor Gender Preference
        doctorGenderLabel = customtkinter.StringVar(value="Gender")
        self.label = customtkinter.CTkLabel(master=self.tab("Settings"), textvariable=doctorGenderLabel)
        self.label.grid(row=2, column=3, padx=20)

        doctor_gender_selector = customtkinter.StringVar(value="Any")
        def doctor_gender_callback(choice):
            return choice
        doctor_gender_box = customtkinter.CTkComboBox(master=self.tab("Settings"),
        values=["Male", "Female", "Either", "Any"],
            command=doctor_gender_callback,
            variable=doctor_gender_selector)
        doctor_gender_box.grid(row=2, column=4)


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
