import tkinter as tk

HEIGHT = 768
WIDTH = 1024

root = tk.Tk()
background_green = '#BACEBF'
canvas = tk.Canvas(root,height= HEIGHT, width=WIDTH,bg=background_green)
canvas.pack()

background = tk.Frame(root,bg=background_green) 
background.place(relx = 0.5, rely = 0, relwidth=1, relheight=1, anchor='n')

lower_frame = tk.Frame(root, bg=background_green, bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

mainBox = tk.Label(lower_frame, font = ('Courier', 20),bg = '#DEE4DF')
mainBox.place(relwidth=2, relheight=2)

inputBoxDestinationCountry = tk.Frame(root, bg='#DEE4DF', bd=5)
inputBoxDestinationCountry.place(relx=0.52, rely = 0.55, relwidth=0.4, relheight=0.05, anchor='n')

destinationCountry = tk.Entry(inputBoxDestinationCountry, font=('Courier',40),bg='#9ECCD7')
destinationCountry.place(relwidth=1, relheight=1)

provinceLabelBox = tk.Frame(root, bg='#DEE4DF', bd=5)
provinceLabelBox.place(relx=0.25, rely = 0.55, relwidth=0.15, relheight=0.05, anchor='n')

provinceLabel = tk.Label(provinceLabelBox, font = ('Courier', 12), bg = '#DEE4DF', fg = '#333')
provinceLabel.place(relwidth = 1, relx = 0)
provinceLabel['text'] = "Country:"

inputBoxProvinceState = tk.Frame(root, bg='#DEE4DF', bd=5)
inputBoxProvinceState.place(relx=0.52, rely = 0.50, relwidth=0.4, relheight=0.05, anchor='n')

destinationProvince_State = tk.Entry(inputBoxProvinceState, font=('Courier',40),bg='#9ECCD7')
destinationProvince_State.place(relwidth=1, relheight=1)

destinationProvinceState = tk.Frame(root, bg='#DEE4DF', bd=5)
destinationProvinceState.place(relx=0.25, rely = 0.50, relwidth=0.15, relheight=0.05, anchor='n')

destinationProvinceStateLabel = tk.Label(destinationProvinceState, font = ('Courier', 12), bg = '#DEE4DF', fg = '#333')
destinationProvinceStateLabel.place(relwidth = 1, relx = 0)
destinationProvinceStateLabel['text'] = "Province/State:"

inputBoxDestinationCity = tk.Frame(root, bg='#DEE4DF', bd=5)
inputBoxDestinationCity.place(relx=0.52, rely = 0.45, relwidth=0.4, relheight=0.05, anchor='n')

destenationCity = tk.Entry(inputBoxDestinationCity, font=('Courier',40),bg='#9ECCD7')
destenationCity.place(relwidth=1, relheight=1)

destenationCityBox = tk.Frame(root, bg='#DEE4DF', bd=5)
destenationCityBox.place(relx=0.25, rely = 0.45, relwidth=0.15, relheight=0.05, anchor='n')

destenationCityLabel = tk.Label(destenationCityBox, font = ('Courier', 12), bg = '#DEE4DF', fg = '#333')
destenationCityLabel.place(relwidth = 1, relx = 0)
destenationCityLabel['text'] = "City:"


titleFrame = tk.Frame(root, bg='#DEE4DF', bd=5)
titleFrame.place(relx=0.5, rely = 0.15, relwidth=0.30, relheight=0.05, anchor='n')

titleLabel = tk.Label(titleFrame, font = ('Courier', 16), bg = '#DEE4DF', fg = '#333')
titleLabel.place(relwidth = 1, relx = 0)
titleLabel['text'] = "Where would you like to go?"


def enter(a,z,x):
    print('Enter')
    print(a,z,x)
    
updateButtonFrame = tk.Frame(root, bg='#333', bd=5)
updateButtonFrame.place(relx=0.5, rely=0.70, relwidth=0.2, relheight=0.1, anchor='n')

updateButton = tk.Button(updateButtonFrame, text= "Enter", bg='#DEE4DF', fg='black', font=('Courier',20), command=lambda: enter(destinationCountry.get(), destenationCity.get(), destinationProvince_State.get()))
updateButton.place(relheight=1, relwidth=1)

  

root.mainloop()
