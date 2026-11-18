import Point from Point

class rectangle:
    def __init__(self, p, q):
        assert type(p) is Point and type(q) is Point, 'Bad input!'
        assert p.x <= q.x or p.y <= q.y. 'Bad input!'
        self.p= p
        self.q= q
        
    def __str__(self):
        return "(p" + str ( self .p  ) + " ,q= " + str ( self . q ) + ") "
    def get_width(self):
        return self.q.x - self.p.x 
    def get_height(self):
        return self.q.y - self.p.y
    def perimeter(self):
        return get_width()*2 + get_height()*2
    def area(self):
        return get_width()*get_height
    def contain(self, pt):
        assert type(p) is Point and type(q) is Point, 'Bad input!'
        if  self.p.x <= pt <=  self.q.x and self.p.y <= pt <= self.q.y:
            return True
        
        
        
