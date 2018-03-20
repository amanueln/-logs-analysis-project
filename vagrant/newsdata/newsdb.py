# /usr/bin/python3

import psycopg2
from termcolor import colored

# Quetions
Quetion1 = colored("\nQuetion #1. What are the most popular three articles of"
                   " all time? \n", 'yellow')
Quetion2 = colored("\nQuetion #2. Who are the most popular article authors of"
                   " all time? \n", 'yellow')
Quetion3 = colored("\nQuetion #3. On which days did more than 1 percent of"
                   " requests lead to errors? \n", 'yellow')


# connects to DB and executes query before closing DB.
def run_query(query):
        try:
            conn = psycopg2.connect(database="news",
                                    user="",
                                    password="",
                                    host="",
                                    port="")

        except:
            print ("I am unable to connect to the database.")

        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows
        db.close()


# Question 1
def print_top_articles():
    try:
        query = """SELECT
       title,
       (SELECT COUNT(log.path) FROM log WHERE log.path
       LIKE '%'||articles.slug||'%'
       AND status='200 OK' ) AS click_count
       FROM articles ORDER BY click_count DESC LIMIT 3"""

        result = run_query(query)

        print (Quetion1)
        count = 1
        for row in result:
            print("#%s top article: " + row[0] +
                  " with " + str(row[1]) + "views.") % count
            count += 1
    except:
        print ("can't perform sql statement for Question 1 ")


# question 2
def print_top_article_authors():
    try:
        query = """
        SELECT
        authors.name, COUNT(log.path) as views FROM authors,log, articles
        WHERE log.path LIKE '%'||articles.slug||'%'
        AND authors.id = articles.author
        AND log.status = '200 OK'
        GROUP BY authors.name
        ORDER BY views DESC
       """

        result = run_query(query)

        print (Quetion2)
        count = 1
        for row in result:
            print ("#%s top Authors: " + row[0] + " with " +
                   str(row[1]) + " views.") % count
            count += 1

    except:
        print ("can't perform sql statement for question 2")


# Question 3
def print_request_errors():
    try:
        query = """
        SELECT
           t1.days,
           t1.f_counts,
           t2.s_counts,
           100.0 * t1.f_counts/t2.s_counts AS request_errors_perc
           FROM
           (SELECT to_char(time, 'YYYY-MM-DD') AS days, COUNT(path) AS f_counts
           FROM log WHERE status!='200 OK' GROUP BY days) t1
           INNER JOIN
           (SELECT to_char(time, 'YYYY-MM-DD') AS days, COUNT(path) AS s_counts
           FROM log GROUP BY days) t2
           ON t1.days = t2.days
       """

        result = run_query(query)

        print (Quetion3)
        for row in result:
            if int(row[3]) > 1:
                print("Answer : On " + row[0] + " request lead"
                      " to errors was " + str(format(row[3], '.2f')) + "%")

    except:
        print("can't perform sql statement for question 3")


if __name__ == '__main__':
    print_top_articles()
    print_top_article_authors()
    print_request_errors()
