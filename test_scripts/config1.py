from pyjavaproperties import Properties

pptobj=Properties()
pptobj.load(open('../config.properties'))
v=pptobj['city']
print(v)


