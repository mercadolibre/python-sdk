import sys
sys.path.append('../lib')
from meli import Meli

def main():
    meli = Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)
    body = {"title":"Item De Teste - Por Favor, Não Ofertar! --kc:off","category_id":"MLB257111","price":10,"currency_id":"BRL","available_quantity":1,"buying_mode":"buy_it_now","listing_type_id":"bronze","condition":"new","description":"Item de Teste. Mercado Livre's PHP SDK.","video_id":"Q6dsRpVyyWs","warranty":"12 month","pictures":[{"source":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/IPhone_7_Plus_Jet_Black.svg/440px-IPhone_7_Plus_Jet_Black.svg.png"},{"source":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/IPhone7.jpg/440px-IPhone7.jpg"}],"attributes":[{"id":"EAN","value_name":"190198043566"},{"id":"COLOR","value_id":"52049"},{"id":"WEIGHT","value_name":"188g"},{"id":"SCREEN_SIZE","value_name":"4.7 polegadas"},{"id":"TOUCH_SCREEN","value_id":"242085"},{"id":"DIGITAL_CAMERA","value_id":"242085"},{"id":"GPS","value_id":"242085"},{"id":"MP3","value_id":"242085"},{"id":"OPERATING_SYSTEM","value_id":"296859"},{"id":"OPERATING_SYSTEM_VERSION","value_id":"iOS 10"},{"id":"DISPLAY_RESOLUTION","value_id":"1920 x 1080"},{"id":"BATTERY_CAPACITY","value_name":"3980 mAh"},{"id":"FRONT_CAMERA_RESOLUTION","value_name":"7 mpx"}]}
    response = meli.post("/items", body, {'access_token':meli.access_token})
    print response.content

if __name__ == "__main__":
    main()
