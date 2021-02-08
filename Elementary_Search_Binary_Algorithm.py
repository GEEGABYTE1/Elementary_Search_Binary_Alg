class search_binary:
    def __init__(self, lst, x):
        self.lst = lst
        self.x = x 

    def sorting(self):
        base_length = len(self.lst)
        base_list = []

        for i in self.lst:
            base_list.append(i)


        for i in range(len(self.lst)):
            
            if self.x == self.lst[int(len(self.lst) / 2)]:
                if len(self.lst) == base_length:
                    print(self.lst[int(len(self.lst) / 2)])
                    print("Element at " + str(int(len(self.lst) / 2)))
                
                else:
                    string = ""
                    for j in range(len(base_list)):
                        if self.x == base_list[j]:
                            string += str(j)
                    print(self.lst[int(len(self.lst) / 2)])
                    print("Element at " + string)
                    
                break 

            elif self.x > self.lst[int(len(self.lst) / 2)]:
                new_lst = self.lst[int(len(self.lst) / 2): ]

                string = ""

                for j in range(len(self.lst)):
                    if self.x == self.lst[j]:
                        string += str(j)

                self.lst = new_lst 

                if not self.x in self.lst:
                    break
                

                if len(self.lst) == 1:
                    print(str(self.lst) + "was at " + string)
            
            elif self.x < self.lst[int(len(self.lst) / 2)]:
                if len(self.lst) == 2:
                    string = ""
                    for j in range(len(base_list)):
                        if self.x == base_list[j]:
                            string += str(j)
                    print(self.lst[0])
                    print("Element at " + string)
                    break
                    
                
                new_lst = self.lst[ :int(len(self.lst)/ 2) + 1]
                self.lst = new_lst

                string = ""

                for j in range(len(self.lst)):
                    if self.x == self.lst[j]:
                        string += str(j)

                if not self.x in self.lst:
                    break

                if len(self.lst) == 1:
                    print(str(self.lst) + "was at " + string)



