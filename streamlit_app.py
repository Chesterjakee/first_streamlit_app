import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('HAPPY 2ND MONTHSARY')
streamlit.header(' BABY BOYFRIEND ASAWA')
streamlit.text('Hi baby, boyfriend, my asawa. Happy monthsary to the both of us. Baby ko, I love you very very very very much. There\'s no ruler or a measuring tool that can measure this love that I\'m feeling for you. You are a treasure that I will always value. Thank you for being with me always. You know how lucky I am that God gave me a kind of person that understands, loves and proud of who I am. Baby ko, I hope that you\'ll always there for me not only in happiness but also in sadness, whatever season there is although 2 seasons lang naman tayo. Baby kopo, I\'m always here for you po, support on the things that you\'ll do that will benefit you of course. 
')

'''
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected =  streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

streamlit.header('View Our Fruit List - Add Your Favorites!')
def get_fruit_load_list():
     with my_cnx.cursor() as my_cur:
          my_cur.execute("select * from fruit_load_list")
          return my_cur.fetchall()
if streamlit.button('Get Fruit List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     my_data_rows = get_fruit_load_list()
     my_cnx.close()
     streamlit.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
     with my_cnx.cursor() as my_cur:
          my_cur.execute("insert into fruit_load_list values ('" + new_fruit +"')")
          return "Thanks for adding" + new_fruit
        
add_my_fruit = streamlit.text_input('What fruit would you like to add?')     
if streamlit.button('Add a Fruit to the List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(add_my_fruit)
     streamlit.text(back_from_function)'''
