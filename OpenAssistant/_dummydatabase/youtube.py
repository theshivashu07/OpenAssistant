








videos = [
        "https://www.youtube.com/embed/C-9dqfXENb4?si=pvQ2QU1IgOC4itQd",
        "https://www.youtube.com/embed/6_0yhsWCWpQ?si=MwWeqICLJ5a7O2Xl",
        "https://www.youtube.com/embed/mr7uP20YVRg?si=AnyIj5swgH6DnWSu",
        "https://www.youtube.com/embed/tb9-MMstDcg?si=YnLQ4LU6mHQW7PaJ",
        "https://www.youtube.com/embed/6pT_ooV_riQ?si=JPX0jirIFpXhdVs_",
        "https://www.youtube.com/embed/gkiTWVDauV0?si=lwspryXFReyMdrT4",
        "https://www.youtube.com/embed/JG7zBSWWo2E?si=G95EC4_m29nUaADN",
        "https://www.youtube.com/embed/LvdmCPe7I-o?si=XO94adV0-kyguHw_",
        "https://www.youtube.com/embed/IrgOlrVT-mo?si=rxByciyAdc8_rqNZ",
        "https://www.youtube.com/embed/-7VeQh1MnQ0?si=DBfOSGHdQjHasLv6",
        "https://www.youtube.com/embed/ZH2PQ6n-Esc?si=WGEZO_qnSoIGt_UO",
        "https://www.youtube.com/embed/83s2oeJMl94?si=hp35VC47D8DcB5Ns",
        "https://www.youtube.com/embed/NDUPymw7bjg?si=tbCsE2uVMr0YbM7w",
        "https://www.youtube.com/embed/81uTuTaDGKM?si=7gq7wqbc8XBJtaSl",
        "https://www.youtube.com/embed/lVjooGXzGSQ?si=sJCLn7KNt0xO4_Dz",
        "https://www.youtube.com/embed/11Ut-DhIHE4?si=7rLA-NGqcg_KPeIw",
        "https://www.youtube.com/embed/bGVVxFO01Ks?si=080b1WtvQlWk9ucc",
        "https://www.youtube.com/embed/S7kgE68skC8?si=kIn4qK4v55B3oStJ",
        # "https://www.youtube.com/embed/TmB_m40Iwgk?si=CEo1mYUJqtn90YOR",
        # "https",
        # "https",
        # "https",
        # "https",
        # "https",
]




class Menus:
        def __init__(self,dictionary):
                self.name = dictionary.get('name',None)
                self.path = dictionary.get('path',None)
                self.logo = dictionary.get('logo',None)
                # print( self.name, self.path, self.logo )
        def __str__(self):
                return f"<object:Menus | name:{self.name}, url:{self.url}, logo:{self.logo}.>"

l = dict()

sidebar_menus = {
        'Mains' : {
                'Home' : { 'name' : 'Home', 'path' : '/youtube/', 'logo' : 'fa-solid fa-house'},  
                'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                'Subscription' : { 'name' : 'Subscription', 'path' : '/youtube/subscription/', 'logo' : 'fa-solid fa-video'},  
        },
        'Others' : {
                'Accessories' : { 'name' : 'Accessories', 'path' : '/youtube/accessories/', 'logo' : 'fa-solid fa-cart-shopping'},  
                'Spiritual' : { 'name' : 'Spiritual', 'path' : '/youtube/spiritual/', 'logo' : 'fa-solid fa-om'},  
                'Study Learning' : { 'name' : 'Study Learning', 'path' : '/youtube/studylearning/', 'logo' : 'fa-solid fa-book'},  
                'Songs' : { 'name' : 'Songs', 'path' : '/youtube/songs/', 'logo' : 'fa-solid fa-headphones'},  
                'Workout' : { 'name' : 'Workout', 'path' : '/youtube/workout/', 'logo' : 'fa-solid fa-dumbbell'},  
                'Political' : { 'name' : 'Political', 'path' : '/youtube/political/', 'logo' : 'fa-solid fa-landmark-dome'},  
                'Standups' : { 'name' : 'Standups', 'path' : '/youtube/standups/', 'logo' : 'fa-regular fa-face-smile'},  
                'NEWS' : { 'name' : 'NEWS', 'path' : '/youtube/news/', 'logo' : 'fa-solid fa-tv'},  
                'Goods Workspace' : { 'name' : 'Goods Workspace', 'path' : '/youtube/goodsworkspace/', 'logo' : 'fa-regular fa-handshake'},  
                'Announcements' : { 'name' : 'Announcements', 'path' : '/youtube/announcements/', 'logo' : 'fa-solid fa-bullhorn'},  
                'Interview | Podcast' : { 'name' : 'Interview | Podcast', 'path' : '/youtube/intervieworpodcast/', 'logo' : 'fa-solid fa-chalkboard-user'},  
                'Interviews Guide' : { 'name' : 'Interviews Guide', 'path' : '/youtube/interviewsguide/', 'logo' : 'fa-solid fa-person-chalkboard'},  
                'Coding' : { 'name' : 'Coding', 'path' : '/youtube/coding/', 'logo' : 'fa-solid fa-laptop-code'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
                # 'Reels' : { 'name' : 'Reels', 'path' : '/youtube/reels/', 'logo' : 'fa-solid fa-mobile'},  
        },
}

def getSidebarData():
        '''actually this is fixed for youtube, but if want for another url, give app name only, like : 'problem' / 'artical' ..... '''
        Database = dict()
        for keys,values in sidebar_menus.items():
                Database[keys] = dict()
                for key,value in values.items():
                        Database[keys][key] = Menus(
                                dictionary = value
                        )
        return Database




def YoutubeRUN(limit=4,dictionary=dict()):
        dictionary['videos'] = list()
        temp = list()
        for links in videos:
                temp.append(links)
                if len(temp)==limit:
                        dictionary['videos'].append(temp)
                        temp = list()
        if temp:
                dictionary['videos'].append(temp)
                temp = list()
        # print(dictionary['videos'])
        dictionary['sidebar'] = getSidebarData()

        return None





