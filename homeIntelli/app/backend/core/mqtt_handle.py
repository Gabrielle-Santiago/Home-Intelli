def handle_message(topic: str, payload: str):
    if topic == "home/temperature":
        trata_temperatura(payload)
    else:
        print(f"Mensagem recebida sem tratamento para o tópico {topic}")

def trata_temperatura(payload):
    print(f"*****Temperatura recebida: {payload}*****")
