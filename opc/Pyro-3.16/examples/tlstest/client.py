import Pyro.core

uri=raw_input("paste uri:")
obj1=Pyro.core.getProxyForURI(uri)
obj1._setOneway("oneway")
obj2=Pyro.core.getProxyForURI(uri)
obj2._setOneway("oneway")
print "obj1.ping"
obj1.ping()
print "obj1.ping"
obj1.ping()
print "obj2.ping"
obj2.ping()
print "obj2.ping"
obj2.ping()
print "obj1.oneway"
obj1.oneway()
print "obj1.oneway"
obj1.oneway()
print "obj2.oneway"
obj1.oneway()
print "obj2.oneway"
obj1.oneway()
print "obj1.comcall"
print "usernames=",obj1.comcall()
print "obj2.comcall"
print "usernames=",obj2.comcall()
