class Project(object):
    def __init__(self,n,s,e,d,sc,sk={}) -> None:
        self.name = n
        self.start = s
        self.end = e
        self.duration = d
        self.score = sc
        self.skills = sk
    def __str__(self):
        return 'Project Name: {}, Skillsets: {}, Ideal Start Time: {},Finish before: {}, Duration: {}, Score: {}'.format(self.name,self.skills,self.start,self.end,self.duration,self.score)
    def __repr__(self) -> str:
        return self.name
    
class Contributor(object):
    def __init__(self,n,sk = {}) -> None:
        self.name = n
        self.skills = sk
    def improveSkill(self,n):
        self.skills[n] +=1
    def __str__(self) -> str:
        return 'Contributor Name: {}, Skills: {}'.format(self.name,self.skills)
    def __repr__(self) -> str:
        return self.name

class ProjectGroup(object):
    def __init__(self,pName,st,du,sc,cList=[]) -> None:
        self.projName = pName
        self.start = st
        self.duration = du
        self.score = sc
        self.contributorList = cList
    def __str__(self):
        return 'Project Name: {}, Contributors: {}, Ideal Start Time: {}, Duration: {}, Score: {}'.format(self.projName,self.contributorList,self.start,self.duration,self.score)
    def __repr__(self) -> str:
        return '({} {} {} {} {})'.format(self.projName,self.start,self.duration,self.contributorList,self.score)

class Course(object):
    def __init__(self,n,l) -> None:
        self.name = n
        self.level = l
    def __str__(self) -> str:
        return 'Contributor Name: {}, Level: {}'.format(self.name,self.level)
    def __hash__(self):
        return hash((self.name, self.level))

    def __eq__(self, other):
        return (self.name, self.level) == (other.name, other.level)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)