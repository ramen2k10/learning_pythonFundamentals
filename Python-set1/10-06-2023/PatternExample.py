# Print the pattern
#*
#**
#***

size = 5

# Loop for rows
for i in range(size):
    # Loop for columns
    for j in range(i):
        print("*", end=" ")
    print()
