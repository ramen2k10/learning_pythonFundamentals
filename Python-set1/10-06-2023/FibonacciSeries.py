# Fibonacci series using a range not in array
#
class Find_FibonacciSeries:
    def get_FibonacciSeries(self, range):
        num1 = 0
        num2 = 1
        sum = 0
        print("Invalid Range")
        if range<1:
            print("Invalid Range")
            return
        print("Fibonacci series: ", num1)
        print("Fibonacci series: ", num2)
        while(num1 < range):
            sum = num1 + num2
            num1 = num2
            num2 = sum
            print("Fibonacci series: ", sum)


try:
    uInput = input("Enter a number:")
    range = int(uInput)
except:
    print("Invalid input")
obj = Find_FibonacciSeries()
obj.get_FibonacciSeries(range)

# Fibonacci series using a range in array
#
class Get_FibonacciSeries_Array:

    def get_FiboSeriesArray(self, range):
        series = [0, 1]
        while len(series) < range:
            sum = series[-1] + series[-2]
            series.append(sum)
        return series

obj1 = Get_FibonacciSeries_Array()
fib_series = obj1.get_FiboSeriesArray(10)
print(fib_series)
