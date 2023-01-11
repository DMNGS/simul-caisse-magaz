# Script      : frm_settings.py
# Description : Simulation settings window
# Author      : DOMINGUES PEDROSA Samuel
# Date        : 2022.12.21, V1.0

window_settings = Tk()
window_settings.title('Simulateur de caisses')
window_settings.geometry('900x600')
window_settings.resizable(False, False)

frm_settings = ttk.Frame(window_settings, padding=10)
frm_settings.grid()

ttk.Label(frm_settings, text="Hello World!").grid(column=5, row=0)
ttk.Button(frm_settings, text="Quit", command=window_settings.destroy).grid(column=1, row=0)

window_settings.mainloop()