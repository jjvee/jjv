from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

from .models import Meetings, Order, Menu, Member, Team

import datetime
import json
import copy
# Create your views here.

def index(request):
    
    teams = Team.objects.all().order_by('-id')

    try :
        request.session['teamcode'] = request.POST['teamcode']
        teamcode = request.session['teamcode']
    except :
        try:
            teamcode = request.session['teamcode']                
        except:
            request.session['teamcode'] = 'TRADE'
            teamcode = request.session['teamcode']

    if (teamcode):

        if (teamcode == 'all'):
            meetings = Meetings.objects.all().order_by('-id')
        else :
            team = Team.objects.get(teamcode = teamcode)
            meetings = Meetings.objects.filter(team = team).order_by('-id')
    else :
        meetings = Meetings.objects.all().order_by('-id')

    context = {'meetings':meetings, 'teams':teams, 'teamcode':teamcode}
    return render(request, 'snctrd/index.html', context)
    
def meetings(request, meeting_id):
    meeting = Meetings.objects.get(id = meeting_id)
    orders  = Order.objects.filter(meeting = meeting)
    context = {'meeting':meeting, 'orders':orders}
    return render(request, 'snctrd/meeting.html', context)
    
def order(request, meeting_id):
    meeting = Meetings.objects.get(id = meeting_id)
    menus = Menu.objects.filter(shop = meeting.shop)
    members = Member.objects.filter(team = meeting.team)
    context = {'meeting':meeting, 'menus':menus, 'members':members}
    return render(request, 'snctrd/order.html', context)
    
def createOrder(request):
    
    membername = request.POST['membername']
    menuid = request.POST['menuid']
    quantity = request.POST['quantity']
    note = request.POST['note']
    meetingid = request.POST['meetingid']
    amount = request.POST['amount']
    
    today = datetime.datetime.now()
    menu = Menu.objects.get(id = menuid)
    meeting = Meetings.objects.get(id = meetingid)
    
    try:
        oldOrder = Order.objects.get(meeting = meeting, membername = membername)
    except:
        oldOrder = None
        
    status = 's'
        
    if (oldOrder) :
        oldOrder.delete()
        status = 'u'
    
    newOrder = Order.objects.create(
        meeting = meeting,
        membername = membername,
        menu = menu,
        quantity = quantity,
        amount = amount,
        note = note,
        crdate = today
        )
        
    newOrder.save()
    return HttpResponse(status)
    
def deleteOrder(request):
    orderid = request.POST['orderid']
    status = 's'
    order = Order.objects.get(id = orderid)
    order.delete()
    return HttpResponse(status)
    
def orderSummary(request, meeting_id):
    meeting = Meetings.objects.get(id = meeting_id)
    orders  = Order.objects.filter(meeting = meeting)
    
    orderList = []
    for order in orders:
        
        orderDict = {}
        keyFlag = False
        keyIdx = 0
        
        keyFlag, keyIdx = getArrayIndexByKeyValue(orderList,'menu',order.menu.name)
        
        if (keyFlag == False) :
            orderDict['menu'] = order.menu.name
            orderDict['qty'] = order.quantity
            orderDict['price'] = order.menu.price
            orderList.append(orderDict)
        elif (keyFlag == True) :
            orderList[keyIdx]['qty'] += order.quantity
            orderList[keyIdx]['price'] += order.menu.price
            
    orderListSum = []
    for ord in orderList:
        orderListSum.append(json.dumps(ord))
            
    # context = {'meeting':meeting, 'orders':orders, 'orderList':json.dumps(orderList)}
    context = {'meeting':meeting, 'orders':orders, 'orderList':orderListSum}
    return render(request, 'snctrd/orderSummary.html', context)
    
def getArrayIndexByKey(arr, key):
    cnt = 0
    for array in arr:
        flag = key in array
        if flag == True :
            return True, cnt
        else:
            cnt += 1
    return False, cnt
    
def getArrayIndexByKeyValue(arr, key, value):
    cnt = 0
    for array in arr:
        flag = value in array[key]
        if flag == True :
            return True, cnt
        else:
            cnt += 1
    return False, cnt
    
# function getArrayIndexByKey(arr, key, value) {
# 	for (var i = 0; i < arr.length; i++) {
# 		if (arr[i][key] == value) {
# 			return i;
# 		}
# 	}
# }