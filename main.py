def umumiy_elementlar(royxat1, royxat2):
    set1 = set(royxat1)
    set2 = set(royxat2)
    umumiy = set1.intersection(set2)
    return list(umumiy)

royxat1 = [1, 2, 3, 4, 5]
royxat2 = [4, 5, 6, 7, 8]

print(umumiy_elementlar(royxat1, royxat2))
```

```python
def umumiy_elementlar(royxat1, royxat2):
    return list(set(royxat1) & set(royxat2))

royxat1 = [1, 2, 3, 4, 5]
royxat2 = [4, 5, 6, 7, 8]

print(umumiy_elementlar(royxat1, royxat2))
