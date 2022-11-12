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

# updateButtonFrame = tk.Frame(root, bg=background_green, bd=5)
# updateButtonFrame.place(relx=1.1, rely=0.05, relwidth=1, relheight=0.1, anchor='n')

# updateButton = tk.Button(updateButtonFrame, text= "Get Voting Results", bg='#5390D9', fg='black', font=('Courier',20), command=lambda : updateVote(voterDatabase))
# updateButton.place(relheight=1, relwidth=0.3)

inputBoxUsername = tk.Frame(root, bg=background_green, bd=5)
inputBoxUsername.place(relx=0.5, rely = 0.05, relwidth=0.4, relheight=0.05, anchor='n')

username = tk.Entry(inputBoxUsername, font=('Courier',40),bg='#73B0F9')
username.place(relwidth=1, relheight=1)

inputBoxProvince = tk.Frame(root, bg=background_green, bd=5)
inputBoxProvince.place(relx=0.5, rely = 0.1, relwidth=0.4, relheight=0.05, anchor='n')

province = tk.Entry(inputBoxProvince, font=('Courier',40),bg='#73B0F9')
province.place(relwidth=1, relheight=1)

provinceLabelBox = tk.Frame(root, bg=background_green, bd=5)
provinceLabelBox.place(relx=0.25, rely = 0.11, relwidth=0.1, relheight=0.05, anchor='n')

votePartyLabel = tk.Label(provinceLabelBox, font = ('Courier', 10), bg = background_green)
votePartyLabel.place(relwidth = 1, relx = 0)
votePartyLabel['text'] = "Province:"

inputBoxCurrentCountry = tk.Frame(root, bg='#DEE4DF', bd=5)
inputBoxCurrentCountry.place(relx=0.5, rely = 0.55, relwidth=0.4, relheight=0.05, anchor='n')

currentCountry = tk.Entry(inputBoxCurrentCountry, font=('Courier',40),bg='#73B0F9')
currentCountry.place(relwidth=1, relheight=1)

currentCountry = tk.Frame(root, bg=background_green, bd=5)
currentCountry.place(relx=0.23, rely = 0.15, relwidth=0.1, relheight=0.05, anchor='n')

currentCountryLabel = tk.Label(currentCountry, font = ('Courier', 10), bg = background_green)
currentCountryLabel.place(relwidth = 1, relx = 0)
currentCountryLabel['text'] = "Current Country:"

inputBoxDestinationCountry = tk.Frame(root, bg='#DEE4DF', bd=5)
inputBoxDestinationCountry.place(relx=0.5, rely = 0.60, relwidth=0.4, relheight=0.05, anchor='n')

destenationCountry = tk.Entry(inputBoxDestinationCountry, font=('Courier',40),bg='#73B0F9')
destenationCountry.place(relwidth=1, relheight=1)

# destinationCountry = tk.Frame(root, bg=background_green, bd=5)
# destenationCountry.place(relx=0.30, rely = 0.50, relwidth=0.15, relheight=0.06, anchor='n')

# destinationCountryLabel = tk.Label(currentCountry, font = ('Courier', 10), bg = background_green)
# destinationCountryLabel.place(relwidth = 1, relx = 0)
# destinationCountryLabel['text'] = "Destenation Country:"



usernameLabelBox = tk.Frame(root, bg=background_green, bd=5)
usernameLabelBox.place(relx=0.25, rely = 0.06, relwidth=0.1, relheight=0.05, anchor='n')

usernameLabel = tk.Label(usernameLabelBox, font = ('Courier', 10), bg = background_green)
usernameLabel.place(relwidth = 1, relx = 0)
usernameLabel['text'] = "Closest City:"

titleFrame = tk.Frame(root, bg=background_green, bd=5)
titleFrame.place(relx=0.5, rely = 0, relwidth=0.25, relheight=0.05, anchor='n')

# titleLabel = tk.Label(titleFrame, font = ('Courier', 14), bg = background_green)
# titleLabel.place(relwidth = 1, relx = 0)
# titleLabel['text'] = "Vote For a Candidate!"

# inputButtonFrame = tk.Frame(root, bg=background_green, bd=5)
# inputButtonFrame.place(relx=0.3, rely=0.175, relwidth=0.35, relheight=0.05, anchor='n')

# loginButton = tk.Button(inputButtonFrame, text= "Authenticate and Vote!", bg='#5390D9', fg='black', font=('Courier',20), command=lambda : authenticateAndVote(username.get(), voteParty.get(), voterDatabase))
# loginButton.place(relheight=1, relwidth=1)


root.mainloop()
