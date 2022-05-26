# for loop to iterate through each line in csv file
for row in csv_reader:
    # if condition to ignore the first line of csv file
    if line != 0:
        # if condition to find the lowest salry
        if float(row[2]) < lowest_salary:
            lowest_salary = float(row[2])
            # storing the name of the person with lowest salary
            first_name = row[0]
            last_name = row[1]

        # if condition to find average saalry of the managers
        if row[3] == 'Manager':
            # calculaing the total salary
            total_salary += float(row[2])
            # calculating the total managers
            count += 1
    line += 1
