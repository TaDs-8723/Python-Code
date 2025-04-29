phone_number=int(input("What is your seven digit phone number?"))
pref_numb=phone_number//10000
suffix_numb=phone_number-(pref_numb*10000)
prenumb_subtotal=pref_numb*80
pre_numb_total=(prenumb_subtotal+1)*250
subtotal=pre_numb_total+(2*suffix_numb)
total=int((subtotal-250)/2)
print("Your prefix is",pref_numb,". Multiply it by 80, and the result is:",prenumb_subtotal)
print("Add 1 to that result and multiply it by 250, and the result is:",pre_numb_total)
print("Your line number is",suffix_numb,". Add this to the previous result twice, and the result is:",subtotal)
print("Subtract 250 from that result and divide it by 2, and the result is:",total)
