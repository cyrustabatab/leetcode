


def daily_temperatures(temperatures):


    
    answers = [0] * len(temperatures)
    
    stack = []
    for i,temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            answers[stack[-1]] = i - stack[-1]
            stack.pop()

        stack.append(i)



    return answers



if __name__ == "__main__":


    temperatures = [73,74,75,71,69,72,76,73]

    print(daily_temperatures(temperatures))



