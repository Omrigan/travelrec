from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . import models
from . import serializers
import random, requests, time
from geopy.distance import vincenty

from stop_words import get_stop_words
from nltk.stem.snowball import RussianStemmer
from nltk.tokenize import RegexpTokenizer
import gensim, re

from django.forms.models import model_to_dict
def json_equivalent(    obj):
    dictionary = {}
    for field in obj._meta.get_all_field_names():
        dictionary[field] = obj.__getattribute__(field)
    return dictionary

def parseData(req):
    models.TNotes.objects.all().delete()
    texts = []
    step = 20
    for i in range(0,30):
        print(i)
        r = requests.get("https://api.vk.com/method/wall.get?domain=the.puzzle.ofworld&count=" + str(step )+ "&offset=" + str(i*step))
        a = random.random()
        b = random.random()*180
        a=random.random()*180
        if random.random()>0.8:
            user_id=68
        else:
            user_id = models.TUsers.objects.order_by('?').first().id

        for p in r.json()['response']:
            # print(i)
            if type(p) == dict and 'text' in p:
                txt = p['text']
                if len(txt)>100 and "<br>" in txt:
                    next = models.TNotes()
                    next.vk = 0
                    next.fb = 0
                    next.tw = 0
                    next.access = 0
                    a+=random.random()-0.3
                    b+=random.random()/2-0.6
                    next.longitude = a
                    next.latitude = b
                    next.title = txt[:txt.index("<br>")]
                    next.text = txt
                    next.user_id = user_id
                    next.save()

def getRandomUser(req):
    return JsonResponse(model_to_dict(models.TUsers.objects.order_by('?').first()))

def dist(first, sec):
    return vincenty((sec['latitude'], sec['longitude']), (first['latitude'], first['longitude'])).km


def getTopByCurLocation(req, pk):
    me = model_to_dict(models.TUsers.objects.get(pk=pk));
    return JsonResponse({'vals' : sorted(models.TUsers.objects.all().values(),key=lambda x: dist(me, x))[0:4]})


def processNotes():
    texts = []
    for note in models.TNotes.objects.all():
        texts.append(textToWordList(note.text))
    
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=6, id2word = dictionary, passes=20)
    ldamodel.save("supermodel.txt")

def textToWordList(txt):
    p_stemmer = RussianStemmer()
    tokenizer = RegexpTokenizer(r'\w+')
    stop_w = [p_stemmer.stem(i) for i in get_stop_words('ru')]
    r = re.compile('^[а-я]+$')
    badword =[
        'дом',
        'город',
        "дорог",
        "час",
        "ноч",
        "слов",
        "утр",
        "стран",
        "пут",
        "путешеств",
        "мест",
        'нов',
        "друз",
        "добр"
    ]
    txt = txt.lower().replace("<br>", "\n")
    tokens = [p_stemmer.stem(i) for i in tokenizer.tokenize(txt)]
    tokens = [i for i in tokens if not i in stop_w and r.match(i) and not i in badword]
    return tokens

def getTagsForText(req, pk):
    ret = {}
    txt=models.TNotes.objects.get(pk=pk).text
    ret['txt'] = txt
    tokens = textToWordList(txt)
    dictionary = gensim.corpora.Dictionary([tokens, ])
    from travelrec import settings
    if not settings.MYMODEL:
        processNotes()
        settings.MYMODEL = gensim.models.ldamodel.LdaModel.load("supermodel.txt")
    mymodel = settings.MYMODEL
    ret['topics'] = []
    for topic in mymodel.print_topics(num_words=7):
        ret['topics'].append(topic)
    ret['analysis'] = sorted(mymodel[dictionary.doc2bow(tokens)], key=lambda x: -x[1])
    return JsonResponse(ret)
