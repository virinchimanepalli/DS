import re

new_cc=str("61234-567-8912-3456")
#### to check the total lengt
without_hyp=new_cc.replace("-","")
###check for starting with 4,5 or 6 and {1234}: 4 digits within each group
match=re.search(r"^(4|5|6)[1-9]{3}-?[1-9]{4}-?[1-9]{4}-?[1-9]{4}$",str(new_cc))
### check for alphabet characters
nomatch=re.search(r"[a-zA-z]",str(new_cc))
##check for repetative numbers
con=re.search(r"(\d)\1{3,}",str(without_hyp))

if nomatch == None:
    if match != None:
        if len(new_cc.replace("-","")) == 16:
            # if match.group(0):
            #     print(match.group(0))
            if con == None:
                print('Valid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
else:
    print('Invalid')
print("valid" if True)