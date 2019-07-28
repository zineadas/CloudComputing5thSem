def getYear(sem):
    if sem=='3':
        return '2'
    elif sem=='5':
        return '3'
    elif sem=='7':
        return '4'

def main():
   names=[['Achal Dixit','CS12018','3'],
          ['Manul Singh Parihar','CS12018','3'],
          ['Aditya Jolly','EC12017','5'],
          ['Ailneni Sai Shishir','CS12017','5'],
          ['Eka Shree Harsha','CS12016','7'],
          ['Kaustav Goswami','CS12016','7'],
          ['Mudam Rahul','EC12016','7'],
          ['Aman Sheel','CS12017','5'],
          ['Chekurthi Manvith','EC12017','5'],
          ['Harsh Vishwakarma','CS12017','5'],
          ['Priyam Bardalai','CS12018','3'],
          ['Amal Thomas K','EC12018','3'],
          ['Varun Parashar','EC12017','5'],
          ['Aayush Nirwan','CS12016','7'],
          ['Bibek Goswami','EC12016','7'],
          ['Deepak Kumar','CS12016','7'],
          ['Rajat Bhattacharjya','EC12017','5'],
          ['Rishu Raj','EC12018','3'],
          ['Siddhant Jha','EC12018','3']
          ]

   courses=[['Algorithms','CS201'],
         ['Data Communications','CS221'],
         ['IT Workshop I','CS201'],
         ['Analog Circuits','EC201'],
         ['Semiconductor Devices','EC260'],
         ['Signals and Systems','EC241'],
         ['Measurement and Instrumentation','EC281'],
         ['Theory of Computation','CS301'],
         ['Computer Networks','CS352'],
         ['Machine Learning','CS306'],
         ['IT Workshop II','CS351'],
         ['Digital Communication','EC351'],
         ['Analog Integrated Circuits','EC301'],
         ['Electromagnetics','EC370'],
         ['Control Systems','EC380'],
         ['Data Analytics','CS401'],
         ['Evolutionary Computation','CS473'],
         ['Advanced Computer Architecture','CS474'],
         ['Introduction to Graph Theory','CS471'],
         ['Semantic Web Technologies','CS472'],
         ['Communication Network','EC456'],
         ['Measurements and Instrumentation','EC481'],
         ['SoC with IoT Applications','EC482'],
         ['Cognitive Radio','EC457'],
         ['MIMO Communications','EC459']
         ]

   name=input("Enter name: ")
   batch=input("Enter batch: ")
   sem=input("Enter semester: ")
   l=[name,batch,sem]

   flag=False
   for x in names:
       if x==l:
           flag=True
           break
   if flag==False:
       print("Student not registered.")
       return 0

   print("Choose from the following courses. Enter 3 or 4 course codes each in a new line: ")
   for x in courses:
       a=x[1]
       if (a[:2]==batch[:2]) and (a[2]==getYear(sem)):
           print(x)
   y=input()
   num=0
   while y!='done' and num<5 :
       num+=1
       for x in courses:
           if x[1]==y:
                l.append(x)
       y=input()
   f=open("student_course_information.txt","a")
   f.write(str(l)+"\n")
   f.close()


if __name__=='__main__':
    main()