# -*- coding: utf-8 -*-
"""
Created on Mon May  2 23:30:31 2022

@author: vicgu
"""
from flask import Flask, request, jsonify
import sqlalchemy as sqla
import pandas as pd
import datetime as datetime

app = Flask(__name__)


@app.route("/pages", methods=["POST", "GET", "DELETE"])
def page():

    try:

        engine = sqla.create_engine("sqlite:///Brut.db")
        connect = engine.connect()

    except Exception as e:

        raise Exception("Can't connect to the base, error: " + e)

    if request.method == "GET":

        page = pd.read_sql("""
                            SELECT *
                            FROM Pages
                            """, connect)

        return jsonify(page.to_dict(orient="index"))

    if request.method == "POST":

        max_id = connect.execute("""
                                 SELECT
                                 COALESCE(MAX(id), 0)
                                 FROM PAGES
                                 """).fetchall()
        print(max_id[0][0])
        new_name = request.form["name"]
        new_date = datetime.datetime.today()
        new_id = max_id[0][0] + 1
        print("to _send")

        try:

            connect.execute("""
                            INSERT INTO pages (id, name, create_at)
                            VALUES (?, ?, ?)
                            """, (new_id, new_name, new_date))
        except:

            raise Exception("Can't insert into the base page")

        return "Page create succesfully", 201

    if request.method == "DELETE":

        name_delete = request.form["name"]
        try:

            connect.execute(f"""
                            DELETE From pages
                            WHERE
                            name = '{name_delete}'
                            """)
        except:

            raise Exception(
                f"Can't Delete the row with the name {name_delete}")

        return "Page Deletes", 201

    connect.detach()
    connect.close()
    connect.closed()


@app.route("/videos", methods=["POST", "GET", "DELETE"])
def videos():

    try:

        engine = sqla.create_engine("sqlite:///Brut.db")
        connect = engine.connect()

    except Exception as e:

        raise Exception("Can't connect to the base, error: " + e)

    if request.method == "GET":

        page = pd.read_sql("""
                            SELECT *
                            FROM Videos
                            """, connect)

        return jsonify(page.to_dict(orient="index"))

    if request.method == "POST":

        max_id = connect.execute("""
                                 SELECT
                                 COALESCE(MAX(id), 0)
                                 FROM Videos
                                 """).fetchall()

        fk_page_id = int(request.form["page_id"])
        new_title = request.form["title"]
        new_date = datetime.datetime.today()
        new_id = max_id[0][0] + 1

        try:

            connect.execute("""
                            INSERT INTO videos (id, title, create_at, page_id)
                            VALUES (?, ?, ?, ?)
                            """, (new_id, new_title, new_date, fk_page_id))
        except:

            raise Exception("Can't insert into the table videos")

        return "Videos create succesfully", 201

    if request.method == "DELETE":

        title_delete = request.form["title"]

        try:

            connect.execute(f"""
                            DELETE From Videos
                            WHERE
                            title = '{title_delete}'
                            """)

        except:

            raise Exception(
                f"Can't Delete the row with the name {title_delete}")

        return "Videos Deletes", 201


@app.route("/videos_insight", methods=["POST", "GET", "DELETE"])
def videos_insight():

    try:

        engine = sqla.create_engine("sqlite:///Brut.db")
        connect = engine.connect()

    except Exception as e:

        raise Exception("Can't connect to the base, error: " + e)

    if request.method == "GET":

        page = pd.read_sql("""
                            SELECT *
                            FROM Videos_Insight
                            """, connect)

        return jsonify(page.to_dict(orient="index"))

    if request.method == "POST":

        max_id = connect.execute("""
                                 SELECT
                                 COALESCE(MAX(id), 0)
                                 FROM Videos_Insight
                                 """).fetchall()

        fk_video_id = int(request.form["video_id"])
        new_likes = request.form["likes"]
        new_views = request.form["views"]
        new_date = datetime.datetime.today()
        new_id = max_id[0][0] + 1

        try:

            connect.execute("""
                            INSERT INTO videos_insight (id, likes, views,
                                                        create_at, video_id)
                            VALUES (?, ?, ?, ?, ?)
                            """, (new_id, new_likes, new_views, new_date, fk_video_id))
        except:

            raise Exception("Can't insert into the table videos_insight")

        return "Videos_insight create succesfully", 201

    if request.method == "DELETE":

        title_delete = request.form["title"]

        try:

            connect.execute(f"""
                            DELETE From Videos_Insight
                            WHERE
                            video_id =(SELECT id
                                       FROM Videos
                                       WHERE title = '{title_delete}')
                            """)
        except:

            raise Exception("Can't Delete the base")

        return "Videos_Insight Deletes", 201


if __name__ == "main":

    app.run(debug=True)
