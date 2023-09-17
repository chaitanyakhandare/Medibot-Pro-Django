# Medical Diagnosis Chatbot

import requests, json

# Age, Gender, symptoms, duration of symptom, severity of symptom,

# name = input("Enter your name: ")
# age = input("Enter your Age: ")
# gender = input("Enter your gender: ")
# symptoms = input("Enter your symptoms: ")
# duration_symptoms = input("Enter your duration_symptoms: ")
# severity = input("Enter your severity: ")

# promptToPass = f"hello my name is {name}, age is {age}, and gender is {gender}. I'm suffering from {symptoms}, since past {duration_symptoms} days. And that symptoms are {severity}. Please help me to provide information related to this symptoms"

example = "hello my name is Chaitanya, age is 20, and gender is male. I'm suffering from not able to smell anything, and having fever, since past 3 days. And that symptoms are mild. Please help me to provide information related to this symptoms"

example2 = "hello, im 22 years old. and having back pain. i need some exercise routing of a week"

example3 = "doctor gave me paracetamol, cheston cold total, and azethomycin, plz tell me uses of this tablet"


url = "https://api.worqhat.com/api/ai/content/v2"

payload = {"question": example3}
headers = {
    "Authorization": "Bearer sk-551bcfd3e22f417092c5db23cca5aee9",
    "Content-Type": "application/json",
}


print("DOING REQUEST")
response = requests.request("POST", url, json=payload, headers=headers)

if response.status_code == 200:
    toJSON = response.json()
    print(toJSON["content"])
else:
    print("Error:", response.text)


# print(promptToPass)
