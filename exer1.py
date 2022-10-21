
# zwróć łańcuch złożony z trzech środkowych znaków danego ciągu:
# Przypadek 1:\ str1 = "Datatypes"
# Oczekiwany wynik:\ aty
sampleStr="Datatypes"
middleIndex = int(len(sampleStr) / 2)
print("Oryginalny ciąg to:", sampleStr)
middleThree = sampleStr[middleIndex - 1:middleIndex + 2]
print("To są trzy środkowe znaki:", middleThree)