def party():
    print("Estou fora")

    def Start_party():
        return "Estou dentro"

    def Finish_party():
        return "Acabou a festa"

    print(Start_party())
    print(Finish_party())

party()