

from theLearnings.models import Skill, SkillOf



def scrollbar( dictionary ):
          skills = Skill.objects.filter( status=True ) 



def getScrollbarDetails(request):
        count = 0
        objects = Skills.objects.all()
        sets,lists = set(),list() #
        returningdataset = dict()
        for object in objects:
                if object.skillsof.id in showonly:
                        count +=1
                        if object not in sets:
                                sets.add(object)
                                lists.append(object)
                                returningdataset[object.skills.name] = {
                                        'name' : object.skills.name,
                                        'path' : '/articals/'+object.slug+'/'
                                }
        return returningdataset 



























