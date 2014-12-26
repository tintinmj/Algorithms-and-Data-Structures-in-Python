""" Author: Diljit Ramachandran
    Date : 4 December,2014
    Problem : Transform a given infix expression into postfix SPOJ ONP
    Language :Python
    License : GPL
    Modified Date : 4 December ,2014
"""

testcases = int(raw_input())
operator_priority= {'^':5,'/':4,'*':3,'-':2,'+':1}
for index in range(1,testcases+1):
    exprssn = raw_input()
    stack = []
    output = ""
    for x in exprssn:
        if (x=='('):
            stack.append(x);
        elif (x== ')'):
            while (stack[-1]!= '('):
                output=output+stack.pop()
            stack.pop()
        elif (operator_priority.has_key(x)):
            "if an operator is found do the following"
            while ((len(stack)>0) and (stack[-1] in operator_priority) and (operator_priority[stack[-1]] > operator_priority[x])):
                output =output +stack.pop(),
            stack.append(x)
        else:
            output=output+x
    while (stack):
        output=output+stack.pop()
    print output,

            

        