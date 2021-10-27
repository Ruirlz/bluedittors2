# Importing shared resources (Inheritances)
from Bluedit.api import mysql
from Bluedit.log import error_logger


class AccountGateway:
    def select_id_name_role_by_id(self, id):
        query = f'SELECT U.UUID, P.username, U.userRole FROM user U INNER JOIN profile P ON U.UUID = P.UUID WHERE U.UUID = "{id}"'

        try:
            conn = mysql.connect()
            cur = conn.cursor()

            cur.execute(query)
            data = cur.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_account_by_email(self, email):
        query = f'SELECT * FROM user WHERE email = "{email}"'

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

    def select_exist_username(self, username):
        query = f'SELECT EXISTS(SELECT * FROM profile WHERE username = "{username}")'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_exist_email(self, email):
        query = f'SELECT EXISTS(SELECT * FROM user WHERE email = "{email}")'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_exist_salt(self, salt):
        query = f'SELECT EXISTS(SELECT * FROM user WHERE salt = "{salt}")'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_exist_otpkey(self, otpkey):
        query = f'SELECT EXISTS(SELECT * FROM user WHERE otpkey = "{otpkey}")'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_otpkey_by_email(self, email):
        query = f'SELECT otpkey FROM user WHERE email = "{email}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def insert_new_user(self, account, uname):
        default_role = "user"
        default_about = "Hello there, I am new to Bluedit."
        default_img = "../../static/profile_image/default/default_profile.png"
        default_num = 0

        query_user = f'INSERT INTO user VALUES ("{account.userID}","{account.email}","{account.password}","{account.salt}",{account.accStatus}, "{account.dateCreated}","{default_role}", {account.activated}, {account.emailAuth}, "{account.otpkey}", "{account.passwordDate}")'
        query_profile = f'INSERT INTO profile VALUES ("{account.userID}", "{uname}", "{default_about}", {default_num}, {default_num}, {default_num}, {default_num}, {default_num}, "{default_img}")'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_user)
            cursor.execute(query_profile)

            conn.commit()

            conn.close()
            return True
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_act_status_by_email(self, email):
        query = f'SELECT activated FROM user WHERE email = "{email}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def update_password_by_email(self, email, pw, salt, time):
        query = f'UPDATE user SET password = "{pw}", salt = "{salt}", passwordDate = "{time}" WHERE email = "{email}"'
        query_get_id = f'SELECT UUID FROM user WHERE email = "{email}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            cursor.execute(query_get_id)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def update_password_by_id(self, id, pw, salt, time):
        query = f'UPDATE user SET password = "{pw}", salt = "{salt}", passwordDate = "{time}" WHERE UUID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            conn.close()
            return True
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def update_act_status_by_email(self, email):
        activate_value = 1

        query = f'UPDATE user SET activated = {activate_value} WHERE email = "{email}"'
        query_get_id = f'SELECT UUID FROM user WHERE email = "{email}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            cursor.execute(query_get_id)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_authenticate_email(self, id, email):
        query = f'SELECT EXISTS(SELECT email FROM user WHERE email = "{email}" AND UUID = "{id}")'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def update_email_by_id(self, email, id, time):
        auth = 1
        activated = 0
        query = f'UPDATE user SET email = "{email}", dateCreated = "{time}", activated = {activated}, emailAuth = {auth} WHERE UUID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            conn.close()
            return True
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_passwordsalt_by_id(self, id):
        query = f'SELECT password, salt FROM user WHERE UUID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def update_tfa_by_id(self, id, tfa):
        query = f'UPDATE user SET emailAuth = {int(tfa)} WHERE UUID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query)
            conn.commit()

            conn.close()
            return True
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def delete_account(self, id):
        postStatus = 0
        query_delete_acc = f'DELETE FROM user WHERE UUID = "{id}"'
        query_update_post = f'UPDATE post SET postStatus = {postStatus} WHERE UUID = "{id}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_delete_acc)
            cursor.execute(query_update_post)
            conn.commit()

            conn.close()
            return True
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)

    def select_userid_by_email(self, email):
        query_get_id = f'SELECT UUID FROM user WHERE email = "{email}"'

        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(query_get_id)
            data = cursor.fetchone()

            conn.close()
            return data
        except Exception as e:
            error_logger.error("Encountered error while accessing the database - " + str(e))
            return str(e)
