#indexing= accesing elemets of a sequence using [] (indexing operaotr)
#[start:end:step]
credit_number="1234-2332-424242"
last_digits=credit_number[-4:]
print(credit_number[2])
print(credit_number[0:4])
print((credit_number[5:9]))
print(credit_number[5:])
print(credit_number[-3])
print(credit_number[::3])
print(f"xxxxx-xxxxx-xxxx-{last_digits}")
credit_number=credit_number[::-1] #it reverses the string
print(credit_number)