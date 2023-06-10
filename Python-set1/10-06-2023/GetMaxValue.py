class Get_MaxValue:
    def get_MaxValue(self, numbers):
        maxNum = 0
        for num in numbers:
            if num < 0:
                print("Invalid number")
            if num > maxNum:
                maxNum = num
        return maxNum

ma_instance = Get_MaxValue()
numbers = [1, 2, 5, 7, 12]
print("The max number is :", ma_instance.get_MaxValue(numbers))
