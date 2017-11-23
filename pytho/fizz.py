def fizzbuzz():
    conditions = {2: "Test",
                  3: "Fizz",
                  5: "Buzz",
                  7: "Sizzle"
                  }

    for i in range(1, 101):
        output = ""
        for k, v in conditions.items():
            if i % k == 0:
                output += v
        if output == "":
            print(i)
        else:
            print(output)
