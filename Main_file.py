from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import tkinter.messagebox
import speech_recognition as sr
import pyttsx3
import pygame
import webbrowser
import random
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
rootp=Tk()
rootp.title("Welcome Page")
rootp.geometry("600x470")
rootp.resizable(False,False)
Label(rootp,text='Welcome',relief='ridge',font='times 25 bold italic',fg='blue').pack()
rootp.config(bg='Light sea green')

#all functions are listed here
def music():
    rootp.withdraw()
    nw1=Tk()
    nw1.title("Discover Music")
    nw1.geometry("697x250+300+220")
    nw1.resizable(False,False)

    pygame.init()
    #Initiating Pygame Mixer
    pygame.mixer.init()
    #Declaring track Variable
    track=StringVar()
    #Declaring Status Variable
    status = StringVar()

    #For playing,pausing and stopping of the song
    def play():
        try:
            # Displaying Selected Song title
            track.set(playlist.get(ACTIVE))
            # Loading Selected Song
            pygame.mixer.music.load(playlist.get(ACTIVE))
        except:
            tkinter.messagebox.showerror("Error","Cannot play any song, not selected")
            pass
    
        track.set(playlist.get(ACTIVE))
        pygame.mixer.music.load(playlist.get(ACTIVE))
        # Displaying Status
        status.set("-Playing")
    
    
        # Playing Selected Song
        pygame.mixer.music.set_volume(0.1)
        #print(pygame.mixer.music.get_volume())
        pygame.mixer.music.play(-1)
        pausebtn['text'] = "PAUSE"

    def pause():
        # pause
        unpause = True
        if(unpause):
            # Displaying Status
            status.set("-Paused")
            pausebtn['text'] = "PAUSED"
            # Paused Song
            pygame.mixer.music.pause()
            unpause = False

    def stop():
        status.set("-Stopped")
    
        # Stopped Song
        pygame.mixer.music.stop()

    def openl():
        path = filedialog.askdirectory()
        #Changing Directory for fetching Songs    

        try:
            os.chdir(path)
        except:
            tkinter.messagebox.showerror("Error","You didn't select any folder")

        #Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        playlist.delete(0,END)
        for track in songtracks:
            if track.endswith('.mp3'):
                playlist.insert(END, track)

    def homebtn():
        nw1.withdraw()
        rootp.deiconify()
            
    # For frame
    track_frame = LabelFrame(nw1,text="Song Track",font=("times new roman",15,"bold"),bg="blue",fg="white",bd=5,relief=GROOVE)    
    track_frame.place(x=0,y=0,width=400,height=100)
   
    songtrack = Label(track_frame, textvariable=track,width=23, font=("times new roman",15,"bold"),bg="blue", fg="gold")
    songtrack.place(x=0,y=10)

    # Inserting Status Label
    trackstatus = Label(track_frame, textvariable=status,width=10, font=("times new roman", 15, "bold"), bg="blue",fg="gold")
    trackstatus.place(x=280,y=10)

    # Creating Button Frame
    buttonframe = LabelFrame(nw1, text="Control Panel", font=("times new roman", 15, "bold"), bg="blue",fg="white", bd=5, relief=GROOVE)
    buttonframe.place(x=0, y=100, width=400, height=150)

    # Inserting Play Button
    playbtn = Button(buttonframe, text="PLAY", command=play, width=8, height=1,font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
    playbtn.place(x=20,y=15)

    # Inserting Pause Button
    pausebtn = Button(buttonframe, text="PAUSE", command=pause, width=8, height=1,font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
    pausebtn.place(x=150,y=15)

    # Inserting Stop Button
    stopbtn = Button(buttonframe, text="STOP", command=stop, width=8, height=1,font=("times new roman", 12, "bold"), fg="navyblue", bg="gold")
    stopbtn.place(x=280,y=15)

    #Inserting Open Button
    openbtn=Button(buttonframe, text="Open",command=openl, width=8, height=1,font=("times new roman", 14, "bold"), fg="black", bg="white")
    openbtn.place(x=80,y=70)

    exitbtn=Button(buttonframe,text="Home",command=homebtn ,width=8,height=1,font=("times new roman", 14, "bold"), fg="black", bg="white")
    exitbtn.place(x=200,y=70)

    #Creating Playlist Frame
    songsframe = LabelFrame(nw1, text="Song Playlist", font=("times new roman", 15, "bold"), bg="blue",fg="white", bd=5, relief=GROOVE)
    songsframe.place(x=400, y=0, width=300, height=250)

    #Inserting scrollbar
    scrol_y=Scrollbar(songsframe, orient=VERTICAL)

    #Inserting Playlist listbox
    playlist=Listbox(songsframe,yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE, font=("times new roman", 12, "bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)

    #Applying Scrollbar to listbox
    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=playlist.yview)
    playlist.pack(fill=BOTH)

    nw1.mainloop()


def browser():
    rootp.withdraw()
    nw2=Toplevel()
    nw2.title("Welcome to the Browser")
    nw2.geometry("400x350")
    nw2.resizable(False,False)
    Label(nw2,text='WELCOME TO NP ASSISSTANT',relief='ridge',font='times 18 bold italic',fg='black',bg="CadetBlue1").pack()
    photo = PhotoImage(file='microphone.png').subsample(10,10)
    btn=StringVar()
    def buttonClick():
        pygame.init()
        pygame.mixer.music.load('chime1.mp3')
        pygame.mixer.music.play()

        r = sr.Recognizer()
        r.pause_threshold = 0.7
        r.energy_threshold = 400
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        def talk(text):
            engine.say(text)
            engine.runAndWait()
        

        with sr.Microphone() as source:
            try:
                audio = r.listen(source, timeout=10)
                message = str(r.recognize_google(audio))
                pygame.mixer.music.load('chime2.mp3')
                pygame.mixer.music.play()
                
                if btn.get() == 'google':
                    webbrowser.open('http://google.com/search?q='+message)
        
                elif btn.get() == 'you':
                    webbrowser.open('https://www.youtube.com/results?search_query='+message)

                else:
                    pass
            except sr.UnknownValueError:
                talk('Google Speech Recognition could not understand audio')

            except sr.RequestError as e:
                talk('Could not request results from Google Speech Recognition Service')

            else:
                pass
        nw2.withdraw()
        rootp.deiconify()
        
    def homeb():
        nw2.withdraw()
        rootp.deiconify()
            

    r1=Radiobutton(nw2, text='Google', value='google',variable=btn,bg="CadetBlue1")
    r1.place(x=90,y=240)
    r2=Radiobutton(nw2, text='Youtube', value='you',variable=btn,bg="CadetBlue1")
    r2.place(x=230,y=240)
    
    b6=Button(nw2,image=photo,command=buttonClick,bd=0,activebackground='#c1bfbf', overrelief='groove', relief='sunken',bg="CadetBlue1")
    b6.place(x=170,y=100)
    Label(nw2,text="Click me!!!", font="arial 9 bold",fg="black",bg="CadetBlue1").place(x=170,y=190)
    b11=Button(nw2,text="Home", font="arial 9",command=homeb)
    b11.place(x=180,y=285)
    nw2.config(bg="CadetBlue1")
    btn.set('google')
    nw2.mainloop()



def analyser():
    rootp.withdraw()
    nw3=Tk()
    nw3.title("Sentiment Detector")
    nw3.geometry("300x325")
    nw3.configure(bg='#00003c')
    nw3.resizable(False,False)

    def detect():
        sentence=e1.get()
        t1.delete(0.0,END)
        sid_obj=SentimentIntensityAnalyzer()
        sentiment_dict=sid_obj.polarity_scores(sentence)
        negative_string=str(sentiment_dict['neg']*100) + "% Negative"
        t1.insert(END,negative_string+'\n')
        neutral_string=str(sentiment_dict['neu']*100) + "% Neutral"
        t1.insert(END,neutral_string+'\n')
        positive_string=str(sentiment_dict['pos']*100) + "% Positive"
        t1.insert(END,positive_string+'\n')

        if sentiment_dict['compound']>=0.05:
            string="Positive"
        elif sentiment_dict['compound']<=-0.05:
            string="Negative"
        else:
            string="Neutral"
        t1.insert(END,f"Overall Result : {string}")
    def home22():
        nw3.withdraw()
        rootp.deiconify()
                          
    e1=Entry(nw3,width=20,font=('arial',14))
    e1.place(x=5,y=20)
    b10=Button(nw3,text="Analyse",bg='#201d2e',width=6,fg='white',font=('Arial',10),command=detect)
    b10.place(x=232,y=20)

    frame2=Frame(nw3,bd=2,relief=RIDGE,bg='#201d2e')
    frame2.place(x=10,y=70,height=250,width=280)

    l1=Label(frame2,text="Result",bg='#201d2e',fg='white',font=('arial',12,'bold'))
    l1.place(x=10,y=5)

    t1=Text(frame2,bd=2,relief=SUNKEN,font=('Calibri',12,'bold'))
    t1.place(x=10,y=30,width=255,height=150)

    b22=Button(frame2, text='HOME',font= ('artal', 10, 'bold'),fg='#ffffff',bg='#201d2e',command=home22)
    b22.place(x=110,y=210)

    nw3.mainloop()



def game():
    rootp.withdraw()
    nw4=Tk()
    nw4.title("Game")
    nw4.geometry("550x300")
    nw4.resizable(False,False)
    nw4.config(bg="DeepSkyBlue2")
    computer_value={"0":"Rock","1":"Paper","2":"Scissor"}
    def reset_game():
        b7["state"]="active"
        b8["state"]="active"
        b9["state"]="active"
        l1.config(text="Player         ")
        l3.config(text="Computer")
        l4.config(text="")

    def button_disable():
        b7["state"]="disable"
        b8["state"]="disable"
        b9["state"]="disable"

    def isrock():
        c_v=computer_value[str(random.randint(0,2))]
        if c_v=="Rock":
            match_result="Match Draw"
        elif c_v=="Scissor":
            match_result="Player Win"
        else:
            match_result="Computer Win"
        l4.config(text=match_result)
        l1.config(text="Rock         ")
        l3.config(text=c_v)
        button_disable()

    def ispaper():
        c_v=computer_value[str(random.randint(0,2))]
        if c_v=="Paper":
            match_result="Match Draw"
        elif c_v=="Scissor":
            match_result="Computer Win"
        else:
            match_result="Player Win"
        l4.config(text=match_result)
        l1.config(text="Paper         ")
        l3.config(text=c_v)
        button_disable()

    def isscissor():
        c_v=computer_value[str(random.randint(0,2))]
        if c_v=="Rock":
            match_result="Computer Win"
        elif c_v=="Scissor":
            match_result="Match Draw"
        else:
            match_result="Player Win"
        l4.config(text=match_result)
        l1.config(text="Scissor         ")
        l3.config(text=c_v)
        button_disable()

    def homebt():
        nw4.withdraw()
        rootp.deiconify()

    Label(nw4,text="Rock Paper Scissor",font="normal 20 bold",fg="blue",bg="DeepSkyBlue2").pack(pady=20)
    frame=Frame(nw4)
    frame.pack()

    l1=Label(frame,text="Player         ",font=10,bg="DeepSkyBlue2")
    l2=Label(frame,text="VS             ",font="normal 10 bold",bg="DeepSkyBlue2")
    l3=Label(frame,text="Computer   ",font=10,bg="DeepSkyBlue2")
    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4=Label(nw4,text="",font="normal 20 bold",width=15,borderwidth=2,relief="solid",bg="DeepSkyBlue2")
    l4.pack(pady=20)
    frame1=Frame(nw4)
    frame1.pack()

    b7=Button(nw4,text="Rock",font=10,width=7,command=isrock,bg="DeepSkyBlue2")
    b8=Button(nw4,text="Paper",font=10,width=7,command=ispaper,bg="DeepSkyBlue2")
    b9=Button(nw4,text="Scissor",font=10,width=7,command=isscissor,bg="DeepSkyBlue2")
    b7.place(x=120,y=190)
    b8.place(x=225,y=190)
    b9.place(x=330,y=190)

    Button(nw4,text="Reset Game",font=10,fg="white",command=reset_game,bg="DeepSkyBlue2").place(x=145,y=240)
    Button(nw4,text="Home",font=8,fg="white",bg="DeepSkyBlue2",command=homebt).place(x=315,y=240)
        
    nw4.mainloop()



def exit():
    rootp.withdraw()



b1=Button(rootp,text="Listen to music",fg="blue",font='times 13 bold',command=music,overrelief='groove', relief='sunken')
b1.place(x=50,y=85)
b1.config(height=4,width=22)
b2=Button(rootp,text="Search on Web Browser",fg="blue",font='times 13 bold',command=browser)
b2.place(x=320,y=85)
b2.config(height=4,width=22)
b3=Button(rootp,text="Get your Text Analysed",fg="blue",font='times 13 bold',command=analyser)
b3.place(x=50,y=210)
b3.config(height=4,width=22)
b4=Button(rootp,text="Bored? Play a Game!",fg="blue",font='times 13 bold',command=game)
b4.place(x=320,y=210)
b4.config(height=4,width=22)
b5=Button(rootp,text="Exit",fg="red",font='times 10 bold',command=exit)
b5.place(x=250,y=335)
b5.config(height=2,width=10)

rootp.mainloop()
