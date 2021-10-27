from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import logout_user
from flask_wtf.csrf import CSRFError
from werkzeug.exceptions import RequestEntityTooLarge
from Bluedit.log import error_logger
from Bluedit.api import csrf

error_bp = Blueprint('error_bp', __name__, template_folder="templates")


@error_bp.app_errorhandler(500)
def internal_service_error(e):
    session.clear()
    return render_template("error.html")


@error_bp.app_errorhandler(404)
def page_not_found_error(e):
    error_logger.error("Encountered error while accessing a webpage - " + str(e))

    session.clear()
    return render_template("error.html")


@error_bp.app_errorhandler(RequestEntityTooLarge)
def request_entity_too_large(e):
    error_logger.error("Encountered error while uploading file - " + str(e))

    return redirect(url_for('home_bp.home'))


@error_bp.app_errorhandler(CSRFError)
def missing_csrf_token(e):
    error_logger.error("Encountered error while processing post request - CSRF Error. Missing CSRF Token")

    logout_user()
    session.clear()
    return redirect(url_for('auth_bp.login'))

