import pandas as pd

# #series
dominos = ['Chicken Pizza','Mutton Pizza','Aligator Pizza','Watermelon Pizza']
domi_pizza = pd.Series(dominos)
# print(domi_pizza)

# #dataframe
domi_pizza = pd.DataFrame(dominos)
# print(domi_pizza)


age = [12,23,34,45]
ages = pd.Series(age)
# print(ages)

boolean = [True,False,True,True,False]
booleans = pd.Series(boolean)
# print(booleans)

# dicti = {'Name':'Madhavan','Age':20,'Organisation':'Saama Technology'}
# dic_series = pd.Series(dicti)
# dic_series


weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
fruits = ['Apples','Grapes','Mangos','Lemons','Oranges']
pd.Series(weekdays,fruits)
week_data = pd.Series(index = weekdays ,data = fruits)
print(week_data)
# print("Index value    : ",week_data.index)

pokemons = pd.read_csv('C:/Users/madhavan.bala/pokemon.csv')
# print(pokemons.head())


#choose columns
poke_type = pd.read_csv('C:/Users/madhavan.bala/pokemon.csv',usecols = ["Name","Type 1","Type 2"])
# print(poke_type.head())


# print(poke_type.head(2))           #head()
# print("\n",poke_type.tail(2))      #tail()
# print("\n",type(poke_type))        #type()
# print("\n",sorted(pokemons))       #sorted
# print("\n Values",pokemons.values)        #values
# print("\n dimesional array",pokemons.ndim )         #dimensional array
# print("\n",pokemons.size)          #size
# print("\n",pokemons.shape)         #shqpe
# print("Index  : ",pokemons.index)              #index
# print("Data list:   ",list(poke_type.values))



maximum_power = pokemons.Attack
# print(max(maximum_power))
# print(maximum_power.is_unique)


#to assign a value in order (Sorting)
alphabet_assigh = pokemons.sort_values("Name").head()
# print(alphabet_assigh)

asc_order = pokemons.sort_values("Attack",ascending = True).head()
# print(asc_order)


pokemons.sort_values('Speed',ascending = False).head()
# # print(pokemons.head())


pokemons.sort_values('Name',ascending = True)     #to reset value/data the table
# print(pokemons.head())

#to check indexe's and value in boolean
# print(pokemons.all())      


pokemons.all(axis = 'columns')
# print(pokemons.head(5))

no_name = pokemons.drop("Name" , axis = 1)
# print(len(pokemons.Name))
# print(len(no_name))



import pandas as pd
a = {'Madhavan',20,'Kri',19}
b = pd.DataFrame(a)
# print(b)

pokemons[27:90]

#to search(show) a particular value in a column by using loc
#filter type
# print(pokemons.loc[pokemons['Name'] == 'Pikachu'])

#to search by number 
# print(pokemons.iloc[30]) 

#filter mehod
# get values by using index names and it can also assigned into variables
print(pokemons.loc[pokemons['Generation'] == 1])
pow = pokemons.iloc[[101,103]]
# print(pow)


print(pokemons.loc[pokemons['Name']=='Gengar'])

print(pokemons.get['Gengar'])

# print(pokemons.head(4))


names_assign =pokemons.Name
# print(names_assign[0])



print(pokemons.loc[pokemons['Name'] == 'Gengar'])
# print(pokemons.loc[3])

# to rename a value
re_value = pokemons.Name
re_value[0] = "Alter_value"   # 0 is used to change the value by using index method
# print(pokemons.Name)

# print(pokemons.sort_index)

pokemons.dropna()

#Index replace
pokemons.reset_index(inplace = True)

#reset all the data's
pokemons.reset_data(inplace = True)


# # ### Math methods on Series Objecets

without_null = pokemons.dropna()
# print(len(without_null))


attack = pd.read_csv('pokemon.csv',usecols = ['Attack'])
defence = pd.read_csv('pokemon.csv',usecols = ['Defense'])


# print(attack.sum())
# print(attack.mean())
# print(attack.product())
# print(attack.std())
# print(attack.min())
# print(attack.max())
# print(attack.mode())
# print(attack.describe())


attack.add(20)


#  Value_counts_method
# The value_counts() method returns a Series containing the counts of unique values.
print("Value's Count : ",pokemons.value_counts())

pokemons.value_counts(normalize = True)

a = mapping ={
    "Grass":"Mass",
    "Ghost":"Super"
    }
gr = pokemons.loc[pokemons['Type 1'] == 'Grass']
print(len(gr))
ni = pokemons.loc[pokemons['Type 1'] == 'Mass']
# print(len(ni))

# print(a)


employee = pd.read_csv('Employee.csv')
employee.info() #to find null values are there or not
employee["Series_reference"].head(3)
#status = employee["STATUS"].head(3)

# Select one column for dataframe

employee[["Series_reference","STATUS"]].head(3)

req = ["Series_reference","Subject","Series_title_3"]
# employee[req].head(3)                                     #a;; must be in saquare brackets


# Add New column into dataframe

employee["Type"] = "Car"
employee.head(4)


employee.insert(1,column = "Color",value = "Red")
employee.head(3)


employee.insert(2,column = "number",value = 1)
employee.head(3)

# Broadcasting Operations

employee["number"].add(100)

employee["number"].mul(178) # * 178 [ - , * , + % ]

employee["New_value"] = employee["number"].add(12)

# employee.head(4)


# A Review of the.value_counts() Method

employee["Series_reference"].value_counts().head(4)

# Drop rows null values

employee.dropna(how = 'all').head(2) # how = 'all' ethukuna null value rows la irunthalum mitha row la values iruku atha

# Drop column null values

employee.dropna(axis = 1).head(3) # here axis use dto remove column null value / use axis = 'columns'


### * dropna() is used to remove null value in rows
### * (axis = 1) / (axis = "columns") is used to remove the null values in column

employee.dropna(subset = ['Suppressed']).head(2)


# .astype() Method    / add values in table
# employee.tail(3)

employee["Suppressed"].fillna(89,inplace = True)

employee["number"] = employee["number"].astype("float") # astype is used to change the type

employee["number"]


employee.sort_index().head(3)


# .rank() method
employee.dropna(how = "all").head(4)
employee["Suppressed"] = employee["Suppressed"].fillna(5)
employee["Rank_based_on_period"] = employee["Period"].rank()
employee.Rank_based_on_period.astype("int")
employee.sort_values(by = "Rank_based_on_period").head(3)

