

from theLearnings.models import Skill, SkillOf, Topic, TopicHeadings, TopicSubHeadings
from Home.models import OptionsOf,OptionsGroup,Options

# from Home.models import *
from theArticals.models import *
from theArticals.functions.getSidebarRight import getDay,getDate,getAgo





def getSkills(request):
          skills = Skill.objects.all()
          return skills


def getTopics(request,skillObject):
        print(skillObject,type(skillObject))
        topicheadings = TopicHeadings.objects.filter(skill=skillObject) 

        resuntantDict = dict()
        for topicheading in topicheadings:
                dataList = resuntantDict.get(topicheading.name,None)
                if dataList:
                        resuntantDict[topicheading.name].append(topicheading)
                        continue
                
                topicsubheadings = TopicSubHeadings.objects.filter( headings=topicheadings ) 
        return topicheading 







