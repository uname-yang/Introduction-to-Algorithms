#BitArray
#Yu.Yang
#
class bitarray():
    def __init__(self,length,defaultValue=False):
        if (length < 0):
            raise Exception("Length param error")
        self.array=[]
        self.length=length
        fillValue=defaultValue
        for  i in range(self.length):
            self.array.append(defaultValue)
        self.version=0

    def input_from_array(self,value):
        if(isinstance(value,list)==False):
            raise Exception("value is not a Array")
        if (value is None or len(value)!=self.length):
            raise Exception("ArgumentException if value == null or value.Length != this.Length.")
        for i in range(self.length):
            self.Set(i,value[i])
        self.version+=1
        return self

    def __len__(self):
        return self.length

    def __str__(self):
        str="["
        for i in range(self.length):
            str+="1" if self.array[i]==True else "0"
            str+=" "
        str+="]"
        return str

    def Get (self,index):
        if (index < 0 or index >=self.length):
            raise Exception("ArgumentOutOfRangeException if index < 0 or index >= GetLength()")
        return self.array[index]

    def Set (self,index,value):
        if (index < 0 or index >=self.length):
            raise Exception("ArgumentOutOfRangeException if index < 0 or index >= GetLength()")
        if (value):
            self.array[index]=True
        else:
            self.array[index]=False
        self.version+=1

    def SetAll(self,value):
        for  i in range(self.length):
            self.Set(i,value)
        self.version+=1

    def And (self,value):
        if(isinstance(value,BitArray)==False):
            raise Exception("value is not a BitArray")
        if (value is None or len(value)!=self.length):
            raise Exception("ArgumentException if value == null or value.Length != this.Length.")
        for i in range(self.length):
            self.array[i]&=value.Get(i)
        self.version+=1
        return self

    def Or (self,value):
        if(isinstance(value,BitArray)==False):
            raise Exception("value is not a BitArray")
        if (value is None or len(value)!=self.length):
            raise Exception("ArgumentException if value == null or value.Length != this.Length.")
        for i in range(self.length):
            self.array[i]|=value.Get(i)
        self.version+=1
        return self

    def Xor (self,value):
        if(isinstance(value,BitArray)==False):
            raise Exception("value is not a BitArray")
        if (value is None or len(value)!=self.length):
            raise Exception("ArgumentException if value == null or value.Length != this.Length.")
        for i in range(self.length):
            self.array[i]^=value.Get(i)
        self.version+=1
        return self

    def Not (self):
        for i in range(self.length):
            self.array[i] =not self.array[i]
        self.version+=1
        return self
