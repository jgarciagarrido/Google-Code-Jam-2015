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


def get_parameters(input_file):
    line = input_file.readline()
    tokens = line.split()
    return map(lambda x: int(x), tokens)


def get_cases(name):
    input_file = open_input_file_name(name)
    N = get_number_of_cases(input_file)
    cases = []
    for i in xrange(N):
        L, X = get_parameters(input_file)
        line = input_file.readline()
        cases.append(line[:L]*X)
    input_file.close()
    return cases


quaternion_mult = {
    '1':  {'1':  '1', 'i':  'i', 'j':  'j', 'k':  'k', '-1': '-1', '-i': '-i', '-j': '-j', '-k': '-k'},
    '-1': {'1': '-1', 'i': '-i', 'j': '-j', 'k': '-k', '-1':  '1', '-i':  'i', '-j':  'j', '-k':  'k'},

    'i':  {'1':  'i', 'i': '-1', 'j':  'k', 'k': '-j', '-1': '-i', '-i':  '1', '-j': '-k', '-k':  'j'},
    '-i': {'1': '-i', 'i':  '1', 'j': '-k', 'k':  'j', '-1':  'i', '-i': '-1', '-j':  'k', '-k': '-j'},

    'j':  {'1':  'j', 'i': '-k', 'j': '-1', 'k':  'i', '-1': '-j', '-i':  'k', '-j':  '1', '-k': '-i'},
    '-j': {'1': '-j', 'i':  'k', 'j':  '1', 'k': '-i', '-1':  'j', '-i': '-k', '-j': '-1', '-k':  'i'},

    'k':  {'1':  'k', 'i':  'j', 'j': '-i', 'k': '-1', '-1': '-k', '-i': '-j', '-j':  'i', '-k':  '1'},
    '-k': {'1': '-k', 'i': '-j', 'j':  'i', 'k':  '1', '-1':  'k', '-i':  'j', '-j': '-i', '-k': '-1'},

}

def find_goal(goal, word):
    base = '1'
    index = 0
    for letter in word:
        base = quaternion_mult[base][letter]
        if base == goal:
            return (True, word[index+1:])
        index += 1
    return (False, "")

def find_goal_i(word):
    base = '1'
    index = 0
    goal = 'i'
    for letter in word:
        base = quaternion_mult[base][letter]
        if base == goal:
            return (True, word[index+1:])
        index += 1
    return (False, "")


def find_goal_k(word):
    base = '1'
    index = 0
    goal = 'k'
    for letter in word[::-1]:
        base = quaternion_mult[letter][base]
        #print base
        if base == goal:
            return (True, word[:-index+1])
        index += 1
    return (False, "")


def find_goal_j(word):
    base = '1'
    goal = 'j'
    for letter in word:
        base = quaternion_mult[base][letter]
    return (base == goal, "")


def is_ijk_equivalent_a(word):
    i, word = find_goal_i(word)
    print i, word
    k, word = find_goal_k(word)
    print k, word
    j, word = find_goal_j(word)
    print j, word
    return i and j and k


def is_ijk_equivalent_b(word):
    i, word = find_goal('i', word)
    print i, word
    j, word = find_goal('j', word)
    print j, word
    k, word = find_goal('k', word)
    print k, word
    return i and j and k and word == ""


def solve_dijkstra(name):
    cases = get_cases(name)
    results = []
    for case in cases:
        if is_ijk_equivalent_a(case) or is_ijk_equivalent_b(case):
            result = 'YES'
        else:
            result = 'NO'
        results.append(result)
    create_output_file(name, results)

if __name__ == "__main__":
    #print is_ijk_equivalent_b('ji'*6)
    solve_dijkstra(sys.argv[1])
