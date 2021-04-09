import json
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class Student:
    def __init__(self, gender, nationality, placeOfBirth, subject, raisedHands, visitedResources, viewedAnnouncements):
        self.gender = gender
        self.nationality = nationality
        self.placeOfBirth = placeOfBirth
        self.subject = subject
        self.raisedHands = raisedHands
        self.visitedResources = visitedResources
        self.viewedAnnouncements = viewedAnnouncements
    
    def GetStudentInfo(self):
        return f'\nGender: {self.gender} \
            \nNationality: {self.nationality} \
            \nPlace of birth: {self.placeOfBirth} \
            \nRaised hands: {self.raisedHands} \
            \nVisited resources: {self.visitedResources} \
            \nViewed announcements: {self.viewedAnnouncements}'
    
class DataConverter():
    @staticmethod   
    def ConvertJsonToObject(fileName):
        students = []

        with open(fileName) as dataFile:
            jsonData = json.load(dataFile)

            for value in jsonData:
                gender = value['gender']
                nationality = value['NationalITy']
                placeOfBirth = value['PlaceofBirth']
                subject = value['Topic']
                raisedHands = value['raisedhands']
                visitedResources = value['VisITedResources']
                viewedAnnouncements = value['AnnouncementsView']

                student = Student(gender, nationality, placeOfBirth, subject, raisedHands, visitedResources, viewedAnnouncements)
                students.append(student)
        
        return students

class Calculations():
    @staticmethod
    def GetGenderCount(students):
        maleNumber = 0
        femaleNumber = 0

        for student in students:
            if(student.gender == 'M'):
                maleNumber += 1
            else:
                femaleNumber += 1
        
        print(f'\nNumber of males: {maleNumber} \nNumber of females: {femaleNumber}')

    @staticmethod
    def GetNationalities(students):
        nationalities = []

        for student in students:
            if student.nationality not in nationalities:
                nationalities.append(student.nationality)

        for n in nationalities:
            print(f'\n{n}')    

    @staticmethod
    def GetRaisedHandsForAboveSetNumber(number, students):
        numberOfPeople = 0
        numberOfPeopleAbove = 0

        for student in students:
            if(int(student.raisedHands) >= int(number)):
                numberOfPeopleAbove += 1

            numberOfPeople += 1

        text = f'\nOut of {numberOfPeople} people\n{numberOfPeopleAbove} of them raised hand more than {number} times.'
        NewWindow(text=text)

    @staticmethod
    def GetStudentsInfo(students):
        studentsInfo = []

        for student in students:
            studentsInfo.append((student.gender, 
            student.nationality, 
            student.placeOfBirth, 
            student.subject, 
            student.raisedHands,
            student.visitedResources,
            student.viewedAnnouncements))
        
        NewWindow(values=studentsInfo)     

    @staticmethod
    def GetMaleFemaleShareForRaisedHands(students):
        maleSum = 0
        femaleSum = 0

        for student in students:
            if(student.gender == 'M'):
                maleSum += int(student.raisedHands)
            else:
                femaleSum += int(student.raisedHands)
        
        ChartDrawing.DrawPieChart([maleSum, femaleSum], ['Male', 'Female'], 'Raised hands share')

    @staticmethod
    def GetSubjectShare(students):
        subjects = []
        subjectsCount = []
        subjectsNames = []
        subjectsCountSingle = []

        for student in students:   
            subjects.append(student.subject)       
            
        for subject in subjects:
            count = subjects.count(subject)
            subjectsCount.append((subject, count))
                
        listSet = set(subjectsCount)
        uniqueList = (list(listSet))
        
        for name,count in uniqueList:
            subjectsNames.append(name)
            subjectsCountSingle.append(count)

        ChartDrawing.DrawPieChart(subjectsCountSingle, subjectsNames, 'Subject share')

    @staticmethod
    def GetComparisonBetweenHandsAndResources(students):
        raisedHands = []
        visitedResources = []

        for student in students:
            raisedHands.append(int(student.raisedHands))
            visitedResources.append(int(student.visitedResources))
        
        ChartDrawing.DrawBoxPlot(raisedHands, visitedResources, 'Comparison between No. raised hands and visited resources')


class ChartDrawing():
    @staticmethod
    def DrawPieChart(items, labels, title):
        y = np.array(items)
        labels = labels

        fig, ax = plt.subplots()

        ax.pie(y, labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')
        fig.canvas.set_window_title(title)

        plt.show() 

    @staticmethod
    def DrawBoxPlot(value1, value2, title):
        data = [value1, value2]

        fig, ax = plt.subplots()

        ax.set_title('Comparison between No. raised hands and visited resources')
        ax.boxplot(data)
        fig.canvas.set_window_title(title)

        plt.show()

class GUI():
    @staticmethod
    def SetGUI(students):
        window = tk.Tk()
        window.title('Education info')
        
        entNumberRaisedHands = tk.Entry(master=window, width=15)
        entNumberRaisedHands.grid(row=1, column=0, pady=10)

        lblNumber = tk.Label(master=window, text='Number of raised hands:')
        lblNumber.grid(row=0, column=0, padx=20)       

        btnGetNumberOfHands = tk.Button(
            master = window,
            text = '➔',
            width = 5,
            command = lambda: Calculations.GetRaisedHandsForAboveSetNumber(entNumberRaisedHands.get(), students)
        )
        btnGetNumberOfHands.grid(row=1, column=1)

        lblGetStudentInfo = tk.Label(master=window, text='Get all students info')
        lblGetStudentInfo.grid(row=2, column=0, padx=20, pady=10)

        btnGetStudentInfo = tk.Button(
            master = window,
            text = '➔',
            width = 5,
            command = lambda: Calculations.GetStudentsInfo(students)
        )
        btnGetStudentInfo.grid(row=2, column=1)      

        lblGetShareRaisedHandsByGender = tk.Label(master=window, text='Get share for raised hands by gender')
        lblGetShareRaisedHandsByGender.grid(row=3, column=0, padx=20, pady=10)

        btnGetShareRaisedHandsByGender = tk.Button(
            master = window,
            text = '➔',
            width = 5,
            command = lambda: Calculations.GetMaleFemaleShareForRaisedHands(students)
        )
        btnGetShareRaisedHandsByGender.grid(row=3, column=1)

        lblGetShareOfSubjects = tk.Label(master=window, text='Get share of subjects')
        lblGetShareOfSubjects.grid(row=4, column=0, padx=20, pady=10)

        btnGetShareOfSubjects = tk.Button(
            master = window,
            text = '➔',
            width = 5,
            command = lambda: Calculations.GetSubjectShare(students)
        )
        btnGetShareOfSubjects.grid(row=4, column=1, padx=20, pady=10)

        lblGetComparisonBetweenHandsAndResources = tk.Label(master=window, text='Comparison between raised hand and visited resources')
        lblGetComparisonBetweenHandsAndResources.grid(row=5, column=0, padx=20, pady=10)

        btnlblGetComparisonBetweenHandsAndResources = tk.Button(
            master = window,
            text = '➔',
            width = 5,
            command = lambda: Calculations.GetComparisonBetweenHandsAndResources(students)
        )
        btnlblGetComparisonBetweenHandsAndResources.grid(row=5, column=1, padx=20, pady=10)

        return window
    
class NewWindow(tk.Toplevel):
      
    def __init__(self, master = None, text = '', values = []):
        super().__init__(master = master)
        self.title('Calculation info')
        self.geometry('300x100')
        self.values = values
        label = tk.Label(self, text = text)
        label.grid(row=0, column=0, padx=15)
        if(len(values) != 0):
            self.SetTreeTable(values)
           
    def SetTreeTable(self, values):       
        self.geometry('1000x300')
        self.tree = ttk.Treeview(self)
        self.tree['columns']=('Gender',"Nationality",'Place of Birth', 'Subject', 'No. Raised hands', 'No. Visited resources', 'No. Viewed Announcements')
        self.tree.column('#0', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('Gender', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('Nationality', width=80, minwidth=50)
        self.tree.column('Place of Birth', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('Subject', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('No. Raised hands', width=150, minwidth=200, stretch=tk.NO)
        self.tree.column('No. Visited resources', width=150, minwidth=200, stretch=tk.NO)
        self.tree.column('No. Viewed Announcements', width=160, minwidth=200, stretch=tk.NO)

        self.tree.heading('#0',text="Name",anchor=tk.W)
        self.tree.heading('Gender', text='Gender',anchor=tk.W)
        self.tree.heading('Nationality', text='Nationality',anchor=tk.W)
        self.tree.heading('Place of Birth', text='Place of birth',anchor=tk.W)
        self.tree.heading('Subject', text='Subject',anchor=tk.W)
        self.tree.heading('No. Raised hands', text='No. Raised hands',anchor=tk.W)
        self.tree.heading('No. Visited resources', text='No. Visited resources',anchor=tk.W)
        self.tree.heading('No. Viewed Announcements', text='No. Viewed Announcements',anchor=tk.W)

        for val in values:
            self.tree.insert(parent='', index='end', text="Student", values=val)

        self.tree.grid(row=4, columnspan=4, sticky='nsew', padx=75)

def main():
    students = DataConverter.ConvertJsonToObject('eduData.json')

    gui = GUI().SetGUI(students)
    gui.geometry('450x250')
    gui.mainloop()

main()
