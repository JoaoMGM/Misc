from traceback import print_tb

def calc():
    print("Calculation for Epic Equipment(Craft values of the equip not included):")
    red1 = int(input("Epic Material(Steel/Platinum)- "))
    red2 = int(input("Epic Material(Evil/Quint/Illuminating)- "))
    red3 = int(input("Epic Material(Moon/Exorcism/Anima)- "))
    blue1 = int(input("Rare Material(Steel/Platinum)- "))
    blue2 = int(input("Rare Material(Evil/Quint/Illuminating)- "))
    blue3 = int(input("Rare Material(Moon/Exorcism/Anima)- "))
    green1 = int(input("Uncommon Material(Steel/Platinum)- "))
    green2 = int(input("Uncommon Material(Evil/Quint/Illuminating)- "))
    green3 = int(input("Uncommon Material(Moon/Exorcism/Anima)- "))

    print("-----------------------------------------------------------------------------")
    #opcao incluindo verdes
    print("Needed Materials(Including craft to Rare):")
    Mat1 = ((30000-(red1*10*10)-(blue1*10)))
    print("Material 1 ->" + str(Mat1-green1) + " Uncommon")
    Mat2 = ((10000-(red2*10*10)-(blue2*10)))
    print("Material 2 ->" + str(Mat2-green2) + " Uncommon")
    Mat3 = ((10000-(red3*10*10)-(blue3*10)))
    print("Material 3 ->" + str(Mat3-green3) + " Uncommon")
    CopperWaste = ((((Mat3+Mat2+Mat1)/10)*2000) + ((((Mat3+Mat2+Mat1)/100)+((blue1+blue2+blue3)/10))*20000))
    PowWaste = ((((Mat3+Mat2+Mat1)/10)*2) + ((((Mat3+Mat2+Mat1)/100)+((blue1+blue2+blue3)/10))*25))
    DsWaste = ((((Mat3+Mat2+Mat1)/10)*1000) + ((((Mat3+Mat2+Mat1)/100)+((blue1+blue2+blue3)/10))*5000))
    print("Copper Waste ->" + str(CopperWaste))
    print("Powder Waste ->" + str(PowWaste))
    print("Darksteel Waste ->" + str(DsWaste))

    print("-----------------------------------------------------------------------------")

    #opcao de raros
    print("Needed Materials(Only craft to Epic):")
    Mat1 = ((3000-(red1*10)))
    print("Material 1 ->" + str(Mat1-blue1) + " Rare")
    Mat2 = ((1000-(red2*10)))
    print("Material 2 ->" + str(Mat2-blue2) + " Rare")
    Mat3 = ((1000-(red3*10)))
    print("Material 3 ->" + str(Mat3-blue3) + " Rare")
    CopperWaste = (((Mat3+Mat2+Mat1)/10)*20000)
    PowWaste = (((Mat3+Mat2+Mat1)/10)*25)
    DsWaste = (((Mat3+Mat2+Mat1)/10)*5000)
    print("Copper Waste ->" + str(CopperWaste))
    print("Powder Waste ->" + str(PowWaste))
    print("Darksteel Waste ->" + str(DsWaste))

    print("-----------------------------------------------------------------------------")


    #opção ideal
    print("Materials Needed(Optimized Version based on how you gather materials faster):")
    Mat1 = ((3000-(red1*10)-blue1))
    print("Material 1 ->" + str(Mat1) + " Rare")
    Mat2 = ((10000-(red2*10*10)-(blue2*10)))
    print("Material 2 ->" + str(Mat2-green2) + " Uncommon")
    Mat3 = ((10000-(red3*10*10)-(blue3*10)))
    print("Material 3 ->" + str(Mat3-green3) + " Uncommon")
    CopperWaste = (((Mat1+blue1)/10)*20000) + (((((Mat3+Mat2)/10)*2000) + (((Mat3+Mat2+blue3*10+blue2*10)/100)*20000)))
    PowWaste = (((Mat1+blue1)/10)*25) + ((((Mat3+Mat2)/10)*2) + (((Mat3+Mat2+blue3*10+blue2*10)/100)*25))
    DsWaste = (((Mat1+blue1)/10)*5000) + (((((Mat3+Mat2)/10)*1000) + (((Mat3+Mat2+blue3*10+blue2*10)/100)*5000)))
    print("Copper Waste ->" + str(CopperWaste))
    print("Powder Waste ->" + str(PowWaste))
    print("Darksteel Waste ->" + str(DsWaste))
    print("-----------------------------------------------------------------------------")
i=0
while i==0:
    calc()
