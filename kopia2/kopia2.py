# zaku[y


import copy

# nabial = ["mleko", "jajka", "ser"]
# chemia = ["domestos", "plyn do naczyn"]
#
# zakupy_styczen = [nabial, chemia]
# print( zakupy_styczen)
#
# zakupy_luty = zakupy_styczen.copy()
# print(zakupy_luty)
#
# zakupy_styczen[1].append("gabka do naczyn")
# print(zakupy_styczen)
# print(zakupy_luty)


nabial = ["mleko", "jajka", "ser"]
chemia = ["domestos", "plyn do naczyn"]

zakupy_styczen = [nabial, chemia]
print( zakupy_styczen)


zakupy_luty = copy.deepcopy(zakupy_styczen)
print(zakupy_luty)

zakupy_styczen.append("gabka")
print(zakupy_styczen)
print(zakupy_luty)


