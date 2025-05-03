def merge(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1
    
    output = num2[:]
    print(f"output: {output}\n")
    
    for n in num1:
        inserted = False
        for i in range(len(output)):
            if n <= output[i]:
                output.insert(i, n)
                inserted = True
                print(f"Inserted output: {output}")
                break
        if not inserted:
            output.append(n)
    return output

num1 = [1, 2, 3, 7]
num2 = [2, 3, 5, 6, 6]

print(f"\nMerge: {merge(num1, num2)}")
