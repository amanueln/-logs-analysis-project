#!/usr/bin/env python

import psycopg2
from termcolor import colored

# Quetions
Quetion1 = colored("\nQuetion #1. What are the most popular three articles of"
                   " all time? \n", 'yellow')
Quetion2 = colored("\nQuetion #2. Who are the most popular article authors of"
                   " all time? \n", 'yellow')
Quetion3 = colored("\nQuetion #3. On which days did more than 1 percent of"
                   " requests lead to errors? \n", 'yellow')


def run_query(query):
        ''' connects to DB and executes query before closing DB. '''
        try:
            conn = psycopg2.connect(database="news",
                                    user="",
                                    password="",
                                    host="",
                                    port="")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows


# Question 1
def print_top_articles():
    try:
        query = """SELECT title, COUNT(log.path) AS click_count
           FROM log, articles
           WHERE log.path = '/article/' || articles.slug
           AND status='200 OK'
           GROUP BY title
           ORDER BY click_count DESC
           LIMIT 3;"""

        result = run_query(query)

        print(Quetion1)
        count = 1
        for i, row in enumerate(result, 1):
            print('#{} top article: "{}" with {} views.'
                  .format(i, row[0], row[1]))

    except (Exception, psycopg2.DatabaseError) as error:
        print("can't perform sql statement for Question 1 ")
        print(error)


# question 2
def print_top_article_authors():
    try:
        query = """
        SELECT
        authors.name, COUNT(log.path) as views FROM authors,log, articles
        WHERE log.path = '/article/' || articles.slug
        AND authors.id = articles.author
        AND log.status = '200 OK'
        GROUP BY authors.name
        ORDER BY views DESC
       """

        result = run_query(query)

        print(Quetion2)
        count = 1
        for i, row in enumerate(result, 1):
            print('#{} top Authors: "{}" with {} views.'
                  .format(i, row[0], row[1]))

    except (Exception, psycopg2.DatabaseError) as error:
        print("can't perform sql statement for Question 1 ")
        print(error)


# Question 3
def print_request_errors():
    try:
        query = """
        SELECT
           t1.days,100.0 * t1.f_counts/t2.s_counts AS request_errors_perc
           FROM
           (SELECT time::date AS days, COUNT(path)  AS f_counts
           FROM log WHERE status!='200 OK' GROUP BY days) t1
           INNER JOIN
           (SELECT time::date AS days, COUNT(path) AS s_counts
           FROM log GROUP BY days) t2
           ON t1.days = t2.days
           Where t1.f_counts > (t2.s_counts / 100)
       """

        result = run_query(query)

        print(Quetion3)
        for row in result:
                print("Answer : On " + str(row[0]) + " request lead"
                      " to errors was " + str(format(row[1], '.2f')) + "%")
    except (Exception, psycopg2.DatabaseError) as error:
        print("can't perform sql statement for Question 3 ")
        print(error)


if __name__ == '__main__':
    print_top_articles()
    print_top_article_authors()
    print_request_errors()
