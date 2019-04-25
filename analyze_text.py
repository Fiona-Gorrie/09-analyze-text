def analyze_text(string):
    ecount=0
    for i in string: 
        if i == "e": 
            ecount+=1

    capital_e_count=0
    for E in string: 
        if E == "E": 
            capital_e_count+=1

    total_e = capital_e_count + ecount        
        
    count=0
    for a in string: 
        if (a.isalpha()) == True: 
                count+=1
    percent = 100 * total_e / len(string)
    str_percent = "{:.2f}".format(percent)
                 
    return "the text contains " + str(count) + " alphabetic characters, of which "+str(total_e) + " (" + str_percent + "%) of them are e"

print(analyze_text("feEling"))
