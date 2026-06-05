def getRow(rowIndex):
        row = [1]
        current_val = 1
        for i in range(1, rowIndex + 1):
            current_val = current_val * (rowIndex - i + 1) // i
            row.append(current_val)
        return row

print(getRow(3))
print(getRow(5))
        