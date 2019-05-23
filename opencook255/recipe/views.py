from django.shortcuts import render,redirect
from .models import Recipe
from django.http import JsonResponse
from django.core import serializers
from django import forms
from django.contrib import messages
import requests
from bs4 import BeautifulSoup 
import json
# Create your views here.

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = ['title' , 'image_path' , 'description']

def get_recipes_api(request):
	recipes = Recipe.objects.all()
	data = serializers.serialize('json',recipes)
	return JsonResponse({'data': data})

#================================================================#
def get_recipe(request, recipe_id):
	print(recipe_id)
	recipe = Recipe.objects.get(pk = recipe_id)

	return render(request,'recipe.html' , locals())

def get_create_recipe(request):
	return render(request,'create_recipe.html')

def post_create_recipe(request):
	if request.method == 'POST':
		form = RecipeForm(request.POST)
		if form.is_valid():
			new_recipe  = form.save() #收集fields的資料
			print(new_recipe)
			messages.add_message(request , messages.SUCCESS,'Share Sucessful!!!')
			return redirect('/',locals())
		else:
			return redirect('/recipes/create')

def get_crawler(request):
	food = requests.get("https://api.thingspeak.com/channels/600831/fields/1.json")
	food.encoding = 'utf-8'
	soup = BeautifulSoup(food.text, "html.parser")
	X=json.loads(str(soup))
	count = len(X['feeds'])
	food_last4 = X['feeds'][count-4:count-3]
	food_last3 = X['feeds'][count-3:count-2]
	food_last2 = X['feeds'][count-2:count-1]
	food_last1 = X['feeds'][count-1:count]

	water = requests.get("https://api.thingspeak.com/channels/600831/fields/2.json")
	water.encoding = 'utf-8'
	soup2 = BeautifulSoup(water.text, "html.parser")
	X2=json.loads(str(soup2))
	count2 = len(X['feeds'])
	water_last4 = X2['feeds'][count2-4:count2-3]
	water_last3 = X2['feeds'][count2-3:count2-2]
	water_last2 = X2['feeds'][count2-2:count2-1]
	water_last1 = X2['feeds'][count2-1:count2]
	for i in water_last4:
		i['field2'] = str(float(i['field2'])*0.303*100)
	for i in water_last3:
		i['field2'] = str(float(i['field2'])*0.303*100)
	for i in water_last2:
		i['field2'] = str(float(i['field2'])*0.303*100)
	for i in water_last1:
		i['field2'] = str(float(i['field2'])*0.303*100)

	big_water = requests.get("https://api.thingspeak.com/channels/600831/fields/3.json")
	big_water.encoding = 'utf-8'
	soup3 = BeautifulSoup(big_water.text, "html.parser")
	X3=json.loads(str(soup3))
	count3 = len(X['feeds'])
	big_water_last4 = X3['feeds'][count3-4:count3-3]
	big_water_last3 = X3['feeds'][count3-3:count3-2]
	big_water_last2 = X3['feeds'][count3-2:count3-1]
	big_water_last1 = X3['feeds'][count3-1:count3]

	big_food = requests.get("https://api.thingspeak.com/channels/600831/fields/4.json")
	big_food.encoding = 'utf-8'
	soup4 = BeautifulSoup(big_food.text, "html.parser")
	X4=json.loads(str(soup4))
	count4 = len(X['feeds'])
	big_food_last4 = X4['feeds'][count4-4:count4-3]
	big_food_last3 = X4['feeds'][count4-3:count4-2]
	big_food_last2 = X4['feeds'][count4-2:count4-1]
	big_food_last1 = X4['feeds'][count4-1:count4]


	return render(request,"crawler.html",locals())