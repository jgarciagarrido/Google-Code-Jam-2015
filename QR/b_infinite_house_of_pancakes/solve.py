import sys


def format_output_line(output, number):
    return "Case #%d: %s" % (number, output)


def create_output_file(name, results):
    f = open(name+".out", 'w')
    for i in range(len(results)):
        f.write("Case #%d: %s\n" % (i+1, results[i]))
    return f


def open_input_file_name(name):
    f = open(name+".in.txt")
    return f


def get_number_of_cases(input_file):
    line = input_file.readline()
    return int(line)


def get_diners(input_file):
    line = input_file.readline()
    return int(line)


def get_cases(name):
    input_file = open_input_file_name(name)
    N = get_number_of_cases(input_file)
    cases = []
    for i in xrange(N):
        get_diners(input_file)
        line = input_file.readline()
        tokens = line.split()
        cases.append(map(lambda x: int(x), tokens))
    input_file.close()
    return cases


def breakfast_end(plates):
    return len(plates) == 0


def estimated_finish(plates):
    if breakfast_end(plates):
        return 0
    else:
        return max(plates)


def clean_plates(plates):
    return filter(lambda x: x > 0, plates)


def special_minute(plates):
    max_pancakes = max(plates)
    max_plate = plates.index(max_pancakes)
    plates_especial = plates + [max_pancakes / 2, ]
    plates_especial[max_plate] = max_pancakes - (max_pancakes / 2)
    return clean_plates(plates_especial)


def minutes_to_finish_breakfast(plates):
    minutes = 0
    min_minutes = estimated_finish(plates)
    for minutes in xrange(min_minutes):
        plates = special_minute(plates)
        minutes += 1
        estimated_minutes = minutes + estimated_finish(plates)
        if estimated_minutes < min_minutes:
            min_minutes = estimated_minutes
    return min_minutes


def solve_infinite_house_of_pancakes_rigodon(name):
    cases = get_cases(name)
    results = []
    i = 1
    for case in cases:
        results.append(minutes_to_finish_breakfast(case))
        i += 1
    create_output_file(name, results)

if __name__ == "__main__":
    solve_infinite_house_of_pancakes_rigodon(sys.argv[1])
