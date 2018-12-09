from suds.client import Client

service = Client("http://115.28.108.130:4000/?wsdl").service
r = service.addUser("猪猪1","123456")
print(r)
r2 = service.checkUser("猪猪","123456")
print(r2)
r3 = service.getAll
print(r3)

r4 = service.getUserById("猪猪")
print(r4)