class HashTable:

    def __init__(self):
        # based on load factor we can change capacity size dynamically
        self.capacity = 10
        self.keys =[None]*self.capacity
        self.values = [None]*self.capacity

    def hash_function(self, key):
        hash_sum = 0 
        for letter in key:
            hash_sum = hash_sum + ord(letter)
        return hash_sum % self.capacity
    
    def insert(self,key, value):
        index = self.hash_function(key)
        # index may be occupied by other key in case of collision. find next available places.
        # if we find a index pos which is occupied by a key value same as incoming key , mean there is update for key,value pair
        while self.keys[index] is not None:
            if self.keys[index] == key: # means there is a update of value for the key
                self.values[index] = value
                return
            index = (index + 1 ) % self.capacity
        # when found a position
        self.keys[index] = key
        self.values[index] = value
    
    def get(self,key):
        #The Chain: If the key isn't at that starting index, it must be in one of
        #the immediately following slots because your insert function places it in the first None slot it finds moving forward.
        index = self.hash_function(key)
        print(f'looking for key = {key}, index calculated={index}')
        while self.keys[index] is not None:
            if self.keys[index] == key:
                print(f'value = {self.values[index]}')
                return self.values[index]
            index = (index+1)%self.capacity
        print('no value found for key')
        return None
    

    
        
    
if __name__ == '__main__':
    ht = HashTable()
    print(f'Hash table - {ht.hash_function('adam')}')

    ht.insert('adam','sandler')
    ht.insert('marco','polo')
    ht.insert('nissan','car')
    ht.insert('battle','ship')
    ht.insert('flash','thunder')

    ht.get('marco')
    ht.get('marco1')