#一些优化，以及实现了显示计算的方法
from fractions import Fraction
try:
    user_input = input("Input 4 numbers range from 1 to 13, split by space：\n")#优化表达，更美观
    numbers = [int(num) for num in user_input.split()]
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    if len(numbers)==4:
        #设定区域
        flag=False
        #函数区域
        def generate_combinations(numbers):
            combinations=[]
            remainings=[]
            for i in range(len(numbers)):
                for j in range(i+1, len(numbers)):
                    combinations.append([numbers[i], numbers[j]])
                    remainings.append([number for index, number in enumerate(numbers) if index != i and index != j])
            return combinations,remainings

        def ASMD(number1, number2):
            generated_number_bank = []
            generated_number_bank.append((number1, "+", number2, int(number1 + number2)))
            generated_number_bank.append((number1, "-", number2, int(number1 - number2)))
            generated_number_bank.append((number2, "-", number1, int(number2 - number1)))
            generated_number_bank.append((number1, "*", number2, int(number1 * number2)))
            if number2 != 0:
                generated_number_bank.append((number1, "/", number2, Fraction(number1 , number2)))#优化：使得结果是整数就保留整数，结果是小数就保留分数形式
            if number1 != 0:
                generated_number_bank.append((number2, "/", number1, Fraction(number2 , number1)))
            return generated_number_bank

        #主程序区域
        combinations,remainings=generate_combinations(numbers)
        for i in range(6):
            combination=combinations[i]
            remaining=remainings[i]
            number1=combination[0]
            number2=combination[1]
            number3=remaining[0]
            number4=remaining[1]
            generated_number_bank=ASMD(number1,number2)
            for generated_number in generated_number_bank:
                second_combinations,second_remainings=generate_combinations([generated_number[3],number3,number4])#generated_number[3]是计算结果的位置
                for i in range(3):
                    second_combination=second_combinations[i]
                    second_remaining=second_remainings[i]
                    second_number1=second_combination[0]
                    second_number2=second_combination[1]
                    second_number3=second_remaining[0]
                    second_generated_number_bank=ASMD(second_number1,second_number2)
                    for second_generated_number in second_generated_number_bank:
                        results=ASMD(second_generated_number[3],second_number3)
                        for result in results:
                            if result[3]==24:
                                print(f'{generated_number[0]}{generated_number[1]}{generated_number[2]}={generated_number[3]}')#逐步输出过程
                                print(f'{second_generated_number[0]}{second_generated_number[1]}{second_generated_number[2]}={second_generated_number[3]}')
                                print(f'{result[0]}{result[1]}{result[2]}={result[3]}\n')
                                
                                flag=True
        if not flag:
            print("This puzzle can't be solved!")
    else:
        print("Please enter 4 numbers split by space!")


#缺点是：如果输入的数字中有相同的数字，会产生多次相同的输出






