from UtilClasses import *
def organizeInput(path):
    with open(path,'r') as f:
        lines = f.readlines()
        num_contribs, num_projs = [int(i) for i in lines[0].split()]
        flag = 0
        i = 1
        contributors, projects, courses = [], [], {}
        while i < len(lines):
            line = lines[i].split()
            if len(line) > 2:
                flag = 1
            if flag == 0:
                name = line[0]
                c = Contributor(name,{})
                num_skills = int(line[1])
                i += 1
                for j in range(i, num_skills+i):
                    skill = lines[j].split()
                    cName, cLevel = skill[0], int(skill[1])
                    c.skills[cName] = cLevel
                    if (cName, cLevel) in courses:
                        courses[(cName, cLevel)].append(c)
                    else:
                        courses[(cName, cLevel)] = [c]
                i += num_skills
                contributors.append(c)
            else:
                pr = lines[i].split()
                proj_name = pr[0]
                proj = Project(proj_name,(int(pr[3]) - int(pr[1])), int(pr[3]),int(pr[1]), int(pr[2]),{})#(n,d,sc,e,num_skill) (n,s,e,d,sc,sk)
                num_proj_skills = int(pr[4])
                i += 1
                for j in range(i,num_proj_skills+i):
                    sk = lines[j].split()
                    proj.skills[sk[0]] = int(sk[1])
                i += num_proj_skills
                projects.append(proj)
    return contributors, projects, courses
    
