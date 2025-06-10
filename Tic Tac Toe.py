import tkinter #tk-interface (gui)

d = {}
def set_tile(row,column):
    global curr_player

    x= [row, column]
    d.update({turn : x})


    if turn>=5:
        board[d[turn - 5][0]][d[turn - 5][1]].config(foreground=color_l_blue)

    if turn>=6:
        board[d[turn - 6][0]][d[turn - 6][1]]["text"] = ""


    if game_over:
        return

    if board[row][column]["text"] != "":
        return

    if board[row][column]["text"] == "" :
        board[row][column].config(foreground=color_blue)

    board[row][column]["text"]= curr_player

    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player =playerO

    label["text"]= curr_player +"'s turns"


    check_winner()

def check_winner():
    global turn,game_over
    turn +=1





    for row in range (3):
        if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"]and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] +" is winner ",foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background = color_light_gray)
            game_over = True
            return

    for column in range (3):
        if (board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"]and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] +" is winner ",foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background = color_light_gray)
            game_over = True
            return

    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is winner ", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return

    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is winner ", foreground=color_yellow)
        for i in range(3):
            board[i][2-i].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return


def new_game():
   global turn,game_over

   turn =0
   game_over =False

   label.config(text=curr_player+"'s turns",foreground="white")

   for row in range(3):
       for column in range(3):
           board[row][column].config(text="", foreground=color_blue,background= color_gray)

#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board =[[0,0,0],
        [0,0,0],
        [0,0,0]]
 

color_blue ="#0000FF"
color_l_blue = "#d0eaff"
color_yellow = "#ffde57"
color_gray =  "#343434"
color_light_gray = "#646464"


turn = 0
game_over = False


window = tkinter.Tk()
window.title("TIC TAC TOE")
window.resizable(False,False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text= curr_player+ "'s turns",font=("Concolas",20), background= color_gray,
                      foreground="white")

label.grid(row = 0 , column= 0,columnspan=3,sticky="we")


for row in range(3):
    for column in range (3):

        board[row][column] = tkinter.Button(frame, text="", font=("Consolas" ,50 ,"bold"), 
                                            background=color_gray,foreground=color_blue ,width=4,height=1,
                                            command=lambda row=row ,column=column : set_tile(row,column))
        board[row][column].grid(row = row+1, column=column)
button = tkinter.Button(frame,text="restart",font= ("Consolas", 20 ),background=color_gray,
                        foreground="white",command=new_game)

button.grid(row = 4 , column= 0,columnspan=3,sticky="we")

frame.pack()


window.mainloop()



