class Phone:
    def __init__(self, phone_number):
        self.call_history = []
        self.messages = []
        self.number = phone_number

    def call(self, other_number):
        print(f"{self.number} called to {other_number.number}")
        self.call_history.append(other_number.number)

    def send_message(self, other_number):
        print(f"{self.number} send a message to {other_number.number}.")
        text = input("Text: ")
        message = {
            "number_to": other_number.number,
            "number_from":self.number,
            "text": text
        }
        other_number.messages.append({
            "number_to": other_number.number,
            "number_from":self.number,
            "text": text})
        self.messages.append(message)
        return other_number
    def show_messages(self):
        print(f"____Messages history of {self.number}:_____")
        for i in range(0, len(self.messages)):
            print(f"Number: {self.messages[i]["number_to"]}\nText: {self.messages[i]["text"]}")

    def show_call_history(self):
        print(f"_____Call history of {self.number}:_____")
        for i in range(0, len(self.call_history)):
            print(self.call_history[i])
    def show_outgoing_messages(self):
        print(f"_____Outgoing messages {self.number}:____")
        for i in range(0, len(self.messages)):
            if self.messages[i]["number_from"] == self.number:
                print(f"Number: {self.messages[i]["number_to"]}\nText: {self.messages[i]["text"]}")
    def show_incoming_messages(self):
        print(f"_____ Incoming messages to {self.number}: _____")
        for i in range(0, len(self.messages)):
            if self.messages[i]["number_to"] == self.number:
                print(f"From: {self.messages[i]["number_from"]}\nText: {self.messages[i]["text"]}")
    def show_messages_from(self, phone):
        print(f"______Messages from {phone.number}:_________")
        for i in range(0, len(self.messages)):
            if self.messages[i]["number_from"] == phone.number:
                print(f"From: {self.messages[i]["number_from"]}\nText: {self.messages[i]["text"]}")


def main():
    my_phone = Phone("+000")
    other_phone1 = Phone("+111")
    other_phone2 = Phone("+222")
    other_phone3 = Phone("+333")
    print("-----------------")
    my_phone.call(other_phone1)
    my_phone.call(other_phone2)
    my_phone.call(other_phone2)
    my_phone.call(other_phone3)
    my_phone.send_message(other_phone1)
    other_phone1.send_message(my_phone)
    my_phone.send_message(other_phone1)
    my_phone.show_call_history()
    other_phone3.send_message(my_phone)
    other_phone3.send_message(my_phone)
    other_phone2.send_message(my_phone)
    my_phone.show_messages()
    my_phone.show_incoming_messages()
    my_phone.show_outgoing_messages()
    my_phone.show_messages_from(other_phone3)






if __name__ == "__main__":
    main()
