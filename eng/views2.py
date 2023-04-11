from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import os


def gen2():


    #############################################    Selecting words from file     ###########################################################
    
    
    #-----------------------------------------------Male Female name-------------------------------------------------------------#

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'mnames.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8') 
    mname = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'fnames.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8') 
    fname = data_file.read().split("\n")


    #-----------------------------------------------first Sentence Object-------------------------------------------------------------#

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'peenewale.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8')
    drinkable = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dekhna.txt')  #full path to text.
    data_file = open(file_path , 'r',encoding='utf-8')
    watchable = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'khaanewale.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    cookable = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'khelnewale.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    playable= data_file.read().split("\n")


    #----------------------------------------------Dependent Object second sentance--------------------------------------------------------------#

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dep_play_obj.txt')  #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    dep_obj_play = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dep_cook_obj.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    dep_obj_cook = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dep_drink_obj.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    dep_obj_drink = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dep_watch_obj.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    dep_obj_watch = data_file.read().split("\n")



    #---------------------------------------------Male verb forms---------------------------------------------------------------#


    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'cv.txt')  #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_c = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'playverbs.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_p = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'drink_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_d = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dekh_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    verbs_see = data_file.read().split("\n")


    #-------------------------------------------female verb forms-----------------------------------------------------------------#


    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_cv.txt')  #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_c = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_playverbs.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_p = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_drink_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_d = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'f_dekh_kriya.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    f_verbs_see = data_file.read().split("\n")

    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'dc.txt')   #full path to text.
    data_file= open(file_path , 'r',encoding='utf-8')
    dc = data_file.read().split("\n")



    #------------------------------------------------------------------------------------------------------------#



    def dep_c():
        return dc[random.randint(0,len(dc)-1)]

    def mnames():
        return mname[random.randint(0,len(mname)-1)]
    def fnames():
        return fname[random.randint(0,len(fname)-1)]
    

    ###################    Selecting Subject  First   ############################
    
    ran = random.randint(1,2)
    
    if(ran == 1):
            n1 = mnames()
    else:
            n1 = fnames()



    ###################    Selecting Object Second    ############################

    def objects():
        rt=random.randint(1,4)
        if(rt==1): 
            term = cookable[random.randint(0,len(cookable)-1)] 
        elif(rt==2):
            term = playable[random.randint(0,len(playable)-1)]
        elif(rt==3):
            term = drinkable[random.randint(0,len(drinkable)-1)]   
        elif(rt==4):
            term = watchable[random.randint(0,len(watchable)-1)]  
            
        return term
    
    ###################    Selecting Dependent Object    ############################
    

    def dep_obj_cookable():
        return dep_obj_cook[random.randint(0,len(dep_obj_cook)-1)]

    def dep_obj_playable():
        return dep_obj_play[random.randint(0,len(dep_obj_play)-1)]
    
    def dep_obj_drinkable():
        return dep_obj_drink[random.randint(0,len(dep_obj_drink)-1)]
    
    def dep_obj_watchable():
        return dep_obj_watch[random.randint(0,len(dep_obj_watch)-1)]
    


    ###################  Then  Selecting Verbs     ############################
    
    def m_play_verbs():
        return verbs_p[random.randint(0,len(verbs_p)-1)]
    
    def m_cook_verbs():
        return verbs_c[random.randint(0,len(verbs_c)-1)]
    
    def m_drink_verbs():
        return verbs_d[random.randint(0,len(verbs_d)-1)]
    
    def m_watch_verbs():
        return verbs_see[random.randint(0,len(verbs_see)-1)]
    
    #-------------------------------------------------------------------#
    

    def f_play_verbs():
        return f_verbs_p[random.randint(0,len(f_verbs_p)-1)]
    
    def f_cook_verbs():
        return f_verbs_c[random.randint(0,len(f_verbs_c)-1)]
    
    def f_drink_verbs():
        return f_verbs_d[random.randint(0,len(f_verbs_d)-1)]
    
    def f_watch_verbs():
        return f_verbs_see[random.randint(0,len(f_verbs_see)-1)]
    

    
    ###################  sentence conjunction  ############################


    
    def conjunction():

        rt = random.randint(1,3)

        if(rt == 1):
            # conj ='लेकिन'
            conj ='क्यो की'
        elif(rt == 2):
            conj ='क्यो की'
        elif(rt == 3):
            # conj ='की'
            conj ='क्यो की'

        return conj
    



    ############################################################################



    def make_sentence():

        global obj1
        obj1 = objects() # selecting object

        if n1 in mname:
            # selecting male Verbs
            c_v1 = m_cook_verbs()
            p_v1 = m_play_verbs()
            d_v1 = m_drink_verbs()
            w_v1 = m_watch_verbs()
            
        elif n1 in fname:
            # selecting female Verbs
            c_v1 = f_cook_verbs()
            p_v1 = f_play_verbs()
            d_v1 = f_drink_verbs()
            w_v1 = f_watch_verbs()

        conj = conjunction() # selecting conjuction
        dc = dep_c()


        if obj1 in cookable:
            sen1 = n1 + " " + obj1 + " " + c_v1
            dep_obj = dep_obj_cookable()
            ans  = conj + " " + " " + "वह" + " " + dep_obj + " है  |"
            full_sen = n1 + " " + obj1 + " " + c_v1 + " " + ans
            
        elif obj1 in playable:
            sen1 = n1 + " " + obj1 + " " + p_v1
            dep_obj = dep_obj_playable()
            ans = conj + " " + " " + "वह" + " " + " " + dep_obj + " है |"
            full_sen = n1 + " " + obj1 + " " + p_v1  + " " + ans

        elif obj1 in drinkable:
            sen1 = n1 + " " + obj1 + " " + d_v1
            dep_obj = dep_obj_drinkable()
            ans  = conj + " " + "वह" + " " + dep_obj + " है |"
            full_sen = n1 + " " + obj1 + " " + d_v1 + " " + ans

        elif obj1 in watchable:
            sen1 = n1 + " " + obj1 + " " + w_v1
            dep_obj = dep_obj_watchable()
            ans  = conj + " " + "वह" + " " + dep_obj + " होता है  |"
            full_sen = n1 + " " + obj1 + " " + w_v1 + " " + ans
        

        return [full_sen,ans,conj,sen1,ans]
    # [sentense , answer , conjunction  , independent claus , dependent claus ]
    

    ############################################################################



    # Sentence Making start's here
    data = make_sentence()


    return (data)

def theory2(request):
    return render(request,'theory2.html')

def next2(request):
    dataa2 = request.session.get('dataa2')
    dataa2 = gen2()
    request.session['dataa2'] = dataa2
    daaa2=dataa2
    return render(request,'next2.html',{'data':daaa2[0],'ans':daaa2[1],'con':daaa2[2],'nta':daaa2[3],'r':daaa2[4]})
    

def explanation2(request):
    dataa2 = request.session.get('dataa2')
    daaa2=dataa2
    return render(request,'explanation2.html',{'data':daaa2[0],'ans':daaa2[1],'con':daaa2[2],'nta':daaa2[3],'r':daaa2[4]})
    
def ex2(request):
    dataa2 = request.session.get('dataa2')
    daaa2=dataa2
    return render(request,'ex2.html',{'data':daaa2[0],'ans':daaa2[1],'con':daaa2[2],'nta':daaa2[3],'r':daaa2[4]})