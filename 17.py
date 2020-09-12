import requests
import json

def send_photo():
    response = requests.get(
    'https://android.photo-filter.com/v1/user',
    headers={'android-device-token':'testDevs0daae7susui',
             'version': '1.1.2'},)
   # json_data = json.loads(response.text)
    data = response.json()
    print(data)


def sendphoto():
    changeHash()
    files = {'photo': open('tes.jpg', 'rb')}
    response = requests.post(
        'https://android.photo-filter.com/v1/user/photo',
        headers={'android-device-token': 'testDevs0daae7susui',
                 'version': '1.1.2'}, files=files)


    # json_data = json.loads(response.text)
   # data = response.json()
   # print(data)


def checkphoto():
    response = requests.get(
        'https://android.photo-filter.com/v1/user/photos',
        headers={'android-device-token': 'testDevs0daae7susui',
                 'version': '1.1.2'}, )
    # json_data = json.loads(response.text)
    data = response.json()
    #print(data)
    if data['photos'][0]['status'] == "completed":
        print("completed")
    else:
        print("not completed")


def jsoncheck(checkdata):
    data = json.loads(checkdata)
    if 'photos' not in data:
        raise ValueError("No target in given data")
    if 'status' not in data['photos'][0]:
        raise ValueError("No data for target")
    if data['photos'][0]['status'] != "completed":
        print("not completed")
    print(data['photos'][0]['status'])

def changeHash():
    file = open('tes.jpg', 'rb').read()
    with open('tes.jpg', 'wb') as new_file:
        new_file.write(file + b'\0')

def ios():
    response = requests.get(
    'https://api.photo-filter.com/v1/settings',
    headers={'ios-device-token':'testDevs0daae7susui',
             'version': '1.19'},)
   # json_data = json.loads(response.text)
    data = response.json()
    print(data)

#changeHash()
sendphoto()
#jsoncheck(checkphoto())
checkphoto()
#ios()