from fileReader import *

def getProjectGroup(courses,projects):
    projectGroups = []
    for p in projects:
        pg = ProjectGroup(p.name,p.start,p.duration,p.score,[])
        for x,y in courses.items():
            for n,l in p.skills.items():
                if n == x[0] and l <= (x[1] + 1):
                    pg.contributorList.extend(y)
        projectGroups.append(pg)
    return projectGroups

if __name__ == '__main__':
    PATH = "D:\\Projects\\Python Scripts\\GoogleHashCode2022\\HashCode2022\\MentorSchedular\\InputData\\a_an_example.in.txt"          
    contributors, projects, courses = organizeInput(PATH)
    for p in projects:
        print(p)
    print()
    for c in contributors:
        print(c)
    print()
    print(courses)
    print()
    print(getProjectGroup(courses,projects))
    
    
'''
Sample Output
Project Name: Logging, Skillsets: {'C++': 3}, Ideal Start Time: 0,Finish before: 5, Duration: 5, Score: 10
Project Name: WebServer, Skillsets: {'HTML': 3, 'C++': 2}, Ideal Start Time: 0,Finish before: 7, Duration: 7, Score: 10
Project Name: WebChat, Skillsets: {'Python': 3, 'HTML': 3}, Ideal Start Time: 10,Finish before: 20, Duration: 10, Score: 20

Contributor Name: Anna, Skills: {'C++': 2}
Contributor Name: Bob, Skills: {'HTML': 5, 'CSS': 5}
Contributor Name: Maria, Skills: {'Python': 3}

{('C++', 2): [Anna], ('HTML', 5): [Bob], ('CSS', 5): [Bob], ('Python', 3): [Maria]}

[Logging [Anna], WebServer [Anna, Bob], WebChat [Bob, Maria]]  
'''