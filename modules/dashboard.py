import customtkinter as ctk


# ==========================================
# ADMIN DASHBOARD
# ==========================================

def open_dashboard(role):

    # Main Window
    dashboard = ctk.CTk()

    dashboard.title(f"{role.capitalize()} Dashboard")
    dashboard.geometry("1200x700")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")



    # ==========================================
    # SIDEBAR FRAME
    # ==========================================

    sidebar = ctk.CTkFrame(
        dashboard,
        width=250,
        corner_radius=0
    )

    sidebar.pack(side="left", fill="y")



    # ==========================================
    # LOGO / TITLE
    # ==========================================

    logo = ctk.CTkLabel(
        sidebar,
        text="QA Tracker",
        font=("Arial", 28, "bold")
    )

    logo.pack(pady=40)



    # ==========================================
    # NAVIGATION BUTTONS
    # ==========================================

    dashboard_btn = ctk.CTkButton(
        sidebar,
        text="Dashboard"
    )

    dashboard_btn.pack(pady=10, padx=20)



    defects_btn = ctk.CTkButton(
        sidebar,
        text="Defects"
    )

    defects_btn.pack(pady=10, padx=20)



    projects_btn = ctk.CTkButton(
        sidebar,
        text="Projects"
    )

    projects_btn.pack(pady=10, padx=20)



    reports_btn = ctk.CTkButton(
        sidebar,
        text="Reports"
    )

    reports_btn.pack(pady=10, padx=20)



    logout_btn = ctk.CTkButton(
        sidebar,
        text="Logout",
        fg_color="red",
        hover_color="darkred",
        command=dashboard.destroy
    )

    logout_btn.pack(side="bottom", pady=30)



    # ==========================================
    # MAIN CONTENT AREA
    # ==========================================

    main_frame = ctk.CTkFrame(
        dashboard
    )

    main_frame.pack(
        side="right",
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )



    # ==========================================
    # DASHBOARD TITLE
    # ==========================================

    heading = ctk.CTkLabel(
        main_frame,
        text=f"Welcome {role.capitalize()}",
        font=("Arial", 30, "bold")
    )

    heading.pack(pady=20)



    # ==========================================
    # STATISTICS CARDS
    # ==========================================

    cards_frame = ctk.CTkFrame(
        main_frame,
        fg_color="transparent"
    )

    cards_frame.pack(pady=20)



    # Total Defects Card
    total_defects = ctk.CTkFrame(
        cards_frame,
        width=200,
        height=120
    )

    total_defects.grid(row=0, column=0, padx=20)

    defects_label = ctk.CTkLabel(
        total_defects,
        text="Total Defects\n25",
        font=("Arial", 22, "bold")
    )

    defects_label.place(relx=0.5, rely=0.5, anchor="center")



    # Open Bugs Card
    open_bugs = ctk.CTkFrame(
        cards_frame,
        width=200,
        height=120
    )

    open_bugs.grid(row=0, column=1, padx=20)

    open_label = ctk.CTkLabel(
        open_bugs,
        text="Open Bugs\n10",
        font=("Arial", 22, "bold")
    )

    open_label.place(relx=0.5, rely=0.5, anchor="center")



    # Closed Bugs Card
    closed_bugs = ctk.CTkFrame(
        cards_frame,
        width=200,
        height=120
    )

    closed_bugs.grid(row=0, column=2, padx=20)

    closed_label = ctk.CTkLabel(
        closed_bugs,
        text="Closed Bugs\n15",
        font=("Arial", 22, "bold")
    )

    closed_label.place(relx=0.5, rely=0.5, anchor="center")



    dashboard.mainloop()