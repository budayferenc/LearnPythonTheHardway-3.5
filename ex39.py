states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Fransisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print('OR State has: ', cities['OR'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        states, abbrev, cities[abbrev]))

print('-' * 10)
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas.")

city = cities.get("TX", 'Does Not Exist')
print("The city for the state 'TX' is %s" % city)

cn_province = {
    '广东': '粤',
    '湖南': '湘',
    '四川': '川',
    '云南': '滇',
    }

cn_cities = {
    '粤': '广州',
    '湘': '长沙',
    '川': '成都',
    }

cn_province['台湾'] = '台'

cn_cities['滇'] = '昆明'
cn_cities['台'] = '高雄'

print('-' * 10)
for prov, abbr in cn_province.items():
    print("%s省的缩写是%s" % (prov, abbr))

print('-' * 10)
cn_abbrevs = {values: keys for keys, values in cn_province.items()}
for abbrev, prov in cn_abbrevs.items():
    print("%s是%s省的缩写" % (abbrev, prov))

print('-' * 10)
for abbrev, city in cn_cities.items():
    print("%s市位于我国的%s省" % (city, cn_abbrevs[abbrev]))