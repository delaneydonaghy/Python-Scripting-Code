
print("Plaintext to Cypertext\n");
while(1==1):
    plain = input("Enter Plaintext: ");

    cipher = "";
    for index in range(len(plain)):
        cipher += chr(ord(plain[index]) + 3);

    print("Ciphertext: %s" % cipher);
    answer= input("More Text? (Y or N): ");
    if(answer == "Y"):
        continue
    if(answer == "N"):
        break

print("\n*************************\n")
print("Cypertext to Plaintext\n");

while(1==1):
    cipher = input("Enter Ciphertext: ");

    plain = "";
    for index in range(len(cipher)):
        plain += chr(ord(cipher[index]) - 3);

    print("Plaintext: %s" % plain);
    answer= input("More Text? (Y or N): ");
    if(answer == "Y"):
        continue
    if(answer == "N"):
        break
