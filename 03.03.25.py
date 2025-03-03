class Circle:
    def __init__(self, r = 3.0):
       self.radius = r
       print(f'Ir ziveidots jauns aplis ar rad')
       
      def setRadius(self, r):
          self.radius  = r 
    
      def getRadius(self) -> float:
          return self.radius

      def getDiametr(self) -> float:
          retur self.radius * 2
          
      def getCircumference(self) -> float:
          retur 2* PI *self.radius
          
      def getArea(self) -> float:
          return PI*self.radius**2
      
        
      def __str__(self):
          return f'{self.Radius()} {self.getDiametr()} {self.getCircumference()} {self.getArea()}'
     
        
circle1 = Circle()
circle2 = Circle(1.5)
circle3 = Circle(12)
circle4 = Circle(5.54)








