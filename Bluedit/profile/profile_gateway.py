# Importing shared resources (Inheritances)
from Bluedit.api import mysql
from Bluedit.log import error_logger


class ProfileGateway:
    def select_exist_name(self, name):
        query = f'SELECT EXISTS(SELECT username FROM profile WHERE username = "{name}")'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchone()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_profile_by_name(self, name):
        query = f'SELECT * FROM profile WHERE username = "{name}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchone()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def update_image_by_nameid(self, path, name, id):
        query = f'UPDATE profile SET profile_img = "{path}" WHERE username = "{name}" and UUID = "{id}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_fa_by_id(self, id):
        query = f'SELECT emailAuth FROM user WHERE UUID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def update_name_by_nameid(self, cur_name, input_name, id):
        query = f'UPDATE profile SET username = "{input_name}" WHERE username = "{cur_name}" and UUID = "{id}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def update_about_by_nameid(self, name, id, about):
        query = f'UPDATE profile SET about = "{about}" WHERE username = "{name}" and UUID = "{id}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_top3user_post_by_name(self, name):
        query_post = f'SELECT * FROM post INNER JOIN profile ON post.UUID = profile.UUID WHERE profile.username = "{name}" AND post.postStatus = {1} ORDER BY postTime DESC LIMIT 3'
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

    def select_user_post_by_name(self, name):
        query_post = f'SELECT * FROM post INNER JOIN profile ON post.UUID = profile.UUID WHERE profile.username = "{name}" AND post.postStatus = {1} ORDER BY postTime DESC'
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

    def select_stashed_post_by_id(self, id):
        query_post = f'SELECT * FROM user_stash U INNER JOIN post P ON U.PostID = P.PostID INNER JOIN profile PF ON P.UUID = PF.UUID WHERE U.UUID = "{id}" AND P.postStatus = {1} ORDER BY postTime DESC'
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

    def select_upvote_post_by_id(self, id):
        query_post = f'SELECT * FROM post_favourite U INNER JOIN post P ON U.PostID = P.PostID INNER JOIN profile PF ON P.UUID = PF.UUID WHERE U.UUID = "{id}" AND P.postStatus = {1} ORDER BY postTime DESC'
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

    def select_upvoted_reply_by_id(self, id):
        query = f'SELECT * FROM reply_favourite RF INNER JOIN reply R ON RF.ReplyID = R.ReplyID INNER JOIN post PT ON R.PostID = PT.PostID INNER JOIN profile P ON R.UUID = P.UUID WHERE RF.UUID = "{id}" AND R.replyStatus = {1};'

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

    def select_commented_post_by_id(self, id):
        query = f'SELECT * FROM reply INNER JOIN post ON post.PostID = reply.PostID INNER JOIN profile ON post.UUID = profile.UUID WHERE reply.UUID = "{id}" AND replyStatus = {1} ORDER BY replyTime DESC'

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
