from django.shortcuts import render, HttpResponse
import requests
import asyncio


# its a general function not a view
async def textGen(promptToPass):
    url = "https://api.worqhat.com/api/ai/content/v2"
    payload = {"question": promptToPass}

    loop = asyncio.get_event_loop()

    def make_request():
        headers = {
            "Authorization": "Bearer sk-551bcfd3e22f417092c5db23cca5aee9",
            "Content-Type": "application/json",
        }
        response = requests.post(url, json=payload, headers=headers)
        return response

    response = await loop.run_in_executor(None, make_request)

    if response.status_code == 200:
        toJSON = response.json()
        resultOutput = toJSON['content']
    else:
        resultOutput = f"Error: {response.status_code}"

    return resultOutput


async def generateImage(painType):
    urlImg = "https://api.worqhat.com/api/ai/images/generate/v2"

    payload = {
        "output_type": "url",
        "prompt": [painType],
    }

    headers = {
        "Authorization": "Bearer sk-551bcfd3e22f417092c5db23cca5aee9",
        "Content-Type": "application/json",
    }

    loop = asyncio.get_event_loop()

    def make_request():
        responseImg = requests.post(urlImg, json=payload, headers=headers)
        return responseImg

    responseImg = await loop.run_in_executor(None, make_request)

    if responseImg.status_code == 200:
        toImgJSON = responseImg.json()
        exerciseimg = toImgJSON['content']
    else:
        exerciseimg = responseImg.text

    return exerciseimg





# Create your views here.

def home(request):
    return render(request, 'home.html')

async def medicalDiag(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        symptoms = request.POST.get('symptoms')
        duration = request.POST.get('duration')
        severity = request.POST.get('severity')
        print(name, age, gender, symptoms, duration, severity)

        promptToPass = f"hello my name is {name}, age is {age}, and gender is {gender}. I'm suffering from {symptoms}, since past {duration} days. And that symptoms are {severity}. Please help me to provide information and name of the disease related to this symptoms"

        # text generation API output
        textOutput = await textGen(promptToPass)

        context = {
            "output" : textOutput
        }
        return render(request, 'medicalDiag.html', context=context)


    return render(request, 'medicalDiag.html')



async def physiobot(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        painType = request.POST.get('paintype')
        duration = request.POST.get('duration')
        severity = request.POST.get('severity')
        print(name, age, gender, painType, duration, severity)

        promptToPass = f"hello my name is {name}, age is {age}, and gender is {gender}. I'm suffering from {painType}, since past {duration} days. And that pain is {severity}. Please suggest me some exercises for week to cure this."

        # Text generation API output
        textOutput = await textGen(promptToPass)

        # Image generation API output
        exerciseimg = await generateImage(painType)

        context = {
            "output" : textOutput,
            "exerciseimg" : exerciseimg
        }
        return render(request, 'physiobot.html', context=context)

    
    return render(request, 'physiobot.html')




def support(request):
    if request.method == 'POST':
        userInput = request.POST.get('any-bot-input')
        print(userInput)

        url = "https://api.worqhat.com/api/ai/content/v2"

        payload = {"question": userInput}
        headers = {
            "Authorization": "Bearer sk-551bcfd3e22f417092c5db23cca5aee9",
            "Content-Type": "application/json",
        }
        print("DOING REQUEST")
        responseAny = requests.request("POST", url, json=payload, headers=headers)

        if responseAny.status_code == 200:
            toAnyJSON = responseAny.json()
            anyOutput = toAnyJSON['content']
            print(anyOutput)
        else:
            anyOutput = responseAny.text
            print("Error:", anyOutput)


        context = {
            "clickMsg" : anyOutput
        }
        return render(request, 'support.html', context)


    noContext = {
        "clickMsg" : "Please click on Search Button"
    }
    return render(request, 'support.html', noContext)





def about(request):
    return render(request, 'about.html')


def report(request):
    return render(request, 'report.html')




