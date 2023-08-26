class Realestate:
    def hoaDiff(self,x,y):
        return(x-y)

home = Realestate()


home.value = 1000000
home.location = "Chicago"
home.area = 1000
home.schoolrating = 5
home.hoa = 300
home.zip = "96066"

condo = Realestate()
condo.value = 1500000
condo.location = "Skokie"
condo.area = 1000
condo.schoolrating = 7
condo.hoa = 400
condo.zip = "96638"

print(home.location, condo.location)
print(home.area, condo.area)
print(home.schoolrating, condo.schoolrating)
print(home.hoa, condo.hoa, home.hoaDiff(home.hoa,condo.hoa))
print(home.zip, condo.zip)


