# Importing shared resources (Inheritances)
from Bluedit.api import mysql
from Bluedit.log import error_logger


class AdminGateway():
    def select_all_user(self):
        value = 1
        role = "user"
        query = f'SELECT user.dateCreated, user.UUID, profile.username, user.userRole FROM profile INNER JOIN user ON profile.UUID = ' \
                f'user.UUID WHERE user.activated = {value} AND user.accStatus = {value} AND userRole = "{role}";'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_all_user_by_auth(self):
        value = 1
        role = "user"
        query = f'SELECT user.dateCreated, user.UUID, profile.username, user.userRole FROM profile INNER JOIN user ON profile.UUID = ' \
                f'user.UUID WHERE user.activated = {value} AND userRole = "{role}";'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def update_userrole_by_id(self, userid):
        role = "admin"
        query = f'UPDATE user SET userRole = "{role}" WHERE UUID = "{userid}"'

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

    def select_reported_post_list(self):
        query = f'SELECT post.PostID, postTitle, postContent, COUNT(*) FROM post_blacklist INNER JOIN post ON post.PostID = post_blacklist.PostID GROUP BY PostID'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_reported_reply_list(self):
        query = f'SELECT reply.ReplyID, replyContent, COUNT(*) FROM reply_blacklist INNER JOIN reply ON reply.ReplyID = reply_blacklist.ReplyID GROUP BY ReplyID'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def update_postlock(self, postid):
        query = f'UPDATE post SET postLock = {1} WHERE PostID = "{postid}"'

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

    def update_user_accStatus(self, userid):
        query = f'UPDATE user SET accStatus = {0} WHERE UUID = "{userid}"'

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

    def update_postlock_unlock(self, postid):
        query = f'UPDATE post SET postLock = {0} WHERE PostID = "{postid}"'

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

    def update_user_accStatus_unban(self, userid):
        query = f'UPDATE user SET accStatus = {1} WHERE UUID = "{userid}"'

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

    def select_locked_post(self):
        query = f'SELECT PostID FROM post WHERE postLock = {1} AND postStatus = {1}'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_banned_userid(self):
        role = 'user'
        query = f'SELECT UUID FROM user WHERE activated = {1} AND userRole = "{role}" AND accStatus = {0}'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_lockstatus_by_id(self, postid):
        query = f'SELECT postLock FROM post WHERE PostID = "{postid}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data

    def select_banstatus_by_id(self, userid):
        query = f'SELECT accStatus FROM user WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return data
