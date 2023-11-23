import requests
from bs4 import BeautifulSoup

def get_food_calories(food_name):
    base_url = "https://calorizator.ru"
    search_url = f"{base_url}/product/search?q={food_name}"

    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Находим первую ссылку на результат поиска
    first_result = soup.find('a', class_='js-link-product', href=True)

    if first_result:
        food_url = base_url + first_result['href']
        food_response = requests.get(food_url)
        food_soup = BeautifulSoup(food_response.content, 'html.parser')

        # Находим информацию о калорийности
        calories_tag = food_soup.find('td', class_='hidden-xs kcal_bzh')
        if calories_tag:
            calories = calories_tag.text.strip()
            return calories

    return None

#if calories_russian is not None:
#   print(f"Калорийность {food_name_russian}: {calories_russian}")
#else:
#    print(f"Информация о калорийности {food_name_russian} не найдена.")
