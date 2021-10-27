# Importing shared resources (Inheritances)
from Bluedit.api import mysql
from Bluedit.log import error_logger


class HomeGateway:
    def get_all_post(self):
        query_post = f'SELECT * FROM post INNER JOIN profile ON post.UUID = profile.UUID WHERE postStatus = 1 ORDER BY postTime DESC'
        query_category = f'SELECT CatName, PostID FROM post_category'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_post)
            post = cursor.fetchall()

            cursor.execute(query_category)
            category = cursor.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return [post, category]

    def get_all_post_with_conditions(self, target, value):
        query_post = f'SELECT * FROM post INNER JOIN profile ON post.UUID = profile.UUID WHERE postStatus = 1 AND {target} LIKE "%{value}%" ORDER BY postTime DESC'
        query_category = f'SELECT CatName, PostID FROM post_category'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_post)
            post = cursor.fetchall()

            cursor.execute(query_category)
            category = cursor.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return [post, category]

    def select_like_by_userid(self, userid):
        query = f'SELECT PostID, UUID FROM post_favourite WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_save_by_userid(self, userid):
        query = f'SELECT PostID, UUID FROM user_stash WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_r_like_by_userid(self, userid):
        query = f'SELECT ReplyID, UUID FROM reply_favourite WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data