print(float(2344-234))
age=14
is_teen=age>12 and age<20
print(is_teen)
is_teen=age>12 or age<20
print(is_teen)

#compare 2 cities' dencity

london_population, london_area = 234567899,66000000

liverpool_population, liverpool_area = 90987654,3000000

london_density=london_population/london_area
liverpool_density=liverpool_population/liverpool_area

print(f"london_density is higher than liverpool_density: {london_density < liverpool_density}")
