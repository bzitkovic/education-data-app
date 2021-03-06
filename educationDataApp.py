import json
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

class Student:
    def __init__(self, gender, nationality, placeOfBirth, subject, raisedHands, visitedResources, viewedAnnouncements, gradeClass):
        self.gender = gender
        self.nationality = nationality
        self.placeOfBirth = placeOfBirth
        self.subject = subject
        self.raisedHands = raisedHands
        self.visitedResources = visitedResources
        self.viewedAnnouncements = viewedAnnouncements
        self.gradeClass = gradeClass
    
    def GetStudentInfo(self):
        return f'\nGender: {self.gender} \
            \nNationality: {self.nationality} \
            \nPlace of birth: {self.placeOfBirth} \
            \nRaised hands: {self.raisedHands} \
            \nVisited resources: {self.visitedResources} \
            \nViewed announcements: {self.viewedAnnouncements} \
            \nGrade class: {self.gradeClass}'
    
class DataConverter():
    @staticmethod   
    def ConvertToStudentObject(fileName):
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
                gradeClass = value['Class']

                student = Student(gender, nationality, placeOfBirth, subject, raisedHands, visitedResources, viewedAnnouncements, gradeClass)
                students.append(student)
        
        return students

class StudentCalculations():
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
        if(number != ''):
            numberOfPeople = 0
            numberOfPeopleAbove = 0

            for student in students:
                if(int(student.raisedHands) >= int(number)):
                    numberOfPeopleAbove += 1

                numberOfPeople += 1

            text = f'\nOut of {numberOfPeople} people\n{numberOfPeopleAbove} of them raised hand more than {number} times.'
            NewWindow(text=text)
        else:
            tk.messagebox.showinfo(title='Message', message='Please enter a valid number!')

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
            student.viewedAnnouncements,
            student.gradeClass))
        
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
        
        ChartDrawing.DrawBoxPlot([raisedHands, visitedResources], 'Comparison between No. raised hands and visited resources')

    @staticmethod
    def GetShareOfStudenGradeClass(students):
        lowClass = 0
        middleClass = 0
        highClass = 0

        for student in students:
            if(student.gradeClass == 'L'):
                lowClass += 1
            elif(student.gradeClass == 'M'):
                middleClass += 1
            else:
                highClass += 1
        
        ChartDrawing.DrawBarChart([lowClass, middleClass, highClass], ('low', 'medium', 'high'), 'Share of students by class grade')

class ChartDrawing():
    @staticmethod
    def DrawPieChart(items, labels, title):
        y = np.array(items)

        fig, ax = plt.subplots()

        ax.pie(y, labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')
        fig.canvas.set_window_title(title)

        plt.show() 

    @staticmethod
    def DrawBoxPlot(data, title):       
        fig, ax = plt.subplots()

        ax.set_title(title)
        ax.boxplot(data)
        fig.canvas.set_window_title(title)

        plt.show()

    @staticmethod
    def DrawBarChart(data, labels, title):
        fig, ax = plt.subplots()    

        x_pos = np.arange(len(labels))
        y_pos = np.arange(len(labels))

        ax.bar(x_pos, data, align='center', alpha=0.7, color='green')
        ax.set_xticks(y_pos)
        ax.set_xticklabels(labels)
        ax.set_ylabel('Number of students')
        fig.canvas.set_window_title(title)

        plt.show()

class GUI():
    @staticmethod
    def SetGUI(students):
        window = tk.Tk()
        window.title('Education info')
        
        entNumberRaisedHands = tk.Entry(master=window, width=15)
        entNumberRaisedHands.grid(row=1, column=0, padx=25, pady=10, sticky='W')

        lblNumber = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Number of raised hands:')
        lblNumber.grid(row=0, column=0, padx=20, sticky='W')       

        btnGetNumberOfHands = tk.Button(
            master = window,
            text = '???',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: StudentCalculations.GetRaisedHandsForAboveSetNumber(entNumberRaisedHands.get(), students)
        )
        btnGetNumberOfHands.grid(row=1, column=1)

        lblGetStudentInfo = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get all students info')
        lblGetStudentInfo.grid(row=2, column=0, padx=20, pady=10, sticky='W')

        btnGetStudentInfo = tk.Button(
            master = window,
            text = '???',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: StudentCalculations.GetStudentsInfo(students)
        )
        btnGetStudentInfo.grid(row=2, column=1)      

        lblGetShareRaisedHandsByGender = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get share for raised hands by gender')
        lblGetShareRaisedHandsByGender.grid(row=3, column=0, padx=20, pady=10, sticky='W')

        btnGetShareRaisedHandsByGender = tk.Button(
            master = window,
            text = '???',            
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: StudentCalculations.GetMaleFemaleShareForRaisedHands(students)
        )
        btnGetShareRaisedHandsByGender.grid(row=3, column=1)

        lblGetShareOfSubjects = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Get share of subjects')
        lblGetShareOfSubjects.grid(row=4, column=0, padx=20, pady=10, sticky='W')

        btnGetShareOfSubjects = tk.Button(
            master = window,
            text = '???',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: StudentCalculations.GetSubjectShare(students)
        )
        btnGetShareOfSubjects.grid(row=4, column=1, padx=20, pady=10)

        lblGetComparisonBetweenHandsAndResources = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Comparison between raised hand and visited resources')
        lblGetComparisonBetweenHandsAndResources.grid(row=5, column=0, padx=20, pady=10, sticky='W')

        btnlblGetComparisonBetweenHandsAndResources = tk.Button(
            master = window,
            text = '???',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: StudentCalculations.GetComparisonBetweenHandsAndResources(students)
        )
        btnlblGetComparisonBetweenHandsAndResources.grid(row=5, column=1, padx=20, pady=10)

        lblGetShareOfStudenGradeClass = tk.Label(master=window, font=("Ariel", 12), bg='#7878ab', text='Share of students by class grade')
        lblGetShareOfStudenGradeClass.grid(row=6, column=0, padx=20, pady=10, sticky='W')

        btnGetShareOfStudenGradeClass = tk.Button(
            master = window,
            text = '???',
            width = 6,
            bd = 3,
            bg = '#78ab7c',
            command = lambda: StudentCalculations.GetShareOfStudenGradeClass(students)
        )
        btnGetShareOfStudenGradeClass.grid(row=6, column=1, padx=20, pady=10)

        return window
    
class NewWindow(tk.Toplevel):
    def __init__(self, master = None, text = '', values = []):
        super().__init__(master = master)
        self.title('Calculation info')
        self.geometry('380x80')
        self.configure(bg='#7878ab')
        self.values = values

        label = tk.Label(self, font=("Ariel", 12), bg='#7878ab', text = text)
        label.grid(row=0, column=0, padx=30, sticky='w')

        if(len(values) != 0):
            self.SetTreeTable(values)
           
    def SetTreeTable(self, values):       
        self.geometry('1100x300')
        self.tree = ttk.Treeview(self)
        self.tree['columns']=('Gender',"Nationality",'Place of Birth', 'Subject', 'No. Raised hands', 'No. Visited resources', 'No. Viewed Announcements', 'Class')
        self.tree.column('#0', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('Gender', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('Nationality', width=80, minwidth=50)
        self.tree.column('Place of Birth', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('Subject', width=80, minwidth=50, stretch=tk.NO)
        self.tree.column('No. Raised hands', width=150, minwidth=200, stretch=tk.NO)
        self.tree.column('No. Visited resources', width=150, minwidth=200, stretch=tk.NO)
        self.tree.column('No. Viewed Announcements', width=160, minwidth=200, stretch=tk.NO)
        self.tree.column('Class', width=80, minwidth=50, stretch=tk.NO)

        self.tree.heading('#0', text="Name", anchor=tk.W)
        self.tree.heading('Gender', text='Gender', anchor=tk.W)
        self.tree.heading('Nationality', text='Nationality', anchor=tk.W)
        self.tree.heading('Place of Birth', text='Place of birth', anchor=tk.W)
        self.tree.heading('Subject', text='Subject', anchor=tk.W)
        self.tree.heading('No. Raised hands', text='No. Raised hands', anchor=tk.W)
        self.tree.heading('No. Visited resources', text='No. Visited resources', anchor=tk.W)
        self.tree.heading('No. Viewed Announcements', text='No. Viewed Announcements', anchor=tk.W)
        self.tree.heading('Class', text='Class', anchor=tk.W)

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.place(x=1000, y=50, height=200)
        self.tree.configure(yscrollcommand=vsb.set)

        for val in values:
            self.tree.insert(parent='', index='end', text="Student", values=val)

        self.tree.grid(row=4, columnspan=4, sticky='nsew', padx=75)

def main():
    students = DataConverter.ConvertToStudentObject('eduData.json')

    gui = GUI().SetGUI(students)

    gui.geometry('550x300')
    gui.configure(bg='#7878ab')

    gui.mainloop()

main()
