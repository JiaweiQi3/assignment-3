import sqlite3

with sqlite3.connect('concrete.db') as conn:
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. SHOW ALL TESTS
    print("ALL TESTS")
    cursor.execute('''
        SELECT project_name, actual_strength, passed
        FROM concrete_tests
        ORDER BY test_id
    ''')
    for row in cursor.fetchall():
        result = "PASS" if row["passed"] == 1 else "FAIL"
        print(f"{row['project_name']}: {row['actual_strength']} PSI - {result}")
    print()

    # 2. Show ONLY failed tests
    print("FAILED TESTS")
    cursor.execute('''
        SELECT project_name, test_date, required_strength, actual_strength
        FROM concrete_tests
        WHERE passed = 0
        ORDER BY test_id
    ''')
    for row in cursor.fetchall():
        print(f"{row['project_name']} on {row['test_date']}")
        print(f"  Required: {row['required_strength']} PSI")
        print(f"  Actual: {row['actual_strength']} PSI")
        print()


    # 3. Count tests by project
    print("TESTS PER PROJECT")
    cursor.execute('''
        SELECT project_name, SUM(passed) AS passed_count, COUNT(*) AS total_count
        FROM concrete_tests
        GROUP BY project_name
        ORDER BY project_name
    ''')
    for row in cursor.fetchall():
        print(f"{row['project_name']}: {row['passed_count']}/{row['total_count']} passed")
