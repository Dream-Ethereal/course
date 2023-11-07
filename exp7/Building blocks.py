class Block:
    def __init__(self,inf):
        self.width=inf[0]
        self.length=inf[1]
        self.height=inf[2]
    def get_width(self):
        return self.width
    def get_length(self):
        return self.length
    def get_height(self):
        return self.height
    def get_volume(self):
        return self.width*self.height*self.length
    def get_surface_area(self):
        return 2*(self.width*self.height)+2*(self.width*self.length)+2*(self.height*self.length)