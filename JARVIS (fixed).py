"""
J.A.R.V.I.S
Objectives: Understand speech and execute the commands accordingly
Commands: Opening applications, Specific websites on Chrome, etc.
Functions needed: 1. For recognizing voice and getting the command. (recognition and decipher func are doing that)
                  2. For getting the time. (both greet_time and get_time are doing that)
                  3. For opening the application needed. (opener func is doing that but we need more applications)
                  4. For reading the time back or any catchphrase. (read_back is good to go still not sure about the other)
                  5. For creating some catchphrases. (catchphrases func needs work and need to decide upon them as well)
Random Ideas: wiki func is for wikipedia searches only but no idea how I will be precise enough
Still need to learn how to play all files in a directory or even one file in a directory as a matter of fact but another
idea would be to list all the files in a directory (both display it and speak it out) and choose from there (definitely
need a GUI for this loading time and stuff). There is an email idea too and also PDF reader and keyboard stroke reader.
Also opener func needs some more applications to open. There maybe a weather API and a news API as well even though I'm
not quite sure about that news API as that is really hard to gather with the full news.
20/11/20 - Update - Resolve was added to opener, wiki func is up and running, catchphrases func is up and running and
in need of more catchphrases.
21/11/20 - Update - Fixed the decipher function big time. The login is fixed and all comparisons work (hopefully) and the
idea for pdf reading was dropped because of encryption issues. And added music as well as Youtube privileges. Still need
to add email client, which I will add later on. But otherwise it is pretty much done I would say even though I might
make it again with a little more improvements. And also I need a GUI for this so there's that.
But for the time being I will stop here.
"""
import pyttsx3
import random
import keyboard
import subprocess
import pyaudio
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
engine = pyttsx3.init()


def decipher(speech):
    words = speech.split(" ")
    catch = True
    for i in range(len(words)):
        if words[i] == 'open':
            catch = False
            opener(words)
            break
        if words[i] == 'google' or words[i] == 'Google':
            catch = False
            search(words)
            break
        if words[i] == 'wikipedia' or words[i] == 'Wikipedia':
            catch = False
            wiki(words)
            break
        if words[i] == 'time':
            catch = False
            get_time()
            break
        if words[i] == 'music':
            catch = False
            music()
            break
        if words[i] == 'Youtube' or words[i] == 'youtube':
            catch = False
            ytube(words)
            break
    if catch:
        catch_phrases(words)


def get_time():
    t = datetime.datetime.now()
    read_back("Currently the time is " + t.strftime("%X"))


def greet():
    greet_time = datetime.datetime.now()
    needed = int(greet_time.strftime("%H"))
    if needed < 12:
        read_back("Good Morning Zander, what can I do for you today?")
    elif 12 < needed < 18:
        read_back("Good Afternoon Zander, what can I do for you today?")
    elif needed > 18:
        read_back("Good Evening Zander, what can I do for you today?")


def search(raw_query):
    try:
        raw_query.remove('search')
        raw_query.remove('on')
        raw_query.remove('Google')
    except:
        raw_query.remove('on')
        raw_query.remove('Google')
    query = " "
    for i in range(len(raw_query)):
        query = query + " " + raw_query[i]
    webbrowser.get('windows-default')
    url = f"https://www.google.com/search?q={query.strip()}"
    webbrowser.open_new(url)


def wiki(raw_query):
    try:
        raw_query.remove('search')
        raw_query.remove('on')
        raw_query.remove('Wikipedia')
    except:
        raw_query.remove('on')
        raw_query.remove('Wikipedia')
    query = " "
    for i in range(len(raw_query)):
        query = query + " " + raw_query[i]
    print(wikipedia.summary(query, sentences=2))
    read_back("According to wikipedia" + wikipedia.summary(query, sentences=2))


def catch_phrases(quotes):
    for i in range(len(quotes)):
        if quotes[i] == 'your':
            read_back("I am JARVIS, your personal assistant")
            break
        if quotes[i] == 'name':
            read_back("You are Zander")
            break


def read_back(voice):
    engine.setProperty('rate', 170)
    engine.say(voice)
    engine.runAndWait()


def hear():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=1, phrase_time_limit=3)
    phrase = r.recognize_google(audio)
    print(phrase)
    decipher(phrase)


def opener(keyword):
    for i in range(len(keyword)):
        if keyword[i] == 'vlc':
            subprocess.Popen(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
        elif keyword[i] == 'resolve':
            subprocess.Popen(r"C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe")
        else:
            read_back("Sorry, I wasn't able to find that application")


def music():
    music_dir = 'E:\Songs'
    songs = os.listdir(music_dir)
    print(songs)
    i = random.randrange(0, (len(songs) - 1))
    os.startfile(os.path.join(music_dir, songs[i]))


def ytube(raw_query):
    try:
        raw_query.remove('search')
        raw_query.remove('on')
        raw_query.remove('Youtube')
    except:
        raw_query.remove('on')
        raw_query.remove('Youtube')
    query = " "
    for i in range(len(raw_query)):
        query = query + " " + raw_query[i]
    url = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.get('windows-default')
    webbrowser.open_new(url)


if __name__ == '__main__':
    greet()
    hear()


engine.stop()
