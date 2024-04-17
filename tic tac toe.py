import tkinter as tk
from tkinter import messagebox

class TikTacToe:
    def __init__(self) :
        self.current_player="x"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()

        self.buttonsgrid=[]
        for i in range(3):
          row=[]
        for j in range(3):
            button=tk.Button(self.window, text="",width=10,height=10)
            button.grid(row=i,column=j)
            row.append(button)
        self.buttonsgrid.append(row)
    
     
    def make_move(self,row,col):
        if self.board[row][col]=="":
           self.board[row][col]== self.current_player
           self.buttonsgrid[row][col].config(text=self.current_player)
           if self.check_winner(self.current_player):
              messagebox.showinfo("game over and the winner is"+self.current_player)
              self.window.quit()
           elif self.is_draw():
              messagebox.showinfo("game over and its draw")
              self.window.quit()
           self.current_player="o"if self.current_player=="x" else "x"

    def check_winner(self,player):
       for i in range(3):
          if player==self.board[i][0]==self.board[i][1]==self.board[i][2]:
             return True
          if player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
             return True
       if player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
          return True
       if player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
          return True
       return False
    
    def is_draw(self):
       for r in self.board:
          if "" in row:
               return False
          return True
          
        
    def run(self):
     self.wndow.mainloop()

game=TikTacToe()
game.run()

