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


def get_cases(name):
    input_file = open_input_file_name(name)
    N = get_number_of_cases(input_file)
    cases = []
    for i in range(N):
        line = input_file.readline()
        tokens = line.split()
        cases.append(tokens[1])
    input_file.close()
    return cases


def invite_friends(audience_stats):
    people_clapping = 0
    friend_needed = 0
    for i in xrange(len(audience_stats)):
        people_to_add = 0
        if people_clapping < i:
            people_to_add = i - people_clapping
            friend_needed += people_to_add
        people_clapping += int(audience_stats[i]) + people_to_add
    return friend_needed


def solve_standing_ovation(name):
    cases = get_cases(name)
    results = []
    for case in cases:
        results.append(invite_friends(case))
    create_output_file(name, results)

if __name__ == "__main__":
    solve_standing_ovation(sys.argv[1])
