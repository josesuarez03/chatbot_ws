import requests
import json

url = "https://graph.facebook.com/v17.0/104233262729435/messages"
headers = {
    "Authorization": "Bearer EAALk9OcQolIBO497djNIAVkOPMjA58YfeRfm7JWnROjGtrFAN9eV8vChJKhrbtNa3eaZAZCevoPZBkDQ0oBLQReWQc1ZBCwjcBxbcH63fD6exHbdDdA1W5ZAg5sOfGDwAFSYeWvfcca9z8abwdAEhn5weqorYlYnp0YDIdj52QdLbyOrxNrZC3xZB37lrehNYnFmAT8IhrMJJ2ldaUDXpMZD",
    "Content-Type": "application/json"
}


data = {
    "messaging_product": "whatsapp",
    "to": "34654156175",
    "type": "text",
    "text": {
        "content": "¡Hola! ¿En qué puedo ayudarte?"
    }
}

data_json = json.dumps(data)

response = requests.post(url, headers=headers, data=data_json)

message = input("Escribe un mensaje: ")

if message.lower() == "hola":
    data["text"] = "¡Hola! ¿En qué puedo ayudarte?"
else:
    data["text"] = "Lo siento, no puedo entender tu mensaje."

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Mensaje enviado con éxito a WhatsApp.")
else:
    print("Error al enviar el mensaje a WhatsApp:", response.text)