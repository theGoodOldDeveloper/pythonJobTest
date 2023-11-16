def checked(myresult2,myresult3):
  tableNames = []
  maxLength = []

# create database tablename(s) list & longest name value
  for i in range(len(myresult2)):
      tableNames.append(myresult2[i][0])
      maxLength.append(len(myresult2[i][0]))
      tableMaxLength = max(maxLength)
  return tableNames, tableMaxLength