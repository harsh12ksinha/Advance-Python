import mysql.connector


conn = mysql.connector.connect(
    user="root",
    password="pass1234",
    host="localhost",
    port= 3306

)

if conn.is_connected():
    print(conn.is_connected())


if conn.is_connected():
    print("connected")

cur = conn.cursor()
cur.execute("SHOW DATABASES")
for x in cur:
    print(x)

cur.execute("USE giet")

cur.execute("SELECT * FROM giet")
for row in cur:
    print(row)

# 1. Show all data
print("1. All Data:")
cur.execute("SELECT * FROM giet")
for row in cur.fetchall():
    print(row)

# 2. Name column
print("\n2. Names:")
cur.execute("SELECT name FROM giet")
for row in cur.fetchall():
    print(row)

# 3. Name and address
print("\n3. Name and Address:")
cur.execute("SELECT name, address FROM giet")
for row in cur.fetchall():
    print(row)

# 4. Roll and salary
print("\n4. Roll and Salary:")
cur.execute("SELECT roll, salary FROM giet")
for row in cur.fetchall():
    print(row)

# 5. Name = 'aman'
print("\n5. Name = aman:")
cur.execute("SELECT * FROM giet WHERE name='aman'")
for row in cur.fetchall():
    print(row)

# 6. Address = delhi
print("\n6. Lives in Delhi:")
cur.execute("SELECT * FROM giet WHERE address='delhi'")
for row in cur.fetchall():
    print(row)

# 7. Gender = M
print("\n7. Gender M:")
cur.execute("SELECT * FROM giet WHERE gender='M'")
for row in cur.fetchall():
    print(row)

# 8. Designation = doctor
print("\n8. Doctors:")
cur.execute("SELECT * FROM giet WHERE desig='doctor'")
for row in cur.fetchall():
    print(row)

# 9. Salary = 15000
print("\n9. Salary = 15000:")
cur.execute("SELECT * FROM giet WHERE salary=15000")
for row in cur.fetchall():
    print(row)

# 10. Salary > 20000
print("\n10. Salary > 20000:")
cur.execute("SELECT * FROM giet WHERE salary > 20000")
for row in cur.fetchall():
    print(row)

# 11. Salary < 30000
print("\n11. Salary < 30000:")
cur.execute("SELECT * FROM giet WHERE salary < 30000")
for row in cur.fetchall():
    print(row)

# 12. Male AND salary > 20000
print("\n12. Male & Salary > 20000:")
cur.execute("SELECT * FROM giet WHERE gender='M' AND salary > 20000")
for row in cur.fetchall():
    print(row)

# 13. Female OR address = raipur
print("\n13. Female OR Raipur:")
cur.execute("SELECT * FROM giet WHERE gender='F' OR address='raipur'")
for row in cur.fetchall():
    print(row)

# 14. Name starts with 'a'
print("\n14. Name starts with 'a':")
cur.execute("SELECT * FROM giet WHERE name LIKE 'a%'")
for row in cur.fetchall():
    print(row)

# 15. Name ends with 'h'
print("\n15. Name ends with 'h':")
cur.execute("SELECT * FROM giet WHERE name LIKE '%h'")
for row in cur.fetchall():
    print(row)

# 16. Address contains 'pur'
print("\n16. Address contains 'pur':")
cur.execute("SELECT * FROM giet WHERE address LIKE '%pur%'")
for row in cur.fetchall():
    print(row)

# 17. Sort by name ASC
print("\n17. Sorted by Name ASC:")
cur.execute("SELECT * FROM giet ORDER BY name ASC")
for row in cur.fetchall():
    print(row)

# 18. Sort by salary DESC
print("\n18. Sorted by Salary DESC:")
cur.execute("SELECT * FROM giet ORDER BY salary DESC")
for row in cur.fetchall():
    print(row)

# 19. Count total employees
print("\n19. Total Employees:")
cur.execute("SELECT COUNT(*) FROM giet")
print(cur.fetchone())

# 20. Count gender M
print("\n20. Total Male Employees:")
cur.execute("SELECT COUNT(*) FROM giet WHERE gender='M'")
print(cur.fetchone())

# Close connection
conn.close()
