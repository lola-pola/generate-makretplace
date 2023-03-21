import streamlit as st
import os

from generatepromt import sending_prompt , generate_code , generate_web ,generate_data_from_turbo
from daliegenerator import sending_picture ,sending_picture_small

res = ""
st.title("ChatGPT-like Web App")
shop = st.text_input("what this shop sells?")
shop_prompt = st.text_input("please add a prompt for the shop:",max_chars=2400)
# shop_prompt = st.text_input("please add a prompt for the shop:",max_chars=2400)
# shop_prompt = st.text_input("please add a prompt for the shop:",max_chars=2400)
# shop_prompt = st.text_input("please add a prompt for the shop:",max_chars=2400)


# generate web content for an online milkshake shop that specializes in healthy unique and delicious milkshakes , generate a clear description of your milkshake shop and write descriptions for 5 of your milkshakes,for each milkshake, provide a prompt for generating Dali-esque descriptions\n\nWelcome to our online milkshake shop, where we specialize in healthy, unique and delicious milkshakes. Our milkshakes are made with only the finest ingredients and are sure to tantalize your taste buds. We have a wide range of flavors, from classic favorites to one-of-a-kind creations. Whether you’re looking for a creamy treat or a refreshing fruity shake, we have something for everyone. So come and explore our delicious selection.\n\n1. Caramel Cappuccino Milkshake: Our Caramel Cappuccino Milkshake is a unique blend of smooth caramel, creamy cappuccino and luscious cream. A special treat for coffee and caramel lovers, this is the perfect pick-me-up.\n\nDali-esque Description: This Milkshake is an artful blend of caramel and cappuccino, swirling together in a creamy canvas of delight.\n\n2. Raspberry Coconut Milkshake: Our Raspberry Coconut Milkshake is a delicious mix of sweet raspberries and creamy coconut. A refreshing and tropical combination, this shake will transport you to paradise with each sip.\n\nDali-esque Description: A heavenly blend of raspberries and coconut, this Milkshake is a delectable dreamscape of flavor.\n\n3. Banana Chocolate Milkshake: Our Banana Chocolate Milkshake is a classic combo of ripe, juicy bananas and rich chocolate. An indulgent treat, this shake is a favorite among all ages.\n\nDali-esque Description: Luscious chocolate and ripe bananas mix together in a swirl of sweet delight.\n\n4. Peanut Butter Cup Milkshake: Our Peanut Butter Cup Milkshake is a creamy, decadent treat. A combination of smooth peanut butter and rich chocolate, this shake is sure to satisfy your sweet tooth.\n\nDali-esque Description: Peanut butter and chocolate create an unforgettable swirl of flavor in this dreamy Milkshake.\n\n5. Chai Tea Milkshake: Our Chai Tea Milkshake is a unique blend of chai tea and creamy milk. A spicy and creamy treat, this shake is perfect for those who love a good cup of chai.\n\nDali-esque Description: This Milkshake is a harmonious blend of chai tea and creamy milk, a tantalizing flavor that fills the senses.



# text1 = "generate web content for an online milkshake shop that specializes in healthy unique and delicious milkshakes"
# text2 = "generate a clear description of your milkshake shop and write descriptions for 5 of your milkshakes,for each milkshake, provide a prompt for generating Dali-esque descriptions"
# text = "generate manu from all the ingredients with prices in $"




click = st.button("Generate shop")
# print(click)
if click:
    # res += str(sending_prompt(prompt=shop_prompt)) + "~"
    _data = generate_data_from_turbo(prompt=shop_prompt) + "~"
    with open("data.txt", "a") as f:
        f.write(_data)
    # print(res)
    # print(data)
    # st.write(data)
    st.success("saved!")





    
if st.checkbox('finished'):
    st.write("Here is the generated website content:")
    st.image(sending_picture_small(data_prompt=shop))
    with open("data.txt", "r") as f:
        res = f.read()
    
    lister = res.split("~")    
    # for i in res.split("~"):
    #     st.write(i)
    get_title = []
    get_calasification = []
    # for each in lister:
    #     print(each)
    #     _get_calasification = sending_prompt(prompt='classify the following: '+each)
    #     # _get_title = sending_prompt(prompt=each+'Tl;dr')
    #     # _get_title = _get_title.replace('\n', '')
    #     _get_calasification = _get_calasification.replace('\n', '')
        
    #     get_calasification.append(_get_calasification)
    #     # get_title.append(_get_title)
    # get_calasification = list(filter(None, get_calasification))
    # # get_title = list(filter(None, get_title))

 
    # st.components.v1.html(generate_web(shop_prompt), height=1500, width=1500)




    tab1, tab2 , tab3 = st.tabs(["main web page", "about us", "menu"])
    _a =lister[0].split(".")
    
    tab1.image(sending_picture(data_prompt=_a))
    for item in _a :
        tab1.write(item)
    tab2.write(lister[1])
    tab2.image(sending_picture(data_prompt=item))
    _b =lister[2].split("-")
    for item in _b :
        item = item.replace('\n', '')
        tab3.write(item) 
        tab3.write("------") 
        tab3.image(sending_picture(data_prompt=item))

     
     
     
         
    # # st.write()

