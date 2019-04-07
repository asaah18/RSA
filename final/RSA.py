import hashlib


def FEMA(m, e: int, n):
    binE = bin(e)[2:]

    i = 0
    d = 1
    while i < len(binE):
        curE = binE[i:i + 1]
        # print(binE[i])
        if curE == '1':
            d = d * d * m
            d = d % n
            # print(d)
        else:
            d = d * d
            d = d % n
            # print(d)
        i = i + 1

    return d


# taking parameter from the user
def Encryption(PlainText, e, n, d, n2):
    TextAscii = []
    TextBin = []
    i = 0
    Temp = 0
    HashMessage = "\nH\n"
    SignMessage = "\nS\n"

    # From text to ascii
    while i < len(PlainText):
        TextAscii.append(ord(PlainText[i]))
        i = i + 1

    i = 0
    # From ascii to binary
    while i < len(TextAscii):
        Temp = f'{TextAscii[i]:08b}'
        TextBin.append(Temp)
        i = i + 1

    # All binary numbers in 1 variable
    TextBinFull = (format(0, '08b'))
    i = 0
    while i < len(TextBin):
        Temp = TextBin[i]
        TextBinFull = TextBinFull + Temp
        i = i + 1

    # binary to integer
    TextInt = int(TextBinFull, 2)

    # Encryption
    EncryptedText = FEMA(TextInt, e, n)

    # Hash md5
    hashObject = hashlib.md5()
    hashObject.update(PlainText.encode('utf-8'))
    hashObject = int(hashObject.hexdigest(), 16)

    # sign
    Sign = FEMA(hashObject, d, n2)

    # Save in encryption.txt File
    file2 = open("encryption.txt", "w")

    file2.write('%d' % EncryptedText)
    file2.write(HashMessage)
    file2.write('%d' % hashObject)
    file2.write(SignMessage)
    file2.write('%d' % Sign)
    file2.close()

    return str(EncryptedText) + str(HashMessage) + str(hashObject) + str(SignMessage) + str(Sign)


###################################################################################


# taking parameter from the user
def Decryption(TextEncryp: str, d, n, e, n2):

    # extract content of encryption text
    spliter = TextEncryp.split("\n")
    TextEncrp = spliter[0]

    print(TextEncrp)

    TextDecrpInt = []
    TextDecrpBin = []
    TextDecrpAsc = []
    Dencrpt = []
    DecrptBinList = []
    TextDecrpMessage = []

    m = int(TextEncrp)

    # Decryption
    x = FEMA(m, d, n)

    # Decryption binary
    DecryptBin = int(x)
    DecryptBin = bin(DecryptBin)
    DecryptBin = DecryptBin[2:]

    i = 0

    # Finding out the length of the First number
    if len(DecryptBin) % 8 == 1:
        start = 1
        End = 0
    elif len(DecryptBin) % 8 == 2:
        start = 2
        End = 0
    elif len(DecryptBin) % 8 == 3:
        start = 3
        End = 0
    elif len(DecryptBin) % 8 == 4:
        start = 4
        End = 0
    elif len(DecryptBin) % 8 == 5:
        start = 5
        End = 0
    elif len(DecryptBin) % 8 == 6:
        start = 6
        End = 0
    elif len(DecryptBin) % 8 == 7:
        start = 7
        End = 0
    else:
        start = 0
        End = 0

    start = start
    temp = DecryptBin[End:start]
    # print(temp)
    DecrptBinList.append(temp)
    i = 1
    End = start
    start = start + 8
    while i < len(DecryptBin) / 8:
        temp = DecryptBin[End:start]
        # print(temp)
        DecrptBinList.append(temp)
        start = start + 8
        End = End + 8
        i = i + 1

    # turning binary to ascii
    i = 0
    while i < len(DecrptBinList):
        Temp = chr(int(DecrptBinList[i], 2))
        TextDecrpAsc.append(Temp)
        i = i + 1

    file3 = open("Decryption.txt", "w")

    print(TextDecrpAsc)
    i = 0
    while i < len(DecrptBinList):
        file3.write(TextDecrpAsc[i])
        i = i + 1

    # hash
    TextDecrpMessage = ''.join(TextDecrpAsc)
    CalculHash = hashlib.md5()
    CalculHash.update(TextDecrpMessage.encode('utf-8'))
    CalculHash = int(CalculHash.hexdigest(), 16)

    Hash = spliter[2]
    Sign = spliter[4]
    # flag = 0

    # with open("encryption.txt") as f:
    #     for line in f:
    #         if flag == 1:
    #             Hash = line
    #             flag = 0
    #         if flag == 2:
    #             Sign = line
    #             flag = 0
    #         if line.startswith("H"):
    #             flag = 1
    #         if line.startswith("S"):
    #             flag = 2

    Hash = int(Hash)

    if CalculHash == Hash:
        alter_flag: bool = True
        print("Hash match")
    else:
        alter_flag: bool = False
        print("Hash not match")

    S = FEMA(int(Sign), e, n2)

    if S == Hash:
        entity_flag: bool = True
        print("Sign match")
    else:
        entity_flag: bool = False
        print("Sign not match")

    file3.close()
    # f.close()

    return {'message': TextDecrpMessage, 'alter validation': alter_flag, 'entity validation': entity_flag}


# print(Decryption(
# '''39911455544647797021650277082789443697800522384388317713827861739361699364312214511222070884048350721959932226808441296938721133167631429508306205462077973692371340884455682265005620056948974514610424466631013026864890084652826909845335475487994276361340556976601285615792459830616596918959486303239195272113
# H
# 0000000000000000
# S
# 00000000000000000
# '''
# , 25079271364692071886807003489651762565109941906241966752763754318564055067826434712518809332720845941110950732808529750683387168507392116893613530695737796135084749454993580940392206236561127450672235436474892780631879663684357524880403491024496733640447973823554159945947035732618297216976932212549229655159665350808948938395622513289377614698334376381616988880527580706317570975147956943879080715011001441932663240863697489490856532627100237436230704315121053108037798213488161816992612864241470853762896314041261593567760158274414974409299438191120958589933462631937756069786930475260535226660599106798636792167237,
# 5736961884214160137853826807515119698700660986936171775467519580859212776226510062011736642087581784433085032477411447281802011739277638938064604790787627144711997523856859974464004979217516256706325438909716384795473973015567443249451755505511835360622263818420502621865702151683849663035650166744290613996382223988628311184654024513794533066358766487510828245154377422314419553038006044034362340056618185114182492364248903796606519116774919551253690705457998772572435461094436161679793893464569014288698635704165696874027200718584173741608715940428292214153420893523017570478145738396318753393586735090007287042453,
# 30871917260627496498241978189902398888119963724832185443911708699998590744136625697492754526844207694611664920920515988318365220181009534902098974495095665656262568146022037210536462837310505841238437110250728010695488633196234170575835306008168951455312374659953494291801009459775501105937313410003391864660185250034085005242646922008487291108416633432947762364526547572501437601155325688752019682064862599317743101890729435143578343108588025007773536835157313516260501104173164798617838127509172117076613367212167882663400991099826242562380888266623071298728088283555305988092789871429547158376253429850093342640411,
# 123067813130773518801232410491671120056960423406113472380398523123138268548746092872607989751927025370131317811472695140775435716898350574480858109695301478714914257198152630226008064828609150336162108720024203404182289293119648402796770619942440335669457413752640805971610349992548530868869865829398722683057
#             ))



