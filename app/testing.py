# #testing the edamam API here
import requests

url =  "https://api.edamam.com/api/recipes/v2"

res = requests.get(url, params={'type':'public', 'app_id':"97c8bd4c", 'app_key':"99402c4f99681503751e94b03de8db33", 'q': "beef", 'health': ["gluten-free", "egg-free"]})

print(res.json()['hits'][3]['recipe']['label']) # prints the name of the first chicken recipe 
print(len(res.json()['hits']))
# print()
# # print(res.json())
# #print(res.json()['hits'][0]['recipe']['url']) 
# print(res.json()['hits'][0]['recipe']['healthLabels'])
# print()
# print(res.json()['hits'][0]['recipe']['dietLabels'])  
# print()
# print(res.json()['hits'][0]['recipe']['cautions']) 
# print()
# print(res.json()['hits'][0]['recipe']['ingredientLines'])
# # print(res.json()['hits'][0]['recipe']['label']) 
# # print(res.json()['hits'][0]['recipe']['cuisineType']) 
# print(res.json()['hits'][0]['recipe']['images']['SMALL']['url'])
# print(res.json()['hits'][0]['recipe']['images']['REGULAR']['url'])
# print(res.json()['hits'][0]['recipe']['images']['LARGE']['url'])

# #testing the spoonacular API here: 
# import requests
# #res = requests.get("https://api.spoonacular.com/recipes/complexSearch?apiKey=12643cbc7c944fc18030685f17426c85").json() #request to get random recipe
# res = requests.get("https://api.spoonacular.com/recipes/random?apiKey=12643cbc7c944fc18030685f17426c85&number=1&intolerances=seafood,dairy").json()
# print(res.get('recipes')[0].get('title')) #gets the recipe title of that random recipe
#print(res.get('recipes')[0].get('image')) #gets the recipe image of that random recipe


#testing string indexing for the url
# string = "/randRecipe/translate/Jambalaya Stew/None/https://www.foodista.com/recipe/HG72GN7R/jambalaya-stew/https://spoonacular.com/recipeImages/www.foodista.com/recipe/HG72GN7R/jambalaya-stew/https://spoonacular.com/recipeImages/648432-556x370.jpg"
# index1= (string.index("http"))
# index2 = (string.index("http", string.index("http")+1))
# print(string[index1:index2])
# print(string[index2:])

#testing google translate api
#import requests

# f = open('app/keys/key_googleTranslate.txt')
# g_key = f.read() #google translate key
# print(g_key)

# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

# q = "pinnapple fired rice!"
# target = "ja"
# payload = f"source=en&target={target}&q={q}" 
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"Accept-Encoding": "application/gzip",
# 	"X-RapidAPI-Key": str(g_key),
# 	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

# testing cocktail recipe
# url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
# res = requests.get(url).json() #request to get random recipe
# title = res.get('drinks')[0].get("strDrink") #gets the recipe title of that random recipe
# image_url = res.get('drinks')[0].get('strDrinkThumb') #gets the recipe image of that random recipe

# print(title)
# print(image_url)
# print(res)

