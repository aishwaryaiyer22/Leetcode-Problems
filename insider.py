output = []
transactions = [] #(date, type, amount, trader)
THRESHOLD = 5000000
datafeed = []
#def  findPotentialInsiderTraders(datafeed):
if not datafeed:
    return []
old_price = -1
new_date = -1
new_price = -1
for i in xrange(len(datafeed)):
    line = datafeed[i].split('|')
    if len(line) == 2:
        new_date = int(line[0])
        new_price = int(line[1])
        if old_price != -1:
            findInsider(new_date,new_price,old_price)   
    else:
        transactions.append((int(line[0]), line[2], int(line[3]), line[1]))
    old_price = new_price    
return output        
            
def findInsider(new_date,new_price,old_price):
for transaction in transactions:
    if new_price > old_price:
        if transaction[1] == "BUY" and new_date-transaction[0]< 3:
            if transaction[2] * (new_price-old_price) >= THRESHOLD:
                output.append(str(transaction[0]) + "|" + str(transaction[3]))
    else:
        if transaction[1] == "SELL" and new_date-transaction[0]< 3:
            if transaction[2] * (old_price - new_price) >= THRESHOLD:
                output.append(str(transaction[0]) + "|" + str(transaction[3]))