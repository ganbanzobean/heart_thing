from tkinter import *
root = Tk()
root.title("Heart_Report")
root.geometry("400x400")

question1_radioButton=StringVar(value="0")

question1=Label(root, text ="Do youe experience shortness of breath while doing routine activities?")
question1.pack()
question1_r1=Radiobutton(root, text = "Yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "No", variable=question1_radioButton, value="no")
question1_r2.pack()

question2_radioButton=StringVar(value="0")
question2=Label(root, text ="Do you have swelling in the feet/legs/ankles(shoes feel tighter) or in the abdomen?")
question2.pack()
question2_r1=Radiobutton(root, text = "Yes", variable=question2_radioButton, value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root, text = "No", variable=question2_radioButton, value="no")
question2_r2.pack()

question3_radioButton=StringVar(value="0")
question3=Label(root, text ="Do you feel any of there symptoms - confusion, disorientation, or loss of memory?")
question3.pack()
question3_r1=Radiobutton(root, text = "Yes", variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "No", variable=question3_radioButton, value="no")
question3_r2.pack()

question4_radioButton=StringVar(value="0")
question4=Label(root, text ="Do you experience shortness of breath while sitting/lying down?")
question4.pack()
question4_r1=Radiobutton(root, text = "Yes", variable=question4_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root, text = "No", variable=question4_radioButton, value="no")
question4_r2.pack()

question5_radioButton=StringVar(value="0")
question5=Label(root, text ="Do you experience persistent wheezing/coughing that produces white or pink blood-tinged mucus?")
question5.pack()
question5_r1=Radiobutton(root, text = "Yes", variable=question5_radioButton, value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root, text = "No", variable=question5_radioButton, value="no")
question5_r2.pack()

def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+20
        print(score)

    if score <= 20:
        print("Report","You don't need to visit a doctor.")
    elif  score > 20 and score <= 60: 
        print("Report","You might perhaps have to visit a doctor")
    else :
        print("Report","I strongly advise you to visit a doctor")
btn = Button(root, text= "click me", command= fever_score)
btn.pack()
root.mainloop()