import sys
sys.path.append('../lib')
from meli import Meli

def main():
    meli = Meli(client_id=CLIENT_ID,client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
    response = meli.delete("/questions/QUESTION_ID", {'access_token':meli.access_token})
    print response.content

if __name__ == "__main__":
    main()
