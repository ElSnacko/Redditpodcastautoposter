# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:53:47 2019

@author: jbrow
"""

from selenium import webdriver
import pandas as pd
import numpy
import timeit
import REDDIT_CRED

class autoposterreddit:

    urldict= {'redditlogurl':'https://www.reddit.com/login/'
          ,'redditurlpodcasts':'https://www.reddit.com/r/podcasts/'
          ,'urlanchor':'https://anchor.fm/NAME'}

    inject = ['DATBODY','DATTYPE','DATSFW','DATNAME']
    platforms = ['Anchor','Apple Podcast','Spotify','Podbean','Castbox','Radio Public','Stitcher','Google Play Music']

    dirdict = {'writeupdir':r'redditpost_template.txt'
           ,'chromedir':r'chromedriver_win32\chromedriver.exe'
           ,'podcastlinkdir':r'Podcast_Links.txt'}

    username = REDDIT_CRED.USERNAME
    password = REDDIT_CRED.PASSWORD


    selendict= {'logindiv':'loginUsername','passdiv':'loginPassword'
            ,'signinbtnclass':'AnimatedForm__submitButton','uploadid':'start-upload-button-single'
            ,'credclass':'_19oWd7e3z7-ztUGzdIoCR7','topstickyclass':'SQnoC3ObvgnGjWt90zD9Z'
            ,'postboxclass':'//*[@id="app"]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div'
            ,'epidpclass':'styles__episodeDescription___C3oZg ','epititleclass':'styles__title___1Av3V'
            }
    option = webdriver.ChromeOptions()
    option.add_argument("--incognito")
    
    def redditpodcastposter(self):
        
        browser = webdriver.Chrome(self.dirdict['chromedir'], chrome_options=self.option)
        browser.get(self.urldict['redditlogurl'])

        try:
            loginuser = browser.find_element_by_id(self.selendict['logindiv'])
            loginuser.clear()
            loginuser.send_keys(self.username)
            loginpass = browser.find_element_by_id(self.selendict['passdiv'])
            loginpass.clear()
            loginpass.send_keys(self.password)
            upload = browser.find_element_by_class_name(self.selendict['signinbtnclass'])
            upload.click()
        except:print('damn')

        days = datetime.now()

        browser.get(self.urldict['redditurlpodcasts'])
        browser.find_element_by_class_name(self.selendict['credclass']).click()
        stickypost = browser.find_element_by_class_name(self.selendict['topstickyclass'])
        weeklyurl = stickypost.get_attribute('href')
        print(weeklyurl)
        if 'Weekly podcast post' in stickypost.text:
            if int(stickypost.text[len(stickypost.text)-3:len(stickypost.text)-1]) - int(days.strftime("%d")) < 7:
                stickypost.click()
            else:print('This weekly post is old, wait till next week.')   
        else:print('Please find proper post and resume.')
       
    
#try:
    #poster1 = browser.find_element_by_class_name(postboxclass)
    #poster.click().clear()
    #poster.click().send_keys('ayyyoo1')
#except :print('damn1')
#poster3 = browser.find_element(By.CLASS_NAME,postboxclass3)

    def writeuppull(self):
         browser = webdriver.Chrome(self.dirdict['chromedir'], chrome_options=self.option)
         browser.get(self.urldict['urlanchor'])
        
             
         post = browser.find_element_by_class_name(self.selendict['epititleclass'])
   
             
         title = post.get_attribute('div')
         self.inject.remove(3)
         self.inject.insert(3,title)
         
         ebody = browser.find_element_by_class_name(self.selendict['epibodyclass']) 
         body = ebody.get_attribute('div')
         self.inject.remove(0)
         self.inject.insert(0,body)
         
         #FW = input('Is the SFW?')
         #if FW<> 'y':#FW='NSFW'
        #else:FW = 'SFW'
         #self.inject.remove(2)
         #self.inject.insert(2,FW)
         
         #Type = input('Whats the type?')
         #self.inject.remove(1)
         #self.inject.insert(1,Type.capitalize())
         return self.inject
         
         
    def hypertxtlinker(self):
        hyperlinked = []
        htdf = pd.read_csv(self.dirdict['podcastlinkdir'],header=None)
        htdf.columns=['links']
        htdf= htdf['links'].values.tolist()
        #print(htdf)
        #postmake = postmaker(self.directdir['writeupdir'],self.inject)
        for x in enumerate(htdf):
           hyperlinked= '<a href="{}">{}</a>',str(htdf[x]),str(self.platforms[x])
        #print(hyperlinked)


    def postmaker(writeupdir,inject):
        writeuptemp = open(writeupdir)
        writeup =writeuptemp.read()
        editer = ['##BODY##','##TYPE##','##SFW##','##NAME##']
        counter = 0
        for x in editer:
            writeup = writeup[0:writeup.find(x)] + inject[counter] + writeup[writeup.find(x)+len(x):]
            counter+=1 
        return writeup
    
    def upvoter(self,upclass):
        self.browser.find_element_by_class_name(upclass).click() 
        
trythis = autoposterreddit()
print(trythis.redditpodcastposter())    
#trythis.hypertxtlinker()