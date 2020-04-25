def todo_liste():
    test = open("todo.txt").readlines()
    for line in test:
        print(line.rstrip())


def sql_error():
    sql = open("sql-error.txt").readlines()
    for line in sql:
        print(line.rstrip())


def lizenz():
    pass


def help_txt():
    pass
