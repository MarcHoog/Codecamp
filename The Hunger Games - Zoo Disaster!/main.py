Menu = {"antelope": {"grass"},
          "big-fish": {"little-fish"},
          "bug":      {"leaves"},
          "bear":     {"big-fish", "bug", "chicken", "cow", "leaves", "sheep"},
          "chicken":  {"bug"},
          "cow":      {"grass"},
          "fox":      {"chicken", "sheep"},
          "giraffe":  {"leaves"},
          "lion":     {"antelope", "cow"},
          "panda":    {"leaves"},
          "sheep":    {"grass"}}


def who_eats_who(zoo):
    
    answer, zoo_list, n = [zoo], zoo.split(","), 0
    
    while n < len(zoo_list):
        while n > 0 and zoo_list[n-1] in Menu.get(zoo_list[n], set()):
            answer.append(f"{zoo_list[n]} eats {zoo_list.pop(n-1)}")
            n -= 2
        
        while n >= 0 and n != len(zoo_list)-1 and zoo_list[n+1] in Menu.get(zoo_list[n], set()):
            answer.append(f"{zoo_list[n]} eats {zoo_list.pop(n+1)}")
        
        n += 1     # Nothing to eat, step forward
        
    return answer + [','.join(zoo_list)]

who_eats_who("fox,bug,chicken,grass,sheep")