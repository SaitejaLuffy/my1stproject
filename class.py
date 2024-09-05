class student:

    def __init__(self,name,rollno):
      self.name=name
      self.rollno=rollno
      self.lap=self.Laptop

    def show(self):
       print(self.name,self.rollno)
       self.lap.show()

    class Laptop:
       def __init__(self,):
          self.brand='HP'
          self.RAM="8GB"
          self.Processor='I5'
       def show(self):
          print(self.brand,self.RAM,self.Processor)
c1=student('Saiteja','004')
c2=student('sandy','003')
print(c1.show())
