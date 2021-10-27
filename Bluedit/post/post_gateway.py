# Importing shared resources (Inheritances)
from Bluedit.api import mysql
from Bluedit.log import error_logger


class PostGateway:
    def insert_post(self, post):
        query_post = f'INSERT INTO post VALUES ("{post.postID}", "{post.postTitle}", "{post.postContent}", "{post.postTime}", {post.postLikes}, {post.postReplies}, {post.postSaves}, "{post.postImage}", {post.postStatus}, {post.postLock}, "{post.UUID}")'
        query_update_profile = f'UPDATE profile SET posted = posted + {1} WHERE UUID = "{post.UUID}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_post)

            for item in post.postCat:
                query_category = f'INSERT INTO post_category (CatName, PostID) VALUES ("{item}", "{post.postID}")'
                cursor.execute(query_category)

            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def insert_replies(self, post_id, user_id, comment, time, reply_id):
        query_reply = f'INSERT INTO reply VALUES ("{reply_id}", "{comment}", "{post_id}", "{time}", {1}, {0}, "{user_id}")'
        query_update_profile = f'UPDATE profile SET commented = commented + {1} WHERE UUID = "{user_id}"'
        query_update_post = f'UPDATE post SET postReplies = (postReplies + {1}) WHERE PostID = "{post_id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_reply)
            cursor.execute(query_update_profile)
            cursor.execute(query_update_post)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_post_by_id(self, id):
        query_post = f'SELECT * FROM post INNER JOIN profile ON post.UUID = profile.UUID WHERE post.PostID = "{id}" and post.postStatus = {1}'
        query_category = f'SELECT CatName, PostID FROM post_category WHERE PostID = "{id}"'

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

    def select_replies_by_postid(self, postid):
        query_replies = f'SELECT * FROM reply INNER JOIN profile ON reply.UUID = profile.UUID WHERE reply.PostID = "{postid}" AND reply.replyStatus = {1} ORDER BY replyTime DESC'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_replies)
            replies = cursor.fetchall()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return replies

    def select_like_by_id(self, id):
        query = f'SELECT PostID, UUID FROM post_favourite WHERE PostID = "{id}"'

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

    def update_post_like_increment(self, id, userid):
        query_insert_fav = f'INSERT INTO post_favourite (PostID, UUID) VALUES ("{id}", "{userid}")'
        query_update_profile = f'UPDATE profile SET upvoted = (upvoted + {1})  WHERE UUID = "{userid}"'
        query_update_post = f'UPDATE post SET postLikes = (postLikes + {1}) WHERE PostID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_insert_fav)
            cursor.execute(query_update_post)
            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def update_post_like_decrement(self, id, userid):
        query_delete_fav = f'DELETE FROM post_favourite WHERE PostID = "{id}" AND UUID = "{userid}"'
        query_update_profile = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{userid}"'
        query_update_post = f'UPDATE post SET postLikes = (postLikes - {1}) WHERE PostID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_delete_fav)
            cursor.execute(query_update_post)
            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_saved_by_id(self, postid):
        query = f'SELECT PostID, UUID FROM user_stash WHERE PostID = "{postid}"'

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

    def select_rlike_by_id(self, reply_id):
        query = f'SELECT ReplyID, UUID FROM reply_favourite WHERE ReplyID = "{reply_id}"'

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

    def update_post_save_increment(self, id, userid):
        query_insert_save = f'INSERT INTO user_stash (PostID, UUID) VALUES ("{id}", "{userid}")'
        query_update_profile = f'UPDATE profile SET saved = (saved + {1})  WHERE UUID = "{userid}"'
        query_update_post = f'UPDATE post SET postSaves = (postSaves + {1}) WHERE PostID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_insert_save)
            cursor.execute(query_update_post)
            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def update_post_save_decrement(self, id, userid):
        query_delete_save = f'DELETE FROM user_stash WHERE PostID = "{id}" AND UUID = "{userid}"'
        query_update_profile = f'UPDATE profile SET saved = (saved - {1})  WHERE UUID = "{userid}"'
        query_update_post = f'UPDATE post SET postSaves = (postSaves - {1}) WHERE PostID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_delete_save)
            cursor.execute(query_update_post)
            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def update_reply_like_increment(self, replyid, userid):
        query_insert_like = f'INSERT INTO reply_favourite (ReplyID, UUID) VALUES ("{replyid}", "{userid}")'
        query_update_profile = f'UPDATE profile SET upvoted = (upvoted + {1})  WHERE UUID = "{userid}"'
        query_update_post = f'UPDATE reply SET replyLikes = (replyLikes + {1}) WHERE ReplyID = "{replyid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_insert_like)
            cursor.execute(query_update_post)
            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def update_reply_like_decrement(self, replyid, userid):
        query_delete_like = f'DELETE FROM reply_favourite WHERE ReplyID = "{replyid}" AND UUID = "{userid}"'
        query_update_profile = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{userid}"'
        query_update_post = f'UPDATE reply SET replyLikes = (replyLikes - {1}) WHERE ReplyID = "{replyid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_delete_like)
            cursor.execute(query_update_post)
            cursor.execute(query_update_profile)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_exist_post_by_id(self, post_id):
        query = f'SELECT EXISTS(SELECT * FROM post WHERE PostID = "{post_id}" AND postStatus = {1})'

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

    def select_exist_reply_by_id(self, reply_id):
        query = f'SELECT EXISTS(SELECT * FROM reply WHERE ReplyID = "{reply_id}" AND replyStatus = {1})'

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

    def update_post(self, post_id, title, content):
        query = f'UPDATE post SET postTitle = "{title}", postContent = "{content}" WHERE PostID = "{post_id}" AND postStatus = {1}'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def update_reply(self, reply_id, content):
        query = f'UPDATE reply SET replyContent = "{content}" WHERE ReplyID = "{reply_id}" AND replyStatus = {1}'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_reply_by_replyid(self, reply_id):
        query = f'SELECT * FROM reply R INNER JOIN post PT ON R.PostID = PT.PostID INNER JOIN profile P ON R.UUID = P.UUID WHERE R.ReplyID = "{reply_id}" AND R.replyStatus = {1};'

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

    def delete_post_by_id(self, postid, userid):
        query_like_list = f'SELECT UUID FROM post_favourite WHERE PostID = "{postid}"'
        query_save_list = f'SELECT UUID FROM user_stash WHERE PostID = "{postid}"'
        query_report_list = f'SELECT UUID FROM post_blacklist WHERE PostID = "{postid}"'

        query_reply_list = f'SELECT ReplyID, UUID FROM reply WHERE PostID = "{postid}"'

        query_remove_like = f'DELETE FROM post_favourite WHERE PostID = "{postid}"'
        query_remove_save = f'DELETE FROM user_stash WHERE PostID = "{postid}"'
        query_remove_reported = f'DELETE FROM post_blacklist WHERE PostID = "{postid}"'

        query_remove_post = f'UPDATE post SET postStatus = {0} WHERE PostID = "{postid}"'
        query_decrement_posted = f'UPDATE profile SET posted  = (posted - {1}) WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_like_list)
            like_list = cursor.fetchall()

            cursor.execute(query_remove_like)
            for like in like_list:
                query_decrement_like = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{like[0]}"'
                cursor.execute(query_decrement_like)

            cursor.execute(query_save_list)
            save_list = cursor.fetchall()

            cursor.execute(query_remove_save)
            for save in save_list:
                query_decrement_save = f'UPDATE profile SET saved = (saved - {1})  WHERE UUID = "{save[0]}"'
                cursor.execute(query_decrement_save)

            cursor.execute(query_report_list)
            report_list = cursor.fetchall()

            cursor.execute(query_remove_reported)
            for report in report_list:
                query_decrement_report = f'UPDATE profile SET reported = (reported - {1})  WHERE UUID = "{report[0]}"'
                cursor.execute(query_decrement_report)

            cursor.execute(query_reply_list)
            reply_list = cursor.fetchall()

            for reply in reply_list:
                query_reply_like_list = f'SELECT UUID FROM reply_favourite WHERE ReplyID = "{reply[0]}"'
                cursor.execute(query_reply_like_list)
                reply_like_list = cursor.fetchall()

                for reply_like in reply_like_list:
                    query_decrement_reply_like = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{reply_like[0]}"'
                    cursor.execute(query_decrement_reply_like)

                query_remove_commented = f'UPDATE profile SET commented = (commented - {1}) WHERE UUID = "{reply[1]}"'
                cursor.execute(query_remove_commented)

                query_remove_reply = f'UPDATE reply SET replyStatus = {0} WHERE ReplyID = "{reply[0]}"'
                cursor.execute(query_remove_reply)

            cursor.execute(query_remove_post)
            cursor.execute(query_decrement_posted)

            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def delete_post(self, postid):
        query_like_list = f'SELECT UUID FROM post_favourite WHERE PostID = "{postid}"'
        query_save_list = f'SELECT UUID FROM user_stash WHERE PostID = "{postid}"'
        query_report_list = f'SELECT UUID FROM post_blacklist WHERE PostID = "{postid}"'

        query_reply_list = f'SELECT ReplyID, UUID FROM reply WHERE PostID = "{postid}"'

        query_remove_like = f'DELETE FROM post_favourite WHERE PostID = "{postid}"'
        query_remove_save = f'DELETE FROM user_stash WHERE PostID = "{postid}"'
        query_remove_reported = f'DELETE FROM post_blacklist WHERE PostID = "{postid}"'

        query_remove_post = f'UPDATE post SET postStatus = {0} WHERE PostID = "{postid}"'

        query_get_user = f'SELECT UUID FROM post WHERE PostID = "{postid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_like_list)
            like_list = cursor.fetchall()

            cursor.execute(query_remove_like)
            for like in like_list:
                query_decrement_like = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{like[0]}"'
                cursor.execute(query_decrement_like)

            cursor.execute(query_save_list)
            save_list = cursor.fetchall()

            cursor.execute(query_remove_save)
            for save in save_list:
                query_decrement_save = f'UPDATE profile SET saved = (saved - {1})  WHERE UUID = "{save[0]}"'
                cursor.execute(query_decrement_save)

            cursor.execute(query_report_list)
            report_list = cursor.fetchall()

            cursor.execute(query_remove_reported)
            for report in report_list:
                query_decrement_report = f'UPDATE profile SET reported = (reported - {1})  WHERE UUID = "{report[0]}"'
                cursor.execute(query_decrement_report)

            cursor.execute(query_reply_list)
            reply_list = cursor.fetchall()

            for reply in reply_list:
                query_reply_like_list = f'SELECT UUID FROM reply_favourite WHERE ReplyID = "{reply[0]}"'
                cursor.execute(query_reply_like_list)
                reply_like_list = cursor.fetchall()

                for reply_like in reply_like_list:
                    query_decrement_reply_like = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{reply_like[0]}"'
                    cursor.execute(query_decrement_reply_like)

                query_remove_commented = f'UPDATE profile SET commented = (commented - {1}) WHERE UUID = "{reply[1]}"'
                cursor.execute(query_remove_commented)

                query_remove_reply = f'UPDATE reply SET replyStatus = {0} WHERE ReplyID = "{reply[0]}"'
                cursor.execute(query_remove_reply)

            cursor.execute(query_remove_post)

            cursor.execute(query_get_user)
            user = cursor.fetchone()

            query_decrement_posted = f'UPDATE profile SET posted  = (posted - {1}) WHERE UUID = "{user[0][0]}"'
            cursor.execute(query_decrement_posted)

            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def delete_reply_by_id(self, replyid, userid):
        query_like_list = f'SELECT UUID FROM reply_favourite WHERE ReplyID = "{replyid}"'
        query_report_list = f'SELECT UUID FROM reply_blacklist WHERE ReplyID = "{replyid}"'

        query_get_post = f'SELECT PostID FROM reply WHERE ReplyID = "{replyid}"'

        query_remove_list = f'DELETE FROM reply_favourite WHERE ReplyID = "{replyid}"'
        query_remove_reported = f'DELETE FROM reply_blacklist WHERE ReplyID = "{replyid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_like_list)
            like_list = cursor.fetchall()

            cursor.execute(query_remove_list)
            for like in like_list:
                query_decrement_like = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{like[0]}"'
                cursor.execute(query_decrement_like)

            cursor.execute(query_report_list)
            report_list = cursor.fetchall()

            cursor.execute(query_remove_reported)
            for report in report_list:
                query_decrement_like = f'UPDATE profile SET reported = (reported - {1})  WHERE UUID = "{report[0]}"'
                cursor.execute(query_decrement_like)

            cursor.execute(query_get_post)
            post = cursor.fetchall()

            for i in post:
                query_decrement_replies = f'UPDATE post SET postReplies = (postReplies - {1}) WHERE PostID = "{i[0]}"'
                cursor.execute(query_decrement_replies)

            query_decrement_commented = f'UPDATE profile SET commented = (commented - {1}) WHERE UUID = "{userid}"'
            cursor.execute(query_decrement_commented)

            query_delete_reply = f'UPDATE reply SET replyStatus = {0} WHERE ReplyID = "{replyid}"'
            cursor.execute(query_delete_reply)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def delete_reply(self, replyid):
        query_like_list = f'SELECT UUID FROM reply_favourite WHERE ReplyID = "{replyid}"'
        query_report_list = f'SELECT UUID FROM reply_blacklist WHERE ReplyID = "{replyid}"'

        query_get_post = f'SELECT PostID FROM reply WHERE ReplyID = "{replyid}"'

        query_remove_list = f'DELETE FROM reply_favourite WHERE ReplyID = "{replyid}"'
        query_remove_reported = f'DELETE FROM reply_blacklist WHERE ReplyID = "{replyid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_like_list)
            like_list = cursor.fetchall()

            cursor.execute(query_remove_list)
            for like in like_list:
                query_decrement_like = f'UPDATE profile SET upvoted = (upvoted - {1})  WHERE UUID = "{like[0]}"'
                cursor.execute(query_decrement_like)

            cursor.execute(query_report_list)
            report_list = cursor.fetchall()

            cursor.execute(query_remove_reported)
            for report in report_list:
                query_decrement_like = f'UPDATE profile SET reported = (reported - {1})  WHERE UUID = "{report[0]}"'
                cursor.execute(query_decrement_like)

            cursor.execute(query_get_post)
            post = cursor.fetchall()

            for i in post:
                query_decrement_replies = f'UPDATE post SET postReplies = (postReplies - {1}) WHERE PostID = "{i[0]}"'
                cursor.execute(query_decrement_replies)

            query_user = f'SELECT UUID FROM reply WHERE ReplyID = "{replyid}"'
            cursor.execute(query_user)
            user = cursor.fetchone()

            query_decrement_commented = f'UPDATE profile SET commented = (commented - {1}) WHERE UUID = "{user[0][0]}"'
            cursor.execute(query_decrement_commented)

            query_delete_reply = f'UPDATE reply SET replyStatus = {0} WHERE ReplyID = "{replyid}"'
            cursor.execute(query_delete_reply)

            conn.commit()
            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_exist_post_is_mine(self, postid, userid):
        query = f'SELECT EXISTS(SELECT * FROM post WHERE PostID = "{postid}" AND UUID = "{userid}" AND postStatus = {1})'

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

    def select_exist_reply_is_mine(self, replyid, userid):
        query = f'SELECT EXISTS(SELECT * FROM reply WHERE ReplyID = "{replyid}" AND UUID = "{userid}" AND replyStatus = {1})'

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

    def insert_reportedpost(self, postid, userid):
        query = f'INSERT INTO post_blacklist (PostID, UUID) VALUES ("{postid}", "{userid}")'
        query_update = f'UPDATE profile SET reported = (reported + {1}) WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            cursor.execute(query_update)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def insert_reportedreply(self, replyid, userid):
        query = f'INSERT INTO reply_blacklist (ReplyID, UUID) VALUES ("{replyid}", "{userid}")'
        query_update = f'UPDATE profile SET reported = (reported + {1}) WHERE UUID = "{userid}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            cursor.execute(query_update)
            conn.commit()

            conn.close()
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
        return True

    def select_exist_reportuser(self, postid, userid):
        query = f'SELECT EXISTS(SELECT * FROM post_blacklist WHERE PostID = "{postid}" AND UUID = "{userid}")'

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

    def select_exist_reply_reportuser(self, replyid, userid):
        query = f'SELECT EXISTS(SELECT * FROM reply_blacklist WHERE ReplyID = "{replyid}" AND UUID = "{userid}")'

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
