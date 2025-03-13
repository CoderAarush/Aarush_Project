import random
import json
import torch
from model import NeuralNet
from nltk_utils import tokenize, bag_of_words

def run():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    with open('intents.json', 'r') as f:
        intents = json.load(f)

    File = "/Users/rajeeva/Documents/Aarush HTML5/data.pth"
    data = torch.load(File)
    input_size = data['input_size']
    output_size = data['output_size']
    hidden_size = data['hidden_size']
    all_words = data['all_words']
    tags = data['tags']
    model_state = data['model_state']
    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()
    bot_name = "Chatterbot"
    print("Hello I am " + bot_name + ". Lets chat! If you want to exit type quit")
    while True:
        sentence = raw_input("You: ")
        if sentence == "quit":
            break
        sentence = tokenize(sentence)
        X = bag_of_words(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        x = torch.from_numpy(X)
        x.to(device)
        output = model.foward(x)
        _, predicted = torch.max(output, dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() >= 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print("{}".format(bot_name) + ": {}".format(random.choice(intent['responses'])))
        else:
            print("Sorry I did not understand")

run()